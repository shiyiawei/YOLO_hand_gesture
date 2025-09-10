# -*- coding: utf-8 -*-
import random  # 导入random模块，用于生成随机数
import sys  # 导入sys模块，用于访问与Python解释器相关的变量和函数
import time  # 导入time模块，用于处理时间
from QtFusion.config import QF_Config
import cv2  # 导入OpenCV库，用于处理图像
from QtFusion.widgets import QMainWindow  # 从QtFusion库中导入FBaseWindow类，用于创建窗口
from QtFusion.utils import cv_imread, drawRectBox  # 从QtFusion库中导入cv_imread和drawRectBox函数，用于读取图像和绘制矩形框
from PySide6 import QtWidgets, QtCore  # 导入PySide6库中的QtWidgets和QtCore模块，用于创建GUI
from QtFusion.path import abs_path
from YOLOv8v5Model import YOLOv8v5Detector  # 从YOLOv8Model模块中导入YOLOv8Detector类，用于加载YOLOv8模型并进行目标检测
from datasets.RPS.label_name import Label_list

QF_Config.set_verbose(False)

cls_name = Label_list  # 定义类名列表
colors = [[random.randint(0, 255) for _ in range(3)] for _ in range(len(cls_name))]  # 为每个目标类别生成一个随机颜色

model = YOLOv8v5Detector()  # 创建YOLOv8Detector对象
model.load_model(abs_path("weights/best-yolov8n.pt", path_type="current"))  # 加载预训练的YOLOv8模型


class MainWindow(QMainWindow):  # 定义MainWindow类，继承自FBaseWindow类
    def __init__(self):  # 定义构造函数
        super().__init__()  # 调用父类的构造函数
        self.resize(850, 500)  # 设置窗口的大小
        self.label = QtWidgets.QLabel(self)  # 创建一个QLabel对象
        self.label.setGeometry(0, 0, 850, 500)  # 设置QLabel的位置和大小

    def keyPressEvent(self, event):  # 定义keyPressEvent函数，用于处理键盘事件
        if event.key() == QtCore.Qt.Key.Key_Q:  # 如果按下的是Q键
            self.close()  # 关闭窗口


if __name__ == '__main__':  # 如果当前模块是主模块
    app = QtWidgets.QApplication(sys.argv)  # 创建QApplication对象
    window = MainWindow()  # 创建MainWindow对象

    img_path = abs_path("test_media/RPS_SIXU_B00143.jpg")  # 定义图像文件的路径
    image = cv_imread(img_path)  # 使用cv_imread函数读取图像

    image = cv2.resize(image, (850, 500))  # 将图像大小调整为850x500
    pre_img = model.preprocess(image)  # 对图像进行预处理

    t1 = time.time()  # 获取当前时间（开始时间）
    pred, superimposed_img = model.predict(pre_img)  # 使用模型进行预测
    t2 = time.time()  # 获取当前时间（结束时间）
    use_time = t2 - t1  # 计算预测所用的时间

    det = pred[0]  # 获取预测结果的第一个元素（检测结果）

    # 如果有检测信息则进入
    if det is not None and len(det):
        det_info = model.postprocess(pred)  # 对预测结果进行后处理
        for info in det_info:  # 遍历检测信息
            # 获取类别名称、边界框、置信度和类别ID
            name, bbox, conf, cls_id = info['class_name'], info['bbox'], info['score'], info['class_id']
            label = '%s %.0f%%' % (name, conf * 100)  # 创建标签，包含类别名称和置信度
            # 画出检测到的目标物
            image = drawRectBox(image, bbox, alpha=0.2, addText=label, color=colors[cls_id])  # 在图像上绘制边界框和标签

    print("推理时间: %.2f" % use_time)  # 打印预测所用的时间
    window.dispImage(window.label, image)  # 在窗口的label上显示图像
    # 显示窗口
    window.show()
    # 进入 Qt 应用程序的主循环
    sys.exit(app.exec())
