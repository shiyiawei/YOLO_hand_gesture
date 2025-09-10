# -*- coding: utf-8 -*-
from QtFusion.widgets import moveCenter
from System_noLogin import RecMainWindow
from LoginWindow import LoginDialog


class RecMainWindow_login(RecMainWindow):
    def __init__(self, parent=None, *args, **kwargs):  # 定义类的初始化函数，接收任意数量的位置参数和关键字参数
        super(RecMainWindow_login, self).__init__(*args, **kwargs)  # 调用父类的初始化函数

        self.pass_flag = False  # 初始化通过标志为False
        self.login = LoginDialog(self)  # 创建登录对话框实例

    def showTime(self):
        # 如果没有通过验证，则显示登录对话框，否则显示主窗口
        if not self.pass_flag:
            self.login.show()
        else:
            self.show()

    def slot_init(self):
        """
        初始化所有的信号和槽连接，包括各种处理器的信号和槽，以及各种按钮的点击事件的信号和槽。
        """
        super(RecMainWindow_login, self).slot_init()
        # 连接登录注册相关的信号和槽
        self.loginTitle.clicked.connect(self.toggle_login)  # 当点击登录标题时，调用toggle_login函数进行处理
        self.pushButton_avatar.clicked.connect(self.toggle_reset_avatar)  # 当点击头像按钮时，调用toggle_reset_avatar函数进行处理
        self.pushButton_login.clicked.connect(self.toggle_reset_login)  # 当点击登录按钮时，调用toggle_reset_login函数进行处理
        self.pushButton_logout.clicked.connect(self.toggle_reset_logout)  # 当点击注销按钮时，调用toggle_reset_logout函数进行处理

    def toggle_login(self):
        """
        切换登录页面。当点击登录标题时，如果当前是第一个页面，则切换到第二个页面；如果当前不是第一个页面，则切换到第一个页面。
        """
        current_index = self.stackPage.currentIndex()  # 获取当前堆栈页面的索引
        if current_index == 0:  # 如果当前索引为0，说明当前是第一个页面
            self.stackPage.setCurrentIndex(1)  # 切换到第二个页面
        else:  # 如果当前索引不为0，说明当前不是第一个页面
            self.stackPage.setCurrentIndex(0)  # 切换到第一个页面

    def reset_user(self, logout=False):
        """
        重置用户信息，包括用户名和用户头像。如果logout参数为True，则会弹出登录窗口。
        """
        # 设置默认的用户名和用户头像
        self.user_name = "sxy_hdu"
        self.user_avatar = ":/default_icons/default_avatar.png"

        # 更新登录标题和登录图片的样式
        self.loginTitle.setStyleSheet(f"""QToolButton {{ 
                                                            border-image: url({self.user_avatar});
                                                            background-color: transparent;
                                                            border-radius:5px;}}
                                                         QToolButton::hover{{
                                                            border:2px;
                                                         }}
                                                         QToolButton::pressed{{
                                                            border:1px;
                                                         }}
                                                         """)
        self.label_loginPic.setStyleSheet(f"QLabel {{ border-image: url({self.user_avatar}) ;"
                                          f"background-color: transparent;"
                                          f"border-radius:40px;}}")
        self.label_person_name.setText("未登录")  # 设置用户名标签的文本为"未登录"

        # 创建登录窗口
        self.login = LoginDialog(self)
        moveCenter(self, self.login)

        if logout:
            # 如果logout为True，设置登录按钮的文本为"注销账户"，并禁用"注册"和"忘记密码"按钮
            self.login.pushButton_login.setText("注销账户")
            self.login.tabWidget.setCurrentIndex(0)
            self.login.toolButton_go2reg.setEnabled(False)
            self.login.toolButton_forgetCode.setEnabled(False)

        self.login.exec_()  # 执行登录窗口

    def init_login_info(self, name_edit, avatar):
        """
        初始化登录信息，包括用户名和用户头像，并更新主窗口的状态。
        """
        # 设置用户名和用户头像
        self.user_name = name_edit
        self.user_avatar = avatar

        # 更新登录标题和登录图片的样式
        self.loginTitle.setStyleSheet(f"""QToolButton {{ 
                                                            border-image: url({avatar});
                                                            background-color: transparent;
                                                            border-radius:5px;}}
                                                         QToolButton::hover{{
                                                            border:2px;
                                                         }}
                                                         QToolButton::pressed{{
                                                            border:1px;
                                                         }}
                                                         """)
        self.label_loginPic.setStyleSheet(f"QLabel {{ border-image: url({avatar}) ;"
                                          f"background-color: transparent;"
                                          f"border-radius:40px;}}")
        self.label_person_name.setText(name_edit)  # 设置用户名标签的文本为用户名
        self.set_buttons_enabled(True)  # 启用按钮
        self.show()  # 显示主窗口

    def init_reg_info(self, avatar, name_edit):
        """
        初始化注册信息，包括用户名和用户头像，并更新主窗口的状态。
        """
        # 更新登录标题和登录图片的样式
        self.loginTitle.setStyleSheet(f"""QToolButton {{ 
                                                border-image: url({avatar});
                                                background-color: transparent;
                                                border-radius:5px;}}
                                             QToolButton::hover{{
                                                border:2px;
                                             }}
                                             QToolButton::pressed{{
                                                border:1px;
                                             }}
                                         """)
        self.label_loginPic.setStyleSheet(f"QLabel {{ border-image: url({avatar}) ;"
                                          f"background-color: transparent;"
                                          f"border-radius:40px;}}")
        self.label_person_name.setText(name_edit)  # 设置用户名标签的文本为用户名

    def toggle_reset_login(self):
        """
        重置登录状态，并禁用按钮。
        """
        self.set_buttons_enabled(False)  # 禁用按钮
        self.reset_user()  # 重置用户信息

    def toggle_reset_logout(self):
        """
        注销用户，并禁用按钮。
        """
        self.set_buttons_enabled(False)  # 禁用按钮
        self.reset_user(logout=True)  # 重置用户信息，并弹出登录窗口

    def toggle_reset_avatar(self):
        """
        修改用户头像。
        """
        self.login = LoginDialog(self)  # 创建登录窗口
        self.login.pushButton_reg.setText("修改头像")  # 设置注册按钮的文本为"修改头像"
        self.login.toolButton_loadLogo.setEnabled(True)  # 启用加载Logo按钮
        self.login.tabWidget.setCurrentIndex(1)  # 切换到第二个页面
        self.login.toolButton_go2login.setEnabled(False)  # 禁用"登录"按钮
        moveCenter(self, self.login)  # 将登录窗口移动到屏幕中心
        self.login.exec_()  # 执行登录窗口
