# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Recognition_UI.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSlider, QStackedWidget, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QToolButton, QVBoxLayout,
    QWidget)
import RecSystem_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(1280, 812)
        MainWindow.setMinimumSize(QSize(1280, 812))
        MainWindow.setMaximumSize(QSize(1280, 812))
        font = QFont()
        font.setFamilies([u"\u534e\u6587\u4eff\u5b8b"])
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/images/icons/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.actionGoogle_Translate = QAction(MainWindow)
        self.actionGoogle_Translate.setObjectName(u"actionGoogle_Translate")
        self.actionHTML_type = QAction(MainWindow)
        self.actionHTML_type.setObjectName(u"actionHTML_type")
        self.actionsoftware_version = QAction(MainWindow)
        self.actionsoftware_version.setObjectName(u"actionsoftware_version")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Layout_main = QVBoxLayout()
        self.Layout_main.setObjectName(u"Layout_main")
        self.title_bar = QFrame(self.centralwidget)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setStyleSheet(u"")
        self.horizontalLayout_12 = QHBoxLayout(self.title_bar)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_12.setContentsMargins(-1, -1, 50, -1)
        self.toolMenu = QHBoxLayout()
        self.toolMenu.setObjectName(u"toolMenu")
        self.toolButton_saveing = QToolButton(self.title_bar)
        self.toolButton_saveing.setObjectName(u"toolButton_saveing")
        self.toolButton_saveing.setMaximumSize(QSize(30, 30))
        self.toolButton_saveing.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_saveing.setAutoFillBackground(False)
        icon1 = QIcon()
        icon1.addFile(u":/images/icons/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_saveing.setIcon(icon1)
        self.toolButton_saveing.setIconSize(QSize(50, 39))
        self.toolButton_saveing.setPopupMode(QToolButton.DelayedPopup)
        self.toolButton_saveing.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.toolButton_saveing.setAutoRaise(False)
        self.toolButton_saveing.setArrowType(Qt.NoArrow)

        self.toolMenu.addWidget(self.toolButton_saveing)

        self.toolButton_author = QToolButton(self.title_bar)
        self.toolButton_author.setObjectName(u"toolButton_author")
        self.toolButton_author.setMaximumSize(QSize(30, 30))
        self.toolButton_author.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_author.setAutoFillBackground(False)
        icon2 = QIcon()
        icon2.addFile(u":/images/icons/author.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_author.setIcon(icon2)
        self.toolButton_author.setIconSize(QSize(50, 39))
        self.toolButton_author.setPopupMode(QToolButton.DelayedPopup)
        self.toolButton_author.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.toolButton_author.setAutoRaise(False)
        self.toolButton_author.setArrowType(Qt.NoArrow)

        self.toolMenu.addWidget(self.toolButton_author)

        self.toolButton_version = QToolButton(self.title_bar)
        self.toolButton_version.setObjectName(u"toolButton_version")
        self.toolButton_version.setMaximumSize(QSize(30, 30))
        self.toolButton_version.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_version.setAutoFillBackground(False)
        icon3 = QIcon()
        icon3.addFile(u":/images/icons/versions.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_version.setIcon(icon3)
        self.toolButton_version.setIconSize(QSize(50, 39))
        self.toolButton_version.setPopupMode(QToolButton.DelayedPopup)
        self.toolButton_version.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.toolButton_version.setAutoRaise(False)
        self.toolButton_version.setArrowType(Qt.NoArrow)

        self.toolMenu.addWidget(self.toolButton_version)


        self.horizontalLayout_12.addLayout(self.toolMenu)

        self.label_title = QLabel(self.title_bar)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setFamilies([u"\u96b6\u4e66"])
        font1.setPointSize(20)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_title.setFont(font1)
        self.label_title.setStyleSheet(u"color: rgb(0\uff0c0\uff0c0);")
        self.label_title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_title)

        self.horizontalLayout_12.setStretch(1, 9)

        self.Layout_main.addWidget(self.title_bar)

        self.Layout_contain = QHBoxLayout()
        self.Layout_contain.setObjectName(u"Layout_contain")
        self.Sidebar = QWidget(self.centralwidget)
        self.Sidebar.setObjectName(u"Sidebar")
        self.Sidebar.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.Sidebar)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 9)
        self.frame = QFrame(self.Sidebar)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(216, 300))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.toolButton_camera = QToolButton(self.frame)
        self.toolButton_camera.setObjectName(u"toolButton_camera")
        self.toolButton_camera.setGeometry(QRect(0, 152, 40, 42))
        self.toolButton_camera.setMinimumSize(QSize(40, 40))
        self.toolButton_camera.setMaximumSize(QSize(45, 45))
        self.toolButton_camera.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_camera.setAutoFillBackground(False)
        icon4 = QIcon()
        icon4.addFile(u":/images/icons/g1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_camera.setIcon(icon4)
        self.toolButton_camera.setIconSize(QSize(50, 39))
        self.toolButton_camera.setPopupMode(QToolButton.DelayedPopup)
        self.toolButton_camera.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.toolButton_camera.setAutoRaise(False)
        self.toolButton_camera.setArrowType(Qt.NoArrow)
        self.textEdit_camera = QTextEdit(self.frame)
        self.textEdit_camera.setObjectName(u"textEdit_camera")
        self.textEdit_camera.setGeometry(QRect(50, 160, 161, 30))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_camera.sizePolicy().hasHeightForWidth())
        self.textEdit_camera.setSizePolicy(sizePolicy)
        self.textEdit_camera.setMinimumSize(QSize(150, 30))
        self.textEdit_camera.setMaximumSize(QSize(280, 40))
        font2 = QFont()
        font2.setFamilies([u"12pt \u534e\u4e3a\u4eff\u5b8b"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        self.textEdit_camera.setFont(font2)
        self.textEdit_camera.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_camera.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.textEdit_camera.setLineWrapMode(QTextEdit.NoWrap)
        self.textEdit_camera.setReadOnly(True)
        self.toolButton_file = QToolButton(self.frame)
        self.toolButton_file.setObjectName(u"toolButton_file")
        self.toolButton_file.setGeometry(QRect(0, 54, 40, 42))
        self.toolButton_file.setMinimumSize(QSize(40, 40))
        self.toolButton_file.setMaximumSize(QSize(45, 45))
        self.toolButton_file.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_file.setAutoFillBackground(False)
        icon5 = QIcon()
        icon5.addFile(u":/images/icons/recovery.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_file.setIcon(icon5)
        self.toolButton_file.setIconSize(QSize(50, 40))
        self.toolButton_file.setPopupMode(QToolButton.DelayedPopup)
        self.toolButton_file.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.toolButton_file.setAutoRaise(False)
        self.toolButton_file.setArrowType(Qt.NoArrow)
        self.textEdit_image = QTextEdit(self.frame)
        self.textEdit_image.setObjectName(u"textEdit_image")
        self.textEdit_image.setGeometry(QRect(50, 61, 161, 30))
        sizePolicy.setHeightForWidth(self.textEdit_image.sizePolicy().hasHeightForWidth())
        self.textEdit_image.setSizePolicy(sizePolicy)
        self.textEdit_image.setMinimumSize(QSize(150, 30))
        self.textEdit_image.setMaximumSize(QSize(280, 40))
        self.textEdit_image.setFont(font2)
        self.textEdit_image.setLayoutDirection(Qt.LeftToRight)
        self.textEdit_image.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_image.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.textEdit_image.setLineWrapMode(QTextEdit.NoWrap)
        self.textEdit_image.setReadOnly(True)
        self.toolButton_model = QToolButton(self.frame)
        self.toolButton_model.setObjectName(u"toolButton_model")
        self.toolButton_model.setGeometry(QRect(0, 258, 40, 40))
        self.toolButton_model.setMinimumSize(QSize(40, 40))
        self.toolButton_model.setMaximumSize(QSize(45, 45))
        self.toolButton_model.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_model.setAutoFillBackground(False)
        icon6 = QIcon()
        icon6.addFile(u":/images/icons/model.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_model.setIcon(icon6)
        self.toolButton_model.setIconSize(QSize(40, 39))
        self.toolButton_model.setPopupMode(QToolButton.DelayedPopup)
        self.toolButton_model.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.toolButton_model.setAutoRaise(False)
        self.toolButton_model.setArrowType(Qt.NoArrow)
        self.textEdit_model = QTextEdit(self.frame)
        self.textEdit_model.setObjectName(u"textEdit_model")
        self.textEdit_model.setGeometry(QRect(50, 262, 161, 30))
        sizePolicy.setHeightForWidth(self.textEdit_model.sizePolicy().hasHeightForWidth())
        self.textEdit_model.setSizePolicy(sizePolicy)
        self.textEdit_model.setMinimumSize(QSize(150, 30))
        self.textEdit_model.setMaximumSize(QSize(280, 40))
        self.textEdit_model.setFont(font2)
        self.textEdit_model.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_model.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.textEdit_model.setLineWrapMode(QTextEdit.NoWrap)
        self.textEdit_model.setReadOnly(True)
        self.toolButton_folder = QToolButton(self.frame)
        self.toolButton_folder.setObjectName(u"toolButton_folder")
        self.toolButton_folder.setGeometry(QRect(0, 102, 40, 40))
        self.toolButton_folder.setMinimumSize(QSize(40, 40))
        self.toolButton_folder.setMaximumSize(QSize(45, 45))
        self.toolButton_folder.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_folder.setAutoFillBackground(False)
        icon7 = QIcon()
        icon7.addFile(u":/images/icons/folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_folder.setIcon(icon7)
        self.toolButton_folder.setIconSize(QSize(50, 39))
        self.toolButton_folder.setPopupMode(QToolButton.DelayedPopup)
        self.toolButton_folder.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.toolButton_folder.setAutoRaise(False)
        self.toolButton_folder.setArrowType(Qt.NoArrow)
        self.textEdit_imgFolder = QTextEdit(self.frame)
        self.textEdit_imgFolder.setObjectName(u"textEdit_imgFolder")
        self.textEdit_imgFolder.setGeometry(QRect(50, 110, 161, 30))
        sizePolicy.setHeightForWidth(self.textEdit_imgFolder.sizePolicy().hasHeightForWidth())
        self.textEdit_imgFolder.setSizePolicy(sizePolicy)
        self.textEdit_imgFolder.setMinimumSize(QSize(150, 30))
        self.textEdit_imgFolder.setMaximumSize(QSize(280, 40))
        self.textEdit_imgFolder.setFont(font2)
        self.textEdit_imgFolder.setLayoutDirection(Qt.LeftToRight)
        self.textEdit_imgFolder.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_imgFolder.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.textEdit_imgFolder.setLineWrapMode(QTextEdit.NoWrap)
        self.textEdit_imgFolder.setReadOnly(True)
        self.toolButton_video = QToolButton(self.frame)
        self.toolButton_video.setObjectName(u"toolButton_video")
        self.toolButton_video.setGeometry(QRect(0, 204, 40, 40))
        self.toolButton_video.setMinimumSize(QSize(40, 40))
        self.toolButton_video.setMaximumSize(QSize(45, 45))
        self.toolButton_video.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_video.setAutoFillBackground(False)
        icon8 = QIcon()
        icon8.addFile(u":/images/icons/video.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_video.setIcon(icon8)
        self.toolButton_video.setIconSize(QSize(40, 40))
        self.toolButton_video.setPopupMode(QToolButton.DelayedPopup)
        self.toolButton_video.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.toolButton_video.setAutoRaise(False)
        self.toolButton_video.setArrowType(Qt.NoArrow)
        self.textEdit_video = QTextEdit(self.frame)
        self.textEdit_video.setObjectName(u"textEdit_video")
        self.textEdit_video.setGeometry(QRect(50, 210, 161, 30))
        sizePolicy.setHeightForWidth(self.textEdit_video.sizePolicy().hasHeightForWidth())
        self.textEdit_video.setSizePolicy(sizePolicy)
        self.textEdit_video.setMinimumSize(QSize(150, 30))
        self.textEdit_video.setMaximumSize(QSize(280, 40))
        self.textEdit_video.setFont(font2)
        self.textEdit_video.setLayoutDirection(Qt.LeftToRight)
        self.textEdit_video.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_video.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.textEdit_video.setLineWrapMode(QTextEdit.NoWrap)
        self.textEdit_video.setReadOnly(True)
        self.loginTitle = QToolButton(self.frame)
        self.loginTitle.setObjectName(u"loginTitle")
        self.loginTitle.setGeometry(QRect(-2, 670, 45, 45))
        self.loginTitle.setMinimumSize(QSize(45, 45))
        self.loginTitle.setMaximumSize(QSize(45, 45))
        self.loginTitle.setCursor(QCursor(Qt.PointingHandCursor))
        self.loginTitle.setAutoFillBackground(False)
        self.loginTitle.setStyleSheet(u"QToolButton{\n"
"	border-image: url(:/login/icons/user.png);\n"
"	background-color: transparent;\n"
"	border-radius:5px;\n"
"	border:3px;\n"
"}\n"
"\n"
"QToolButton::hover{\n"
"     border:2px;\n"
"}\n"
"\n"
"QToolButton::pressed{\n"
"     border:1px;\n"
"}")
        self.loginTitle.setIconSize(QSize(40, 40))
        self.loginTitle.setPopupMode(QToolButton.MenuButtonPopup)
        self.loginTitle.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.loginTitle.setAutoRaise(False)
        self.loginTitle.setArrowType(Qt.NoArrow)
        self.toolButton_menu = QToolButton(self.frame)
        self.toolButton_menu.setObjectName(u"toolButton_menu")
        self.toolButton_menu.setGeometry(QRect(0, 6, 40, 40))
        self.toolButton_menu.setMinimumSize(QSize(40, 40))
        self.toolButton_menu.setMaximumSize(QSize(45, 45))
        self.toolButton_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_menu.setAutoFillBackground(False)
        icon9 = QIcon()
        icon9.addFile(u":/images/icons/burger-menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_menu.setIcon(icon9)
        self.toolButton_menu.setIconSize(QSize(50, 39))
        self.toolButton_menu.setPopupMode(QToolButton.DelayedPopup)
        self.toolButton_menu.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.toolButton_menu.setAutoRaise(False)
        self.toolButton_menu.setArrowType(Qt.NoArrow)
        self.pushButton_hide = QPushButton(self.frame)
        self.pushButton_hide.setObjectName(u"pushButton_hide")
        self.pushButton_hide.setGeometry(QRect(50, 11, 161, 33))
        self.pushButton_hide.setMinimumSize(QSize(150, 30))
        self.pushButton_hide.setMaximumSize(QSize(280, 40))
        self.pushButton_hide.setFont(font2)
        self.pushButton_hide.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.frame)


        self.Layout_contain.addWidget(self.Sidebar)

        self.dispSide = QVBoxLayout()
        self.dispSide.setObjectName(u"dispSide")
        self.dispSide.setContentsMargins(-1, 15, -1, -1)
        self.Layout_slide = QHBoxLayout()
        self.Layout_slide.setSpacing(0)
        self.Layout_slide.setObjectName(u"Layout_slide")
        self.Layout_slide.setContentsMargins(45, -1, 55, -1)
        self.layer_slide_conf = QHBoxLayout()
        self.layer_slide_conf.setObjectName(u"layer_slide_conf")
        self.layer_slide_conf.setContentsMargins(-1, -1, 15, -1)
        self.label_slide_conf = QLabel(self.centralwidget)
        self.label_slide_conf.setObjectName(u"label_slide_conf")
        self.label_slide_conf.setMinimumSize(QSize(90, 35))
        self.label_slide_conf.setMaximumSize(QSize(120, 16777215))
        font3 = QFont()
        font3.setFamilies([u"\u534e\u6587\u4eff\u5b8b"])
        font3.setPointSize(14)
        self.label_slide_conf.setFont(font3)

        self.layer_slide_conf.addWidget(self.label_slide_conf)

        self.slider_conf = QSlider(self.centralwidget)
        self.slider_conf.setObjectName(u"slider_conf")
        self.slider_conf.setStyleSheet(u"color: rgb(159,168,218);")
        self.slider_conf.setValue(25)
        self.slider_conf.setOrientation(Qt.Horizontal)

        self.layer_slide_conf.addWidget(self.slider_conf)


        self.Layout_slide.addLayout(self.layer_slide_conf)

        self.layer_slide_iou = QHBoxLayout()
        self.layer_slide_iou.setObjectName(u"layer_slide_iou")
        self.layer_slide_iou.setContentsMargins(35, -1, -1, -1)
        self.label_slide_iou = QLabel(self.centralwidget)
        self.label_slide_iou.setObjectName(u"label_slide_iou")
        self.label_slide_iou.setMinimumSize(QSize(60, 35))
        self.label_slide_iou.setMaximumSize(QSize(70, 16777215))
        self.label_slide_iou.setFont(font3)

        self.layer_slide_iou.addWidget(self.label_slide_iou)

        self.slider_iou = QSlider(self.centralwidget)
        self.slider_iou.setObjectName(u"slider_iou")
        self.slider_iou.setStyleSheet(u"color: rgb(159,168,218);")
        self.slider_iou.setValue(50)
        self.slider_iou.setOrientation(Qt.Horizontal)

        self.layer_slide_iou.addWidget(self.slider_iou)


        self.Layout_slide.addLayout(self.layer_slide_iou)


        self.dispSide.addLayout(self.Layout_slide)

        self.Layout_res = QHBoxLayout()
        self.Layout_res.setObjectName(u"Layout_res")
        self.Layout_res.setContentsMargins(40, -1, -1, -1)
        self.label_picTime = QLabel(self.centralwidget)
        self.label_picTime.setObjectName(u"label_picTime")
        self.label_picTime.setMinimumSize(QSize(30, 30))
        self.label_picTime.setMaximumSize(QSize(35, 35))
        self.label_picTime.setStyleSheet(u"border-image: url(:/images/icons/net_speed.png);")

        self.Layout_res.addWidget(self.label_picTime)

        self.label_useTime = QLabel(self.centralwidget)
        self.label_useTime.setObjectName(u"label_useTime")
        self.label_useTime.setMaximumSize(QSize(120, 16777215))
        self.label_useTime.setFont(font3)

        self.Layout_res.addWidget(self.label_useTime)

        self.label_time_result = QLabel(self.centralwidget)
        self.label_time_result.setObjectName(u"label_time_result")
        self.label_time_result.setMinimumSize(QSize(145, 0))
        self.label_time_result.setFont(font3)

        self.Layout_res.addWidget(self.label_time_result)

        self.label_picNumber = QLabel(self.centralwidget)
        self.label_picNumber.setObjectName(u"label_picNumber")
        self.label_picNumber.setMinimumSize(QSize(30, 35))
        self.label_picNumber.setMaximumSize(QSize(35, 35))
        self.label_picNumber.setStyleSheet(u"border-image: url(:/images/icons/count.png);")

        self.Layout_res.addWidget(self.label_picNumber)

        self.label_objNum = QLabel(self.centralwidget)
        self.label_objNum.setObjectName(u"label_objNum")
        self.label_objNum.setMinimumSize(QSize(120, 0))
        self.label_objNum.setMaximumSize(QSize(120, 16777215))
        self.label_objNum.setFont(font3)

        self.Layout_res.addWidget(self.label_objNum)

        self.label_numer_result = QLabel(self.centralwidget)
        self.label_numer_result.setObjectName(u"label_numer_result")
        font4 = QFont()
        font4.setFamilies([u"SimSun"])
        font4.setPointSize(14)
        self.label_numer_result.setFont(font4)
        self.label_numer_result.setStyleSheet(u"color: rgb(159,168,218);")

        self.Layout_res.addWidget(self.label_numer_result)


        self.dispSide.addLayout(self.Layout_res)

        self.label_display = QLabel(self.centralwidget)
        self.label_display.setObjectName(u"label_display")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_display.sizePolicy().hasHeightForWidth())
        self.label_display.setSizePolicy(sizePolicy1)
        self.label_display.setMinimumSize(QSize(569, 454))
        self.label_display.setMaximumSize(QSize(1152, 648))
        font5 = QFont()
        font5.setFamilies([u"\u6977\u4f53"])
        font5.setPointSize(16)
        self.label_display.setFont(font5)
        self.label_display.setLayoutDirection(Qt.LeftToRight)
        self.label_display.setStyleSheet(u"border-image: url(:/images/icons/love.jpg)")
        self.label_display.setAlignment(Qt.AlignCenter)

        self.dispSide.addWidget(self.label_display)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximumSize(QSize(16777215, 6))
        self.progressBar.setStyleSheet(u"")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)

        self.dispSide.addWidget(self.progressBar)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        font6 = QFont()
        font6.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font6.setPointSize(9)
        font6.setBold(False)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font6);
        __qtablewidgetitem.setBackground(QColor(0, 0, 0, 0));
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font6);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font6);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        font7 = QFont()
        font7.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font7.setPointSize(9)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font7);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font7);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.tableWidget.rowCount() < 6):
            self.tableWidget.setRowCount(6)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(0, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(0, 2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(1, 0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(1, 2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(2, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(2, 2, __qtablewidgetitem14)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy2)
        self.tableWidget.setMinimumSize(QSize(569, 150))
        self.tableWidget.setMaximumSize(QSize(1152, 180))
        font8 = QFont()
        font8.setFamilies([u"Microsoft YaHei UI"])
        font8.setPointSize(10)
        self.tableWidget.setFont(font8)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setRowCount(6)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)

        self.dispSide.addWidget(self.tableWidget)


        self.Layout_contain.addLayout(self.dispSide)

        self.stackPage = QStackedWidget(self.centralwidget)
        self.stackPage.setObjectName(u"stackPage")
        self.stackPage.setMaximumSize(QSize(400, 16777215))
        self.Page_result = QWidget()
        self.Page_result.setObjectName(u"Page_result")
        self.verticalLayout_2 = QVBoxLayout(self.Page_result)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_website = QLabel(self.Page_result)
        self.label_website.setObjectName(u"label_website")
        self.label_website.setMinimumSize(QSize(0, 30))
        font9 = QFont()
        font9.setFamilies([u"Times new roman"])
        font9.setPointSize(12)
        font9.setBold(False)
        font9.setItalic(False)
        self.label_website.setFont(font9)
        self.label_website.setStyleSheet(u"QLabel{font: 12pt \"Times new roman\";}")
        self.label_website.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_website)

        self.label_bar = QLabel(self.Page_result)
        self.label_bar.setObjectName(u"label_bar")
        self.label_bar.setMinimumSize(QSize(382, 300))
        self.label_bar.setMaximumSize(QSize(400, 300))
        self.label_bar.setStyleSheet(u"border-image: url(:/images/icons/love.jpg)")
        self.label_bar.setMargin(5)

        self.verticalLayout_2.addWidget(self.label_bar)

        self.label = QLabel(self.Page_result)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 20))
        self.label.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_2.addWidget(self.label)

        self.Layout_obj = QHBoxLayout()
        self.Layout_obj.setObjectName(u"Layout_obj")
        self.Layout_obj.setContentsMargins(-1, 0, 200, -1)
        self.label_picSelect = QLabel(self.Page_result)
        self.label_picSelect.setObjectName(u"label_picSelect")
        self.label_picSelect.setMinimumSize(QSize(30, 30))
        self.label_picSelect.setMaximumSize(QSize(35, 35))
        self.label_picSelect.setStyleSheet(u"border-image: url(:/images/icons/selection.png);")

        self.Layout_obj.addWidget(self.label_picSelect)

        self.comboBox_select = QComboBox(self.Page_result)
        self.comboBox_select.addItem("")
        self.comboBox_select.setObjectName(u"comboBox_select")
        self.comboBox_select.setMinimumSize(QSize(0, 24))
        self.comboBox_select.setMaximumSize(QSize(150, 28))
        font10 = QFont()
        font10.setFamilies([u"Consolas"])
        font10.setPointSize(12)
        font10.setBold(False)
        font10.setItalic(True)
        self.comboBox_select.setFont(font10)
        self.comboBox_select.setFocusPolicy(Qt.ClickFocus)
        self.comboBox_select.setIconSize(QSize(36, 36))

        self.Layout_obj.addWidget(self.comboBox_select)


        self.verticalLayout_2.addLayout(self.Layout_obj)

        self.Layout_cls = QHBoxLayout()
        self.Layout_cls.setObjectName(u"Layout_cls")
        self.label_picResult = QLabel(self.Page_result)
        self.label_picResult.setObjectName(u"label_picResult")
        self.label_picResult.setMinimumSize(QSize(35, 35))
        self.label_picResult.setMaximumSize(QSize(40, 40))
        self.label_picResult.setStyleSheet(u"border-image: url(:/images/icons/result.png);")

        self.Layout_cls.addWidget(self.label_picResult)

        self.label_class = QLabel(self.Page_result)
        self.label_class.setObjectName(u"label_class")
        self.label_class.setFont(font3)

        self.Layout_cls.addWidget(self.label_class)

        self.label_class_result = QLabel(self.Page_result)
        self.label_class_result.setObjectName(u"label_class_result")
        self.label_class_result.setFont(font4)
        self.label_class_result.setStyleSheet(u"color: rgb(159,168,218);")

        self.Layout_cls.addWidget(self.label_class_result)


        self.verticalLayout_2.addLayout(self.Layout_cls)

        self.Layout_conf = QHBoxLayout()
        self.Layout_conf.setObjectName(u"Layout_conf")
        self.label_picConf = QLabel(self.Page_result)
        self.label_picConf.setObjectName(u"label_picConf")
        self.label_picConf.setMinimumSize(QSize(35, 35))
        self.label_picConf.setMaximumSize(QSize(40, 40))
        self.label_picConf.setStyleSheet(u"border-image: url(:/images/icons/Score.png);")

        self.Layout_conf.addWidget(self.label_picConf)

        self.label_conf = QLabel(self.Page_result)
        self.label_conf.setObjectName(u"label_conf")
        self.label_conf.setFont(font3)

        self.Layout_conf.addWidget(self.label_conf)

        self.label_score_result = QLabel(self.Page_result)
        self.label_score_result.setObjectName(u"label_score_result")
        self.label_score_result.setFont(font4)
        self.label_score_result.setStyleSheet(u"color: rgb(159,168,218);")

        self.Layout_conf.addWidget(self.label_score_result)


        self.verticalLayout_2.addLayout(self.Layout_conf)

        self.Layout_loc = QHBoxLayout()
        self.Layout_loc.setObjectName(u"Layout_loc")
        self.label_picLocation = QLabel(self.Page_result)
        self.label_picLocation.setObjectName(u"label_picLocation")
        self.label_picLocation.setMinimumSize(QSize(35, 35))
        self.label_picLocation.setMaximumSize(QSize(40, 40))
        self.label_picLocation.setStyleSheet(u"border-image: url(:/images/icons/Ordinateur.png);")

        self.Layout_loc.addWidget(self.label_picLocation)

        self.label_location = QLabel(self.Page_result)
        self.label_location.setObjectName(u"label_location")
        self.label_location.setFont(font3)

        self.Layout_loc.addWidget(self.label_location)


        self.verticalLayout_2.addLayout(self.Layout_loc)

        self.Layout_xymin = QHBoxLayout()
        self.Layout_xymin.setObjectName(u"Layout_xymin")
        self.Layout_xymin.setContentsMargins(20, -1, -1, -1)
        self.label_xmin = QLabel(self.Page_result)
        self.label_xmin.setObjectName(u"label_xmin")
        self.label_xmin.setFont(font10)

        self.Layout_xymin.addWidget(self.label_xmin)

        self.label_xmin_result = QLabel(self.Page_result)
        self.label_xmin_result.setObjectName(u"label_xmin_result")
        font11 = QFont()
        font11.setFamilies([u"SimSun-ExtB"])
        font11.setPointSize(12)
        self.label_xmin_result.setFont(font11)

        self.Layout_xymin.addWidget(self.label_xmin_result)

        self.label_ymin = QLabel(self.Page_result)
        self.label_ymin.setObjectName(u"label_ymin")
        self.label_ymin.setFont(font10)

        self.Layout_xymin.addWidget(self.label_ymin)

        self.label_ymin_result = QLabel(self.Page_result)
        self.label_ymin_result.setObjectName(u"label_ymin_result")
        self.label_ymin_result.setFont(font11)

        self.Layout_xymin.addWidget(self.label_ymin_result)


        self.verticalLayout_2.addLayout(self.Layout_xymin)

        self.Layout_xymax = QHBoxLayout()
        self.Layout_xymax.setObjectName(u"Layout_xymax")
        self.Layout_xymax.setContentsMargins(20, -1, -1, -1)
        self.label_xmax = QLabel(self.Page_result)
        self.label_xmax.setObjectName(u"label_xmax")
        self.label_xmax.setFont(font10)

        self.Layout_xymax.addWidget(self.label_xmax)

        self.label_xmax_result = QLabel(self.Page_result)
        self.label_xmax_result.setObjectName(u"label_xmax_result")
        self.label_xmax_result.setFont(font11)

        self.Layout_xymax.addWidget(self.label_xmax_result)

        self.label_ymax = QLabel(self.Page_result)
        self.label_ymax.setObjectName(u"label_ymax")
        self.label_ymax.setFont(font10)

        self.Layout_xymax.addWidget(self.label_ymax)

        self.label_ymax_result = QLabel(self.Page_result)
        self.label_ymax_result.setObjectName(u"label_ymax_result")
        self.label_ymax_result.setFont(font11)

        self.Layout_xymax.addWidget(self.label_ymax_result)


        self.verticalLayout_2.addLayout(self.Layout_xymax)

        self.stackPage.addWidget(self.Page_result)
        self.Page_login = QWidget()
        self.Page_login.setObjectName(u"Page_login")
        self.pushButton_logout = QPushButton(self.Page_login)
        self.pushButton_logout.setObjectName(u"pushButton_logout")
        self.pushButton_logout.setGeometry(QRect(90, 428, 219, 43))
        self.pushButton_logout.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(26, 122, 244);\n"
