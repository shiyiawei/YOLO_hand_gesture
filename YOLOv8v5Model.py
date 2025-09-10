# -*- coding: utf-8 -*-
import cv2  # 导入OpenCV库，用于处理图像和视频
import torch
from QtFusion.models import Detector, HeatmapGenerator  # 从QtFusion库中导入Detector抽象基类
from datasets.RPS.label_name import Chinese_name  # 从datasets库中导入Chinese_name字典，用于获取类别的中文名称
from ultralytics import YOLO  # 从ultralytics库中导入YOLO类，用于加载YOLO模型
from ultralytics.utils.torch_utils import select_device  # 从ultralytics库中导入select_device函数，用于选择设备

device = "cuda:0" if torch.cuda.is_available() else "cpu"

ini_params = {
    'device': device,  # 设备类型，这里设置为CPU
    'conf': 0.25,  # 物体置信度阈值
    'iou': 0.5,  # 用于非极大值抑制的IOU阈值
    'classes': None,  # 类别过滤器，这里设置为None表示不过滤任何类别
    'verbose': False
}


def count_classes(det_info, class_names):
    """
    Count the number of each class in the detection info.

    :param det_info: List of detection info, each item is a list like [class_name, bbox, conf, class_id]
    :param class_names: List of all possible class names
    :return: A list with counts of each class
    """
    count_dict = {name: 0 for name in class_names}  # 创建一个字典，用于存储每个类别的数量
    for info in det_info:  # 遍历检测信息
        class_name = info['class_name']  # 获取类别名称
        if class_name in count_dict:  # 如果类别名称在字典中
            count_dict[class_name] += 1  # 将该类别的数量加1

    # Convert the dictionary to a list in the same order as class_names
    count_list = [count_dict[name] for name in class_names]  # 将字典转换为列表，列表的顺序与class_names相同
    return count_list  # 返回列表


class YOLOv8v5Detector(Detector):  # 定义YOLOv8Detector类，继承自Detector类
    def __init__(self, params=None):  # 定义构造函数
        super().__init__(params)  # 调用父类的构造函数
        self.model = None
        self.img = None  # 初始化图像为None
        self.names = list(Chinese_name.values())  # 获取所有类别的中文名称
        self.params = params if params else ini_params  # 如果提供了参数则使用提供的参数，否则使用默认参数

        # 创建heatmap
        self.heatmap = HeatmapGenerator(heatmap_intensity=0.4, hist_eq_threshold=200)

    def load_model(self, model_path):  # 定义加载模型的方法
        self.device = select_device(self.params['device'])  # 选择设备
        self.model = YOLO(model_path, )
        layer = list(self.model.model.children())[0][-3]
        self.heatmap.register_hook(reg_layer=layer)
        names_dict = self.model.names  # 获取类别名称字典
        self.names = [Chinese_name[v] if v in Chinese_name else v for v in names_dict.values()]  # 将类别名称转换为中文
        
        self.model(torch.zeros(1, 3, *[self.imgsz] * 2).to(self.device).
                   type_as(next(self.model.model.parameters())))  # 预热
        self.model(torch.rand(1, 3, *[self.imgsz] * 2).to(self.device).
                   type_as(next(self.model.model.parameters())))  # 预热
        
    def preprocess(self, img):  # 定义预处理方法
        self.img = img  # 保存原始图像
        return img  # 返回处理后的图像

    def predict(self, img):  # 定义预测方法
        results = self.model(img, **ini_params)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        superimposed_img = self.heatmap.get_heatmap(img)
        return results, superimposed_img

    def postprocess(self, pred):  # 定义后处理方法
        results = []  # 初始化结果列表
        for res in pred[0].boxes:
            for box in res:
                # 提前计算并转换数据类型
                class_id = int(box.cls.cpu())
                bbox = box.xyxy.cpu().squeeze().tolist()
                bbox = [int(coord) for coord in bbox]  # 转换边界框坐标为整数

                result = {
                    "class_name": self.names[class_id],  # 类别名称
                    "bbox": bbox,  # 边界框
                    "score": box.conf.cpu().squeeze().item(),  # 置信度
                    "class_id": class_id,  # 类别ID
                }
                results.append(result)  # 将结果添加到列表

        return results  # 返回结果列表

    def set_param(self, params):
        self.params.update(params)
