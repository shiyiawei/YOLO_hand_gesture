# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginForm.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTabWidget, QToolButton, QWidget)
import RecSystem_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(749, 482)
        Dialog.setMinimumSize(QSize(749, 482))
        Dialog.setMaximumSize(QSize(749, 482))
        icon = QIcon()
        icon.addFile(u":/login/icons/bird-logo.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 747, 483))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.btn_minimize = QPushButton(self.frame)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setGeometry(QRect(666, 8, 35, 31))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy)
        self.btn_minimize.setMinimumSize(QSize(25, 25))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        icon1 = QIcon()
        icon1.addFile(u":/login/icons/minmax.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon1)
        self.label_movie = QLabel(self.frame)
        self.label_movie.setObjectName(u"label_movie")
        self.label_movie.setGeometry(QRect(30, 20, 301, 71))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_movie.sizePolicy().hasHeightForWidth())
        self.label_movie.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"\u6977\u4f53"])
        font.setPointSize(16)
        self.label_movie.setFont(font)
        self.label_movie.setLayoutDirection(Qt.LeftToRight)
        self.label_movie.setStyleSheet(u"QLabel{\n"
"border-image: url(:/login/icons/sign.png);\n"
"}")
        self.label_movie.setAlignment(Qt.AlignCenter)
        self.tabWidget = QTabWidget(self.frame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(326, 2, 417, 475))
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"\n"
"QTabWidget::pane{\n"
"min-width:70px;\n"
"min-height:25px;\n"
"border-top: 0px solid;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"font-size:10px;\n"
"min-width:70px;\n"
"\n"
"min-height:25px;\n"
"\n"
"color: black;\n"
"\n"
"font:12px \"Microsoft YaHei\";\n"
"\n"
"border: -1px solid;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QTabBar::tab:selected{\n"
"\n"
"min-width:70px;\n"
"\n"
"min-height:25px;\n"
"color: black;\n"
"\n"
"font:11px \"Microsoft YaHei\";\n"
"\n"
"border: 0px solid;\n"
"\n"
"border-bottom: 0px solid;\n"
"\n"
"border-color: #4796f0;\n"
"\n"
"}")
        self.tabWidget.setTabBarAutoHide(True)
        self.tab_login = QWidget()
        self.tab_login.setObjectName(u"tab_login")
        self.checkBox_remenber = QCheckBox(self.tab_login)
        self.checkBox_remenber.setObjectName(u"checkBox_remenber")
        self.checkBox_remenber.setGeometry(QRect(66, 272, 115, 35))
        self.checkBox_remenber.setStyleSheet(u"\n"
"QCheckBox{\n"
"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"color: rgb(100, 100, 100);\n"
"spacing: 5px;\n"
"background-color: transparent;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"width: 18px;\n"
"height: 18px;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"border-image: url(:/login/icons/check.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"border-image: url(:/login/icons/checked.png);\n"
"}\n"
" ")
        self.checkBox_remenber.setIconSize(QSize(18, 18))
        self.checkBox_remenber.setChecked(True)
        self.lineEdit_password = QLineEdit(self.tab_login)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setGeometry(QRect(100, 208, 261, 41))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(12)
        self.lineEdit_password.setFont(font1)
        self.label_log_passwordBack = QLabel(self.tab_login)
        self.label_log_passwordBack.setObjectName(u"label_log_passwordBack")
        self.label_log_passwordBack.setGeometry(QRect(52, 208, 319, 43))
        self.label_log_passwordBack.setStyleSheet(u"border-image: url(:/images/icons/logo1.png);")
        self.label_log_user = QLabel(self.tab_login)
        self.label_log_user.setObjectName(u"label_log_user")
        self.label_log_user.setGeometry(QRect(64, 146, 21, 21))
        self.label_log_user.setStyleSheet(u"border-image: url(:/login/icons/logo2.png);\n"
"background-color: transparent;")
        self.lineEdit_user_log = QLineEdit(self.tab_login)
        self.lineEdit_user_log.setObjectName(u"lineEdit_user_log")
        self.lineEdit_user_log.setGeometry(QRect(100, 136, 259, 41))
        font2 = QFont()
        font2.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        self.lineEdit_user_log.setFont(font2)
        self.toolButton_forgetCode = QToolButton(self.tab_login)
        self.toolButton_forgetCode.setObjectName(u"toolButton_forgetCode")
        self.toolButton_forgetCode.setGeometry(QRect(252, 272, 121, 33))
        self.toolButton_forgetCode.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_forgetCode.setIconSize(QSize(16, 16))
        self.label_log_password = QLabel(self.tab_login)
        self.label_log_password.setObjectName(u"label_log_password")
        self.label_log_password.setGeometry(QRect(64, 220, 21, 21))
        self.label_log_password.setStyleSheet(u"border-image: url(:/login/icons/logo3.png);\n"
"background-color: transparent;")
        self.pushButton_login = QPushButton(self.tab_login)
        self.pushButton_login.setObjectName(u"pushButton_login")
        self.pushButton_login.setGeometry(QRect(76, 338, 261, 43))
        self.pushButton_login.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(159,168,218);\n"
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
        self.label_pic = QLabel(self.tab_login)
        self.label_pic.setObjectName(u"label_pic")
        self.label_pic.setGeometry(QRect(166, 16, 85, 85))
        self.label_pic.setMinimumSize(QSize(85, 85))
        self.label_pic.setMaximumSize(QSize(85, 85))
        font3 = QFont()
        font3.setFamilies([u"Adobe \u9ed1\u4f53 Std R"])
        font3.setPointSize(18)
        font3.setBold(True)
        font3.setItalic(False)
        self.label_pic.setFont(font3)
        self.label_pic.setStyleSheet(u"border-image: url(:/login/icons/user.png);\n"
"background-color: transparent;\n"
"border-radius:40px;")
        self.label_pic.setAlignment(Qt.AlignCenter)
        self.label_log_userBack = QLabel(self.tab_login)
        self.label_log_userBack.setObjectName(u"label_log_userBack")
        self.label_log_userBack.setGeometry(QRect(52, 136, 319, 43))
        self.label_log_userBack.setStyleSheet(u"border-image: url(:/images/icons/logo1.png);")
        self.toolButton_go2reg = QToolButton(self.tab_login)
        self.toolButton_go2reg.setObjectName(u"toolButton_go2reg")
        self.toolButton_go2reg.setGeometry(QRect(30, 390, 121, 41))
        self.toolButton_go2reg.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_log_info = QLabel(self.tab_login)
        self.label_log_info.setObjectName(u"label_log_info")
        self.label_log_info.setGeometry(QRect(162, 402, 179, 39))
        self.label_log_info.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(255, 0, 127);\n"
"font: 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.tabWidget.addTab(self.tab_login, "")
        self.label_log_passwordBack.raise_()
        self.label_log_userBack.raise_()
        self.checkBox_remenber.raise_()
        self.lineEdit_password.raise_()
        self.label_log_user.raise_()
        self.lineEdit_user_log.raise_()
        self.toolButton_forgetCode.raise_()
        self.label_log_password.raise_()
        self.pushButton_login.raise_()
        self.label_pic.raise_()
        self.toolButton_go2reg.raise_()
        self.label_log_info.raise_()
        self.tab_reg = QWidget()
        self.tab_reg.setObjectName(u"tab_reg")
        self.lineEdit_user_reg = QLineEdit(self.tab_reg)
        self.lineEdit_user_reg.setObjectName(u"lineEdit_user_reg")
        self.lineEdit_user_reg.setGeometry(QRect(100, 122, 259, 41))
        self.lineEdit_user_reg.setFont(font2)
        self.label_reg_passwordBack = QLabel(self.tab_reg)
        self.label_reg_passwordBack.setObjectName(u"label_reg_passwordBack")
        self.label_reg_passwordBack.setGeometry(QRect(52, 192, 319, 43))
        self.label_reg_passwordBack.setStyleSheet(u"border-image: url(:/login/icons/logo1.png);")
        self.label_reg_user = QLabel(self.tab_reg)
        self.label_reg_user.setObjectName(u"label_reg_user")
        self.label_reg_user.setGeometry(QRect(64, 132, 21, 21))
        self.label_reg_user.setStyleSheet(u"border-image: url(:/login/icons/logo2.png);\n"
"background-color: transparent;")
        self.lineEdit_password_reg = QLineEdit(self.tab_reg)
        self.lineEdit_password_reg.setObjectName(u"lineEdit_password_reg")
        self.lineEdit_password_reg.setGeometry(QRect(100, 192, 261, 41))
        self.lineEdit_password_reg.setFont(font1)
        self.label_pic_reg = QLabel(self.tab_reg)
        self.label_pic_reg.setObjectName(u"label_pic_reg")
        self.label_pic_reg.setGeometry(QRect(166, 10, 85, 85))
        self.label_pic_reg.setMinimumSize(QSize(85, 85))
        self.label_pic_reg.setMaximumSize(QSize(85, 85))
        self.label_pic_reg.setFont(font3)
        self.label_pic_reg.setStyleSheet(u"border-image: url(:/login/icons/user.png);\n"
"background-color: transparent;\n"
"border-radius:40px;")
        self.label_pic_reg.setAlignment(Qt.AlignCenter)
        self.toolButton_go2login = QToolButton(self.tab_reg)
        self.toolButton_go2login.setObjectName(u"toolButton_go2login")
        self.toolButton_go2login.setGeometry(QRect(10, 380, 119, 39))
        self.toolButton_go2login.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_reg_password = QLabel(self.tab_reg)
        self.label_reg_password.setObjectName(u"label_reg_password")
        self.label_reg_password.setGeometry(QRect(64, 204, 21, 21))
        self.label_reg_password.setStyleSheet(u"border-image: url(:/login/icons/logo3.png);\n"
"background-color: transparent;")
        self.label_reg_userBack = QLabel(self.tab_reg)
        self.label_reg_userBack.setObjectName(u"label_reg_userBack")
        self.label_reg_userBack.setGeometry(QRect(52, 122, 319, 43))
        self.label_reg_userBack.setStyleSheet(u"border-image: url(:/login/icons/logo1.png);")
        self.pushButton_reg = QPushButton(self.tab_reg)
        self.pushButton_reg.setObjectName(u"pushButton_reg")
        self.pushButton_reg.setGeometry(QRect(76, 340, 261, 43))
        self.pushButton_reg.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(159,168,218);\n"
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
        self.label_reg_vercodeBack = QLabel(self.tab_reg)
        self.label_reg_vercodeBack.setObjectName(u"label_reg_vercodeBack")
        self.label_reg_vercodeBack.setGeometry(QRect(52, 262, 223, 43))
        self.label_reg_vercodeBack.setStyleSheet(u"border-image: url(:/login/icons/logo1.png);")
        self.label_reg_vercode = QLabel(self.tab_reg)
        self.label_reg_vercode.setObjectName(u"label_reg_vercode")
        self.label_reg_vercode.setGeometry(QRect(64, 272, 21, 23))
        self.label_reg_vercode.setStyleSheet(u"border-image: url(:/login/icons/logo4.png);\n"
"background-color: transparent;")
        self.lineEdit_code_reg = QLineEdit(self.tab_reg)
        self.lineEdit_code_reg.setObjectName(u"lineEdit_code_reg")
        self.lineEdit_code_reg.setGeometry(QRect(100, 262, 159, 41))
        self.lineEdit_code_reg.setFont(font1)
        self.toolButton_verCode = QToolButton(self.tab_reg)
        self.toolButton_verCode.setObjectName(u"toolButton_verCode")
        self.toolButton_verCode.setGeometry(QRect(282, 262, 89, 43))
        sizePolicy1.setHeightForWidth(self.toolButton_verCode.sizePolicy().hasHeightForWidth())
        self.toolButton_verCode.setSizePolicy(sizePolicy1)
        self.toolButton_verCode.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/login/icons/captcha_1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_verCode.setIcon(icon2)
        self.toolButton_verCode.setIconSize(QSize(89, 43))
        self.label_reg_info = QLabel(self.tab_reg)
        self.label_reg_info.setObjectName(u"label_reg_info")
        self.label_reg_info.setGeometry(QRect(158, 404, 179, 39))
        self.label_reg_info.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(255, 0, 127);\n"
"font: 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.toolButton_loadLogo = QToolButton(self.tab_reg)
        self.toolButton_loadLogo.setObjectName(u"toolButton_loadLogo")
        self.toolButton_loadLogo.setGeometry(QRect(272, 40, 35, 37))
        self.toolButton_loadLogo.setMaximumSize(QSize(45, 45))
        self.toolButton_loadLogo.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_loadLogo.setAutoFillBackground(False)
        icon3 = QIcon()
        icon3.addFile(u":/images/icons/gallery.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_loadLogo.setIcon(icon3)
        self.toolButton_loadLogo.setIconSize(QSize(30, 30))
        self.toolButton_loadLogo.setPopupMode(QToolButton.DelayedPopup)
        self.toolButton_loadLogo.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.toolButton_loadLogo.setAutoRaise(False)
        self.toolButton_loadLogo.setArrowType(Qt.NoArrow)
        self.tabWidget.addTab(self.tab_reg, "")
        self.label_reg_userBack.raise_()
        self.lineEdit_user_reg.raise_()
        self.label_reg_passwordBack.raise_()
        self.label_reg_user.raise_()
        self.lineEdit_password_reg.raise_()
        self.label_pic_reg.raise_()
        self.toolButton_go2login.raise_()
        self.label_reg_password.raise_()
        self.pushButton_reg.raise_()
        self.label_reg_vercodeBack.raise_()
        self.label_reg_vercode.raise_()
        self.lineEdit_code_reg.raise_()
        self.toolButton_verCode.raise_()
        self.label_reg_info.raise_()
        self.toolButton_loadLogo.raise_()
        self.btn_close = QPushButton(self.frame)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(704, 8, 33, 31))
        sizePolicy.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy)
        self.btn_close.setMinimumSize(QSize(25, 25))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        icon4 = QIcon()
        icon4.addFile(u":/login/icons/extractLeft.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon4)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 10, 151, 20))
        self.label.setStyleSheet(u"border-image: url(:/images/icons/motto.png)")
        self.label_back = QLabel(self.frame)
        self.label_back.setObjectName(u"label_back")
        self.label_back.setGeometry(QRect(20, 90, 321, 381))
        self.label_back.setStyleSheet(u"border-image:url(:/login/icons/login.jpg)")
        self.tabWidget.raise_()
        self.btn_minimize.raise_()
        self.label_movie.raise_()
        self.btn_close.raise_()
        self.label.raise_()
        self.label_back.raise_()

        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("Dialog", u"\u6700\u5c0f\u5316", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.label_movie.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>\u601d\u7eea\u65e0\u9650</p><p>CSDN\uff1a<a href=\"htps:wuxian.blog.csdn.net\"><span style=\" text-decoration: underline; color:#0000ff;\">wuxian.blog.csdn.net</span></a></p><p>B\u7ad9\uff1a<a href=\"https://space.bilibili.com/456667721\"><span style=\" text-decoration: underline; color:#0000ff;\">\u601d\u7eea\u4ea6\u65e0\u9650</span></a></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_movie.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.checkBox_remenber.setText(QCoreApplication.translate("Dialog", u"\u8bb0\u4f4f\u5bc6\u7801", None))
        self.lineEdit_password.setText("")
        self.label_log_passwordBack.setText("")
        self.label_log_user.setText("")
        self.lineEdit_user_log.setText("")
        self.toolButton_forgetCode.setText(QCoreApplication.translate("Dialog", u"\u5fd8\u8bb0\u5bc6\u7801", None))
        self.label_log_password.setText("")
        self.pushButton_login.setText(QCoreApplication.translate("Dialog", u"\u767b \u5f55", None))
        self.label_pic.setText("")
        self.label_log_userBack.setText("")
        self.toolButton_go2reg.setText(QCoreApplication.translate("Dialog", u"\u6ce8\u518c\u8d26\u53f7", None))
        self.label_log_info.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_login), "")
        self.lineEdit_user_reg.setText("")
        self.label_reg_passwordBack.setText("")
        self.label_reg_user.setText("")
        self.lineEdit_password_reg.setText("")
        self.label_pic_reg.setText("")
        self.toolButton_go2login.setText(QCoreApplication.translate("Dialog", u"\u524d\u5f80\u767b\u5f55", None))
        self.label_reg_password.setText("")
        self.label_reg_userBack.setText("")
        self.pushButton_reg.setText(QCoreApplication.translate("Dialog", u"\u6ce8 \u518c", None))
        self.label_reg_vercodeBack.setText("")
        self.label_reg_vercode.setText("")
        self.lineEdit_code_reg.setText("")
        self.toolButton_verCode.setText("")
        self.label_reg_info.setText("")
#if QT_CONFIG(tooltip)
        self.toolButton_loadLogo.setToolTip(QCoreApplication.translate("Dialog", u"\u4fee\u6539\u5934\u50cf", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_loadLogo.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_reg), "")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("Dialog", u"\u5173\u95ed", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label.setText("")
        self.label_back.setText("")
    # retranslateUi