"	border-radius:10px; \n"
"    border:1px;\n"
"	font:17px \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	color:rgba(255,255,255);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	border-color:rgba(255,255,255,30);\n"
"	background-color: rgb(0, 170, 255);\n"
"	border-style:inset;\n"
"	color:rgba(0,0,0,100);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(73, 154, 237);\n"
"	border-color:rgba(255,255,255,200);\n"
"	color:rgba(255,255,255);\n"
"}")
        self.label_loginPic = QLabel(self.Page_login)
        self.label_loginPic.setObjectName(u"label_loginPic")
        self.label_loginPic.setGeometry(QRect(160, 68, 85, 85))
        self.label_loginPic.setMinimumSize(QSize(85, 85))
        self.label_loginPic.setMaximumSize(QSize(85, 85))
        font12 = QFont()
        font12.setFamilies([u"Adobe \u9ed1\u4f53 Std R"])
        font12.setPointSize(18)
        font12.setBold(True)
        font12.setItalic(False)
        self.label_loginPic.setFont(font12)
        self.label_loginPic.setStyleSheet(u"border-image: url(:/images/icons/user.png);\n"
"background-color: transparent;\n"
"border-radius:40px;")
        self.label_loginPic.setAlignment(Qt.AlignCenter)
        self.pushButton_login = QPushButton(self.Page_login)
        self.pushButton_login.setObjectName(u"pushButton_login")
        self.pushButton_login.setGeometry(QRect(90, 360, 219, 43))
        self.pushButton_login.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(26, 122, 244);\n"
