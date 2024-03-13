import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QMessageBox, QVBoxLayout
from PyQt5.QtWidgets import QInputDialog, QGridLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QDate, QDateTime, QTime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('模拟端')
        self.setFixedSize(800, 600)  # 调整整个框的大小
        self.center()  # 居中

        # 设置样式表
        style = "font-size: 160px; font-family: Arial;"
        self.setStyleSheet("QMainWindow::title {" + style + "}")

        # 创建按钮
        self.start_button = QPushButton('开始')
        self.stop_button = QPushButton('停止')
        self.pause_button = QPushButton('暂停')
        self.config_button = QPushButton('参数配置')
        self.data_button = QPushButton('设定时间')

        # 调整按钮大小
        self.start_button.setFixedSize(350, 150)
        self.stop_button.setFixedSize(350, 150)
        self.pause_button.setFixedSize(350, 150)
        self.config_button.setFixedSize(350, 150)
        self.data_button.setFixedSize(250, 100)

        # # 创建写入框
        # self.write_edit = QLineEdit()
        # self.write_edit.setPlaceholderText('发送时间')
        # self.write_edit.setFixedSize(750, 100)

        # 创建日期时间空间，并把当前日期时间赋值，。并修改显示格式
        self.dateEdit = QDateTimeEdit(QDateTime.currentDateTime(), self)
        self.dateEdit.setFixedSize(400, 80)
        self.dateEdit.setDisplayFormat('yyyy-MM-dd HH:mm:ss')
        self.dateEdit.setMinimumDate(QDate.currentDate().addDays(-365))
        self.dateEdit.setMaximumDate(QDate.currentDate().addDays(365))
        self.dateEdit.setCalendarPopup(True)

        # 按钮布局
        grid = QGridLayout()
        grid.setSpacing(30)
        grid.addWidget(self.start_button, 0, 0, 1, 1)  # 第一行第一列
        grid.addWidget(self.stop_button, 0, 1, 1, 1)  # 第一行第二列
        grid.addWidget(self.pause_button, 1, 0, 1, 1)  # 第二行第一列
        grid.addWidget(self.config_button, 1, 1, 1, 1)  # 第二行第二列
        grid.addWidget(self.dateEdit, 2, 0, 1, 1)
        grid.addWidget(self.data_button, 2, 1, 1, 1, Qt.AlignmentFlag.AlignCenter)
        self.setLayout(grid)

        # 字体设置
        font = QFont()
        font.setFamily('微软雅黑')
        font.setBold(True)
        font.setPointSize(30)
        font.setWeight(90)

        font_data = QFont()
        font_data.setFamily('微软雅黑')
        font_data.setBold(True)
        font_data.setPointSize(20)
        font_data.setWeight(80)

        # 按钮设置
        self.start_button.setFont(font)
        self.stop_button.setFont(font)
        self.pause_button.setFont(font)
        self.config_button.setFont(font)
        self.data_button.setFont(font)
        self.dateEdit.setFont(font_data)

        # 按钮样式
        # style_start = "QPushButton { background-color: #4CAF50; color: white; font-size: 16px; }"
        # style_stop = "QPushButton { background-color: #f44336; color: white; font-size: 16px; }"
        # self.start_button.setStyleSheet("QMainWindow::title {" + style_start + "}")
        # self.stop_button.setStyleSheet("QMainWindow::title {" + style_stop + "}")

        # 布局管理
        # vbox = QVBoxLayout()
        # vbox.addWidget(self.start_button)
        # vbox.addWidget(self.stop_button)
        # vbox.addWidget(self.pause_button)
        # vbox.addWidget(self.config_button)
        # vbox.addWidget(self.write_edit)
        # self.setLayout(vbox)

        # 绑定事件函数
        self.start_button.clicked.connect(self.start_button_clicked)
        self.stop_button.clicked.connect(self.stop_button_clicked)
        self.pause_button.clicked.connect(self.pause_button_clicked)
        self.config_button.clicked.connect(self.show_config_dialog)
        self.data_button.clicked.connect(self.get_time)

    def start_button_clicked(self):
        print('开始按钮被点击')

    def stop_button_clicked(self):
        print('停止按钮被点击')

    def pause_button_clicked(self):
        print('暂停按钮被点击')

    def get_time(self):
        dateTime = self.dateEdit.dateTime()
        print(dateTime)

    def show_config_dialog(self):
        # 弹出参数配置对话框
        file_name, ok1 = QInputDialog.getText(self, '参数配置', '请输入文件名:')
        frequency, ok2 = QInputDialog.getInt(self, '参数配置', '请输入发送频率:')
        terminal_id, ok3 = QInputDialog.getText(self, '参数配置', '请输入终端标识:')

        if ok1 and ok2 and ok3:
            # 处理配置参数
            print('文件名:', file_name)
            print('发送频率:', frequency)
            print('终端标识:', terminal_id)

    def center(self):
        # 获取窗口的大小和屏幕的分辨率
        window_rect = self.frameGeometry()
        screen_center = QApplication.desktop().screenGeometry().center()

        # 计算窗口居中的位置
        window_rect.moveCenter(screen_center)
        self.move(window_rect.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec_())
