import time

from QtFusion.styles import loadYamlSettings, loadQssStyles
from QtFusion.path import get_script_dir
from QtFusion.manager import UserManager
from QtFusion.widgets import QLoginDialog
from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtGui import QMovie
from PySide6.QtWidgets import QLineEdit, QFileDialog

from LoginForm import Ui_Dialog


class LoginDialog(QLoginDialog, Ui_Dialog):  # 定义一个名为LoginDialog的类，它继承自FLoginDialog和Ui_Dialog

    def __init__(self, parent=None, *args, **kwargs):  # 定义类的初始化函数，接受可变数量的参数和关键字参数
        super(LoginDialog, self).__init__(*args, **kwargs)  # 调用父类的初始化函数
        self.mainWindow = parent  # 将传入的parent参数赋值给self.mainWindow，这通常是父窗口的引用
        self.ver_code = ""  # 初始化验证码为空字符串
        self.avatar = ""  # 初始化头像为空字符串
        self.user_manager = UserManager("UserDatabase.db")  # 创建一个UserManager对象，用于管理用户数据库

        self.setupUi(self)  # 设置用户界面
        self.setUiStyle(windowFlag=True, transBackFlag=True)  # 设置用户界面的样式

        # 设置Tab键的顺序，即用户按Tab键时，焦点会按照这个顺序移动
        self.set_tab_order(self.lineEdit_user_log, self.lineEdit_password, self.pushButton_login)
        self.set_tab_order(self.lineEdit_user_reg, self.lineEdit_password_reg, self.lineEdit_code_reg,
                           self.pushButton_reg)
        self.setSlots()  # 设置槽函数，即设置各个按钮的点击事件对应的函数
        self.yaml_file = "./themes/Settings_login.yaml"  # 设置登录界面的背景或文字

        # 加载YAML设置和QSS样式表
        self.loadYamlSettings(yaml_file=self.yaml_file, base_path=get_script_dir())  # 设置图标背景或文字，使用当前文件夹为基本路径
        self.loadStyleSheet(qssFilePath="themes/login_text_black.qss")  # 设置样式表
        self.generate_code()  # 生成验证码

    def setSlots(self):  # 定义setSlots函数，用于设置各个按钮的点击事件对应的函数
        self.pushButton_reg.clicked.connect(self.do_reg)  # 当注册按钮被点击时，调用self.do_reg函数
        self.pushButton_login.clicked.connect(self.do_login)  # 当登录按钮被点击时，调用self.do_login函数
        self.toolButton_loadLogo.clicked.connect(self.do_avatar)  # 当加载头像按钮被点击时，调用self.do_avatar函数
        self.toolButton_forgetCode.clicked.connect(self.do_forget)  # 当忘记密码按钮被点击时，调用self.do_forget函数
        self.toolButton_verCode.clicked.connect(self.generate_code)  # 当验证码按钮被点击时，调用self.generate_code函数
        self.btn_close.clicked.connect(self.close)  # 当关闭按钮被点击时，关闭窗口
        self.btn_minimize.clicked.connect(self.minButton)  # 当最小化按钮被点击时，最小化窗口
        self.toolButton_go2reg.clicked.connect(self.go2reg)  # 当转到注册按钮被点击时，调用self.go2reg函数
        self.toolButton_go2login.clicked.connect(self.go2log)  # 当转到登录按钮被点击时，调用self.go2log函数

    def setUiStyle(self, windowFlag=False, transBackFlag=False):  # 定义setUiStyle函数，用于设置用户界面的样式
        """
        Function: Setting the state of UI controls, author: SXY,
        :param windowFlag:
        :param transBackFlag:
        :return:
        """
        if windowFlag:
            self.setWindowFlags(Qt.FramelessWindowHint)  # 如果windowFlag为True，设置窗口为无边框样式
        if transBackFlag:
            self.setAttribute(Qt.WA_TranslucentBackground)  # 如果transBackFlag为True，设置窗口背景为透明

        # self.gif_movie()  # 设置动画
        self.lineEdit_password.setEchoMode(QLineEdit.Password)  # 设置密码输入框的显示方式为密码模式
        self.lineEdit_password_reg.setEchoMode(QLineEdit.Password)  # 设置注册密码输入框的显示方式为密码模式
        self.lineEdit_user_log.setMaxLength(10)  # 设置登录用户名输入框的最大输入长度为10
        self.lineEdit_user_reg.setMaxLength(10)  # 设置注册用户名输入框的最大输入长度为10
        self.lineEdit_password.setMaxLength(12)  # 设置登录密码输入框的最大输入长度为12
        self.lineEdit_password_reg.setMaxLength(12)  # 设置注册密码输入框的最大输入长度为12

        # 设置各个输入框的占位符文本
        self.lineEdit_user_log.setPlaceholderText("用户名")
        self.lineEdit_password.setPlaceholderText("密码")
        self.lineEdit_user_reg.setPlaceholderText("用户名")
        self.lineEdit_password_reg.setPlaceholderText("密码")
        self.lineEdit_code_reg.setPlaceholderText("验证码")

    def generate_code(self):  # 定义generate_code函数，用于生成验证码
        # 调用generate_random_code函数生成验证码，并将验证码显示在toolButton_verCode控件上
        self.generate_random_code(widget=self.toolButton_verCode)

    def do_forget(self):  # 定义do_forget函数，用于处理用户点击忘记密码后的操作
        # 清空所有的输入框和提示标签
        self.lineEdit_user_log.clear()
        self.lineEdit_password.clear()
        self.lineEdit_user_reg.clear()
        self.lineEdit_password_reg.clear()
        self.lineEdit_code_reg.clear()
        self.label_reg_info.clear()
        self.label_log_info.clear()

        self.loadYamlSettings(yaml_file=self.yaml_file, base_path=get_script_dir())  # 重新加载YAML设置，使用当前文件夹为基础路径
        self.generate_code()  # 生成新的验证码

        # 设置标签页的可见性，并切换到注册标签页
        self.tabWidget.setTabVisible(0, False)
        self.tabWidget.setTabVisible(1, True)
        self.tabWidget.setCurrentIndex(1)

        self.pushButton_reg.setText("修改密码")  # 将注册按钮的文本改为"修改密码"
        self.toolButton_loadLogo.setEnabled(False)  # 禁用加载头像按钮

    def do_avatar(self):  # 定义do_avatar函数，用于处理用户点击加载头像按钮后的操作
        name_edit = self.lineEdit_user_reg.text()  # 获取注册用户名输入框的文本

        # 使用文件选择对话框选择图片
        file_choose, filetype = QFileDialog.getOpenFileName(
            self, "选取图片文件",
            "./",  # 起始路径
            "图片(*.jpg;*.jpeg;*.png)")  # 文件类型

        reply = self.user_manager.verify_avatar(file_choose)  # 验证选择的头像文件
        if reply == -1:  # 如果文件不存在，显示提示信息
            self.label_reg_info.setText("文件不存在")
        elif reply == -2:  # 如果读取头像失败，显示提示信息
            self.label_reg_info.setText("读取头像失败")
        elif reply == 0:  # 如果头像文件有效，显示提示信息，并将头像文件的路径保存到self.avatar中
            self.label_reg_info.setText("有效头像文件")
            self.avatar = file_choose
            self.label_pic_reg.setStyleSheet(f"QLabel {{ border-image: url({file_choose}) }}")  # 将头像显示在label_pic_reg控件上

    def do_login(self):  # 定义do_login函数，用于处理用户点击登录按钮后的操作
        name_edit = self.lineEdit_user_log.text()  # 获取登录用户名输入框的文本
        pwd_edit = self.lineEdit_password.text()  # 获取登录密码输入框的文本

        if name_edit != "" and pwd_edit != "":  # 如果用户名和密码都不为空
            if self.pushButton_login.text() == "登 录":  # 如果登录按钮的文本是"登 录"
                # 尝试验证用户名和密码
                reply = self.user_manager.verify_login(name_edit, pwd_edit)
                if reply == -2:  # 如果密码不正确，显示提示信息
                    self.label_log_info.setText("密码不正确")
                elif reply == -1:  # 如果用户未注册，显示提示信息
                    self.label_log_info.setText("用户未注册")
                elif reply == 0:  # 如果用户名和密码都正确
                    # 获取头像
                    avatar = self.user_manager.get_avatar(name_edit)
                    self.label_pic.setStyleSheet(f"QLabel {{ border-image: url({avatar}) }}")  # 将头像显示在label_pic控件上
                    self.label_log_info.setText("正在登录...")  # 显示正在登录的提示信息
                    QtWidgets.QApplication.processEvents()  # 处理所有事件，以更新界面
                    time.sleep(3)  # 等待3秒
                    self.close()  # 关闭登录对话框

                    # 设置主窗口的登录状态
                    self.mainWindow.init_login_info(name_edit, avatar)

            elif self.pushButton_login.text() == "注销账户":  # 如果登录按钮的文本是"注销账户"
                reply = self.user_manager.delete_user(name_edit, pwd_edit)  # 尝试注销用户
                if reply == -2:  # 如果密码不正确，显示提示信息
                    self.label_log_info.setText("密码不正确")
                elif reply == -1:  # 如果用户名不存在，显示提示信息
                    self.label_log_info.setText("用户名不存在")
                elif reply == 0:  # 如果用户名和密码都正确，用户成功注销
                    self.label_log_info.setText("账户已成功删除")
                    QtWidgets.QApplication.processEvents()  # 处理所有事件，以更新界面
                    time.sleep(3)  # 等待3秒
                    self.close()  # 关闭登录对话框
        else:  # 如果用户名或密码为空，显示提示信息
            self.label_log_info.setText("信息填写不全")

    def do_reg(self):  # 定义do_reg函数，用于处理用户点击注册按钮后的操作
        name_edit = self.lineEdit_user_reg.text()  # 获取注册用户名输入框的文本
        pwd_edit = self.lineEdit_password_reg.text()  # 获取注册密码输入框的文本
        ver_edit = self.lineEdit_code_reg.text()  # 获取验证码输入框的文本

        if name_edit != "" and pwd_edit != "" and ver_edit != "":  # 如果用户名、密码和验证码都不为空
            if ver_edit.lower() == self.ver_code.lower():  # 如果输入的验证码（忽略大小写）与生成的验证码一致
                if self.pushButton_reg.text() == "注 册":  # 如果注册按钮的文本是"注 册"
                    # 调用数据库接口尝试注册
                    reply = self.user_manager.register(name_edit, pwd_edit, self.avatar)
                    if reply == 0:  # 如果注册成功，显示提示信息
                        self.label_reg_info.setText("注册成功")
                    elif reply == -1:  # 如果用户已被注册过，显示提示信息
                        self.label_reg_info.setText("该用户已被注册过")
                    elif reply == -2:  # 如果密码长度过短，显示提示信息
                        self.label_reg_info.setText("密码长度过短")
                    elif reply == -3:  # 如果没有选择头像文件，显示提示信息
                        self.label_reg_info.setText("请选择头像文件")

                elif self.pushButton_reg.text() == "修改密码":  # 如果注册按钮的文本是"修改密码"
                    reply = self.user_manager.change_password(name_edit, pwd_edit)  # 尝试修改密码
                    if reply == 0:  # 如果修改密码成功，显示提示信息
                        self.label_reg_info.setText("修改密码成功")
                        avatar = self.user_manager.get_avatar(name_edit)  # 获取头像
                        # 将头像显示在label_pic_reg控件上
                        self.label_pic_reg.setStyleSheet(f"QLabel {{ border-image: url({avatar}) }}")
                    elif reply == -1:  # 如果用户名不存在，显示提示信息
                        self.label_reg_info.setText("用户名不存在")
                    elif reply == -2:  # 如果密码长度过短，显示提示信息
                        self.label_reg_info.setText("密码长度过短")

                elif self.pushButton_reg.text() == "修改头像":  # 如果注册按钮的文本是"修改头像"
                    # 获取
                    reply = self.user_manager.change_avatar(name_edit, pwd_edit, self.avatar)  # 尝试修改头像
                    if reply == 0:  # 如果修改头像成功，显示提示信息
                        self.label_reg_info.setText("修改头像成功")
                        self.mainWindow.init_reg_info(self.avatar, name_edit)  # 设置主窗口的注册信息
                        self.toolButton_go2login.setEnabled(True)  # 启用转到登录按钮
                    elif reply == -1:  # 如果用户名不存在，显示提示信息
                        self.label_reg_info.setText("用户名不存在")
                    elif reply == -2:  # 如果密码不正确，显示提示信息
                        self.label_reg_info.setText("密码不正确")
                    elif reply == -3:  # 如果没有选择头像文件，显示提示信息
                        self.label_reg_info.setText("请选择头像文件")
            else:  # 如果验证码错误，显示提示信息
                self.label_reg_info.setText("验证码错误")
        else:  # 如果用户名、密码或验证码为空，显示提示信息
            self.label_reg_info.setText("填写信息不全")

    def show_dialog(self):  # 定义show_dialog函数，用于显示登录对话框
        self.show()  # 显示对话框

    def minButton(self):  # 定义minButton函数，用于最小化对话框
        self.showMinimized()  # 最小化对话框

    def go2reg(self):  # 定义go2reg函数，用于切换到注册界面
        # 清空所有的输入框和提示标签
        self.lineEdit_user_log.clear()
        self.lineEdit_password.clear()
        self.lineEdit_user_reg.clear()
        self.lineEdit_password_reg.clear()
        self.lineEdit_code_reg.clear()
        self.label_reg_info.clear()
        self.label_log_info.clear()

        self.loadYamlSettings(yaml_file=self.yaml_file, base_path=get_script_dir())  # 重新加载YAML设置，使用当前文件夹为基础路径
        self.generate_code()  # 生成新的验证码

        # 设置标签页的可见性，并切换到注册标签页
        self.tabWidget.setTabVisible(0, False)
        self.tabWidget.setTabVisible(1, True)
        self.tabWidget.setCurrentIndex(1)

        self.pushButton_reg.setText("注 册")  # 将注册按钮的文本改为"注 册"
        self.toolButton_loadLogo.setEnabled(True)  # 启用加载头像按钮

    def go2log(self):  # 定义go2log函数，用于切换到登录界面
        # 清空所有的输入框和提示标签
        self.lineEdit_user_log.clear()
        self.lineEdit_password.clear()
        self.lineEdit_user_reg.clear()
        self.lineEdit_password_reg.clear()
        self.lineEdit_code_reg.clear()
        self.label_reg_info.clear()
        self.label_log_info.clear()

        self.loadYamlSettings(yaml_file=self.yaml_file, base_path=get_script_dir())  # 重新加载YAML设置，使用当前文件夹为基础路径
        self.generate_code()  # 生成新的验证码

        # 设置标签页的可见性，并切换到登录标签页
        self.tabWidget.setTabVisible(0, True)
        self.tabWidget.setTabVisible(1, False)
        self.tabWidget.setCurrentIndex(0)

    def setConfig(self):  # 定义setConfig函数，用于设置配置，但函数体为空，可能在子类中被重写
        pass

    def gif_movie(self):  # 定义gif_movie函数，用于设置界面动画
        gif = QMovie(':/login/icons/person1.gif')  # 创建QMovie对象，加载GIF动画文件
        self.label_movie.setMovie(gif)  # 将GIF动画设置到label_movie标签上
        self.label_movie.setScaledContents(True)  # 设置label_movie标签的内容自动缩放以填充可用空间
        gif.start()  # 开始播放GIF动画
