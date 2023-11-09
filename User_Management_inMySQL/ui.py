from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(562, 531)
        self.center_window()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.username_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.username_textEdit.setGeometry(QtCore.QRect(170, 150, 251, 41))
        self.username_textEdit.setObjectName("login_textEdit")
        self.password_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.password_textEdit.setGeometry(QtCore.QRect(170, 240, 251, 41))
        self.password_textEdit.setObjectName("register_textEdit")
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(90, 160, 67, 17))
        self.username_label.setObjectName("username")
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(100, 250, 67, 17))
        self.password_label.setObjectName("password")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(180, 370, 89, 25))
        self.loginButton.setObjectName("login_button")
        self.registerButton = QtWidgets.QPushButton(self.centralwidget)
        self.registerButton.setGeometry(QtCore.QRect(320, 370, 89, 25))
        self.registerButton.setObjectName("register_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 562, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.loginButton.clicked.connect(MainWindow.login)
        self.registerButton.clicked.connect(MainWindow.register)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.username_label.setText(_translate("MainWindow", "用户名"))
        self.password_label.setText(_translate("MainWindow", "密码"))
        self.loginButton.setText(_translate("MainWindow", "登录"))
        self.registerButton.setText(_translate("MainWindow", "注册"))

    def center_window(self):
        # 获取屏幕信息
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口大小和位置
        window_size = self.geometry()
        # 计算窗口的新位置
        x = (screen.width() - window_size.width()) // 2
        y = (screen.height() - window_size.height()) // 2
        # 设置窗口的位置
        self.move(x, y)