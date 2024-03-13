import sys
from PyQt5.QtCore import QDate, QDateTime, QTime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class DateTimeEditDemo(QWidget):
    def __init__(self):
        super(DateTimeEditDemo, self).__init__()
        self.initUI()

    def initUI(self):
        # 设置标题与初始大小
        self.setWindowTitle('QDateTimeEdit 例子')
        self.resize(300, 90)
        # 垂直布局
        layout = QVBoxLayout()
        # 创建日期时间空间，并把当前日期时间赋值，。并修改显示格式
        self.dateEdit = QDateTimeEdit(QDateTime.currentDateTime(), self)
        self.dateEdit.setDisplayFormat('yyyy-MM-dd HH:mm:ss')
        # 设置日期最大值与最小值，在当前日期的基础上，后一年与前一年
        self.dateEdit.setMinimumDate(QDate.currentDate().addDays(-365))
        self.dateEdit.setMaximumDate(QDate.currentDate().addDays(365))
        # 设置日历控件允许弹出
        self.dateEdit.setCalendarPopup(True)
        # 当日期改变时触发槽函数
        self.dateEdit.dateChanged.connect(self.onDateChanged)
        # 当日期时间改变时触发槽函数
        self.dateEdit.dateTimeChanged.connect(self.onDateTimeChanged)
        # 当时间改变时触发槽函数
        self.dateEdit.timeChanged.connect(self.onTimeChanged)
        # 创建按钮并绑定一个自定义槽函数
        self.btn = QPushButton('获得日期和时间')
        self.btn.clicked.connect(self.onButtonClick)
        # 布局控件的加载与设置
        layout.addWidget(self.dateEdit)
        layout.addWidget(self.btn)
        self.setLayout(layout)
    # 日期发生改变时执行

    def onDateChanged(self, date):
        # 输出改变的日期
        print(date)
        # 无论是日期还是时间改变都执行

    def onDateTimeChanged(self, dateTime):
        # 输出改变的日期时间
        print(dateTime)
    # 时间发生改变执行

    def onTimeChanged(self, time):
        # 输出改变的时间
        print(time)

    def onButtonClick(self):
        dateTime = self.dateEdit.dateTime()
        # 最大日期
        maxDate = self.dateEdit.maximumDate()
        # 最大日期时间
        maxDateTime = self.dateEdit.maximumDateTime()
        # 最大时间
        maxTime = self.dateEdit.maximumTime()
        # 最小日期
        minDate = self.dateEdit.minimumDate()
        # 最小日期时间
        minDateTime = self.dateEdit.minimumDateTime()
        # 最小时间
        minTime = self.dateEdit.minimumTime()
        print('\n选择时间日期')
        print('日期时间=%s' % str(dateTime))
        print('最大日期=%s' % str(maxDate))
        print('最大日期时间=%s' % str(maxDateTime))
        print('最大时间=%s' % str(maxTime))
        print('最小日期=%s' % str(minDate))
        print('最小日期时间=%s' % str(minDateTime))
        print('最小时间=%s' % str(minTime))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = DateTimeEditDemo()
    demo.show()
    sys.exit(app.exec_())