"	border-radius:10px; \n"
"    border:1px;\n"
"	font:17px \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	color:rgba(255,255,255);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	border-color:rgba(255,255,255,30);\n"
"	background-color: rgb(0, 170, 255);\n"
"	border-style:inset;\n"
"	color:rgba(0,0,0,100);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(73, 154, 237);\n"
"	border-color:rgba(255,255,255,200);\n"
"	color:rgba(255,255,255);\n"
"}")
        self.toolButton_loadLogo = QToolButton(self.Page_login)
        self.toolButton_loadLogo.setObjectName(u"toolButton_loadLogo")
        self.toolButton_loadLogo.setGeometry(QRect(188, 160, 25, 27))
        self.toolButton_loadLogo.setMaximumSize(QSize(45, 45))
        self.toolButton_loadLogo.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_loadLogo.setAutoFillBackground(False)
        icon10 = QIcon()
        icon10.addFile(u":/images/icons/gallery.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_loadLogo.setIcon(icon10)
        self.toolButton_loadLogo.setIconSize(QSize(50, 39))
        self.toolButton_loadLogo.setPopupMode(QToolButton.DelayedPopup)
        self.toolButton_loadLogo.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.toolButton_loadLogo.setAutoRaise(False)
        self.toolButton_loadLogo.setArrowType(Qt.NoArrow)
        self.label_info = QLabel(self.Page_login)
        self.label_info.setObjectName(u"label_info")
        self.label_info.setGeometry(QRect(8, 564, 377, 83))
        self.label_info.setMinimumSize(QSize(0, 30))
        self.label_info.setFont(font9)
        self.label_info.setStyleSheet(u"QLabel{font: 12pt \"Times new roman\";}")
        self.label_info.setAlignment(Qt.AlignCenter)
        self.label_pic_name = QLabel(self.Page_login)
        self.label_pic_name.setObjectName(u"label_pic_name")
        self.label_pic_name.setGeometry(QRect(114, 230, 25, 29))
        self.label_pic_name.setMaximumSize(QSize(85, 85))
        self.label_pic_name.setFont(font12)
        self.label_pic_name.setStyleSheet(u"border-image: url(:/images/icons/author.png);\n"
"background-color: transparent;\n"
"")
        self.label_pic_name.setAlignment(Qt.AlignCenter)
        self.label_person_name = QLabel(self.Page_login)
        self.label_person_name.setObjectName(u"label_person_name")
        self.label_person_name.setGeometry(QRect(142, 226, 161, 40))
        self.label_person_name.setMinimumSize(QSize(0, 30))
        font13 = QFont()
        font13.setFamilies([u"Times new roman"])
        font13.setPointSize(14)
        font13.setBold(False)
        font13.setItalic(False)
        self.label_person_name.setFont(font13)
        self.label_person_name.setStyleSheet(u"QLabel{font: 14pt \"Times new roman\";}")
        self.label_person_name.setAlignment(Qt.AlignCenter)
        self.pushButton_avatar = QPushButton(self.Page_login)
        self.pushButton_avatar.setObjectName(u"pushButton_avatar")
        self.pushButton_avatar.setGeometry(QRect(88, 290, 219, 43))
        self.pushButton_avatar.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(26, 122, 244);\n"
"	border-radius:10px; \n"
"    border:1px;\n"
"	font:17px \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	color:rgba(255,255,255);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	border-color:rgba(255,255,255,30);\n"
"	background-color: rgb(0, 170, 255);\n"
"	border-style:inset;\n"
"	color:rgba(0,0,0,100);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(73, 154, 237);\n"
"	border-color:rgba(255,255,255,200);\n"
"	color:rgba(255,255,255);\n"
"}")
        self.stackPage.addWidget(self.Page_login)

        self.Layout_contain.addWidget(self.stackPage)


        self.Layout_main.addLayout(self.Layout_contain)


        self.horizontalLayout.addLayout(self.Layout_main)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackPage.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Recognition v1.0", None))
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.actionGoogle_Translate.setText(QCoreApplication.translate("MainWindow", u"Google Translate", None))
        self.actionHTML_type.setText(QCoreApplication.translate("MainWindow", u"HTML type", None))
        self.actionsoftware_version.setText(QCoreApplication.translate("MainWindow", u"software version", None))
