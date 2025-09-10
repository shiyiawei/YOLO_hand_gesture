# -*- coding: utf-8 -*-
import sys  # 导入sys模块，用于访问与Python解释器相关的变量和函数
import time  # 导入time模块，用于获取当前时间

import cv2  # 导入OpenCV库，用于图像处理
from QtFusion.widgets import QMainWindow  # 从QtFusion库导入FBaseWindow类，用于创建主窗口
from QtFusion.handlers import MediaHandler  # 从QtFusion库导入MediaHandler类，用于处理媒体流
from QtFusion.utils import drawRectBox, get_cls_color  # 从QtFusion库导入drawRectBox函数，用于在图像上绘制矩形框
from PySide6 import QtWidgets, QtCore  # 导入PySide6库的QtWidgets和QtCore模块，用于创建GUI
from QtFusion.path import abs_path
from QtFusion.config import QF_Config
from YOLOv8v5Model import YOLOv8v5Detector  # 从YOLOv8Model模块导入YOLOv8Detector类，用于物体检测
from datasets.RPS.label_name import Label_list

QF_Config.set_verbose(False)


class MainWindow(QMainWindow):  # 定义MainWindow类，继承自FBaseWindow类
    def __init__(self):  # 定义构造函数
        super().__init__()  # 调用父类的构造函数
        self.resize(850, 500)  # 设置窗口的大小
        self.label = QtWidgets.QLabel(self)  # 创建一个QLabel对象，用于显示图像
        self.label.setGeometry(0, 0, 850, 500)  # 设置QLabel对象的几何形状

    def keyPressEvent(self, event):  # 定义keyPressEvent函数，用于处理键盘事件
        if event.key() == QtCore.Qt.Key.Key_Q:  # 如果按下的键是Q键
            self.close()  # 关闭窗口


def frame_process(image):  # 定义frame_process函数，用于处理每一帧图像
    image = cv2.resize(image, (850, 500))  # 调整图像的大小
    pre_img = model.preprocess(image)  # 对图像进行预处理

    t1 = time.time()  # 获取当前时间
    pred, superimposed_img = model.predict(pre_img)  # 使用模型进行预测
    t2 = time.time()  # 获取当前时间
    use_time = t2 - t1  # 计算预测所用的时间

    print("推理时间: %.2f" % use_time)  # 打印预测所用的时间
    det = pred[0]  # 获取预测结果
    # 如果有检测信息则进入
    if det is not None and len(det):
        det_info = model.postprocess(pred)  # 对预测结果进行后处理
        for info in det_info:  # 遍历检测信息
            name, bbox, conf, cls_id = info['class_name'], info['bbox'], info['score'], info[
                'class_id']  # 获取类名、边界框、置信度和类别ID
            label = '%s %.0f%%' % (name, conf * 100)  # 创建标签，包含类名和置信度
            # 画出检测到的目标物
            image = drawRectBox(image, bbox, alpha=0.2, addText=label, color=colors[cls_id])  # 在图像上绘制矩形框，并添加标签和颜色

    window.dispImage(window.label, image)  # 在窗口的label控件上显示图像


cls_name = Label_list   # 定义类名列表

model = YOLOv8v5Detector()  # 创建YOLOv8Detector对象
model.load_model(abs_path("weights/best-yolov8n.pt", path_type="current"))  # 加载预训练的YOLOv8模型
colors = get_cls_color(model.names)  # 获取类别颜色

app = QtWidgets.QApplication(sys.argv)  # 创建QApplication对象
window = MainWindow()  # 创建MainWindow对象

videoHandler = MediaHandler(fps=30)  # 创建MediaHandler对象，设置帧率为30
videoHandler.frameReady.connect(frame_process)  # 当有新的帧准备好时，调用frame_process函数
videoHandler.setDevice(device=0)  # 设置设备为0，即默认的摄像头
videoHandler.startMedia()  # 开始处理媒体流

# 显示窗口
window.show()
# 进入 Qt 应用程序的主循环
sys.exit(app.exec())