#if QT_CONFIG(tooltip)
        self.toolButton_saveing.setToolTip(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u7ed3\u679c", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_saveing.setText("")
#if QT_CONFIG(tooltip)
        self.toolButton_author.setToolTip(QCoreApplication.translate("MainWindow", u"\u5f00\u53d1\u4fe1\u606f", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_author.setText("")
#if QT_CONFIG(tooltip)
        self.toolButton_version.setToolTip(QCoreApplication.translate("MainWindow", u"\u7248\u672c\u4fe1\u606f", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_version.setText("")
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"\u57fa\u4e8eYOLOv8/v5\u7684\u624b\u52bf\u8bc6\u522b\u7cfb\u7edf", None))
#if QT_CONFIG(tooltip)
        self.toolButton_camera.setToolTip(QCoreApplication.translate("MainWindow", u"\u5f00\u542f\u6444\u50cf\u5934", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_camera.setText("")
        self.textEdit_camera.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'12pt \u534e\u4e3a\u4eff\u5b8b'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Adobe Devanagari';\">\u6444\u50cf\u5934\u672a\u5f00\u542f</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.toolButton_file.setToolTip(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u56fe\u7247", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_file.setText("")
        self.textEdit_image.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'12pt \u534e\u4e3a\u4eff\u5b8b'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Adobe Devanagari';\">\u9009\u62e9\u56fe\u7247\u6587\u4ef6</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.toolButton_model.setToolTip(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528\u9ed8\u8ba4\u6a21\u578b", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_model.setText("")
        self.textEdit_model.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'12pt \u534e\u4e3a\u4eff\u5b8b'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Adobe Devanagari';\">\u9009\u62e9\u6a21\u578b\u6587\u4ef6</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.toolButton_folder.setToolTip(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u56fe\u7247\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_folder.setText("")
        self.textEdit_imgFolder.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'12pt \u534e\u4e3a\u4eff\u5b8b'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Adobe Devanagari';\">\u9009\u62e9\u56fe\u7247\u6587\u4ef6\u5939</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.toolButton_video.setToolTip(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u89c6\u9891", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_video.setText("")
        self.textEdit_video.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'12pt \u534e\u4e3a\u4eff\u5b8b'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Adobe Devanagari';\">\u9009\u62e9\u89c6\u9891\u6587\u4ef6</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.loginTitle.setToolTip(QCoreApplication.translate("MainWindow", u"\u767b\u5f55\u4fe1\u606f", None))
#endif // QT_CONFIG(tooltip)
        self.loginTitle.setText("")
#if QT_CONFIG(tooltip)
        self.toolButton_menu.setToolTip(QCoreApplication.translate("MainWindow", u"\u5f39\u51fa\u663e\u793a", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_menu.setText("")
        self.pushButton_hide.setText(QCoreApplication.translate("MainWindow", u"\u9690\u85cf\u663e\u793a", None))
        self.label_slide_conf.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span >CONF\uff1a</span></p></body></html>", None))
        self.label_slide_iou.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>IOU\uff1a</p></body></html>", None))
        self.label_picTime.setText("")
        self.label_useTime.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span >\u7528\u65f6\uff1a</span></p></body></html>", None))
        self.label_time_result.setText(QCoreApplication.translate("MainWindow", u"0 s", None))
        self.label_picNumber.setText("")
        self.label_objNum.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u76ee\u6807\u6570\u76ee\uff1a</p></body></html>", None))
        self.label_numer_result.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_display.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u5e8f\u53f7", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u753b\u9762\u6807\u8bc6", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u679c", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u4f4d\u7f6e", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u7f6e\u4fe1\u5ea6", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"2", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label_website.setText(QCoreApplication.translate("MainWindow", u"\u676d\u7535\u5723\u5149\u673a2020\u7ea7\u5b8b\u8f69\u9038\u6bd5\u4e1a\u8bbe\u8ba1", None))
        self.label_bar.setText("")
        self.label.setText("")
        self.label_picSelect.setText("")
        self.comboBox_select.setItemText(0, QCoreApplication.translate("MainWindow", u"\u6240\u6709\u76ee\u6807", None))

        self.comboBox_select.setCurrentText(QCoreApplication.translate("MainWindow", u"\u6240\u6709\u76ee\u6807", None))
        self.label_picResult.setText("")
        self.label_class.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u7c7b\u522b\uff1a</p></body></html>", None))
        self.label_class_result.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_picConf.setText("")
        self.label_conf.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u7f6e\u4fe1\u5ea6\uff1a</p></body></html>", None))
        self.label_score_result.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_picLocation.setText("")
        self.label_location.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u4f4d \u7f6e\uff1a</p></body></html>", None))
        self.label_xmin.setText(QCoreApplication.translate("MainWindow", u"xmin: ", None))
        self.label_xmin_result.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_ymin.setText(QCoreApplication.translate("MainWindow", u"ymin: ", None))
        self.label_ymin_result.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_xmax.setText(QCoreApplication.translate("MainWindow", u"xmax: ", None))
        self.label_xmax_result.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_ymax.setText(QCoreApplication.translate("MainWindow", u"ymax: ", None))
        self.label_ymax_result.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_logout.setText(QCoreApplication.translate("MainWindow", u"\u6ce8\u9500\u8d26\u6237", None))
        self.label_loginPic.setText("")
        self.pushButton_login.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u65b0\u767b\u5f55", None))
#if QT_CONFIG(tooltip)
        self.toolButton_loadLogo.setToolTip(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u7ed3\u679c", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_loadLogo.setText("")
        self.label_info.setText(QCoreApplication.translate("MainWindow", u"HDU \n"
" ITMO", None))
        self.label_pic_name.setText("")
#if QT_CONFIG(tooltip)
        self.label_person_name.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>www.zhihu.com/people/sixuwuxian</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_person_name.setText(QCoreApplication.translate("MainWindow", u"\u5b8b\u8f69\u9038", None))
        self.pushButton_avatar.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u5934\u50cf", None))
    # retranslateUi

