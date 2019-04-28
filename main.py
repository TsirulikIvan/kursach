import sys
import random
import math
from PyQt5.QtWidgets import (QWidget, QVBoxLayout,
    QSizePolicy, QLabel, QFontDialog, QApplication, QToolTip,
    QPushButton, QApplication, QMessageBox, QInputDialog, QLineEdit)
from PyQt5.QtGui import QFont, QIcon, QPainter, QColor, QPen
from PyQt5.QtCore import QCoreApplication, Qt


class App(QWidget):
    '''
    Кастомный класс приложения
    '''
    def __init__(self, wd, hg):
        '''
        Конструктор приложения
        '''
        super().__init__()
        self.width  = wd
        self.height = hg
        self.initUI()

    def initUI(self):

        '''
        Инициализирование объектов(юнитов) интерфейса
        '''

        QToolTip.setFont(QFont('SansSerif', 10))
        self.setGeometry(300, 150, self.width, self.height)
        self.setWindowTitle('Осциллятор')
        self.setWindowIcon(QIcon('icon.png'))
        start_btn = self.createbutton('Начать моделирование', 50)
        start_btn.setToolTip('Кнопка начала отрисовки модели')
        qbtn = self.createbutton('Выйти', 70, 470)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        self.getInteger()
        self.show()

    def createbutton(self, name='Кнопка', x=100, y=50):

        '''
        Создает новую кнопку
        '''

        btn = QPushButton(name, self)
        btn.resize(btn.sizeHint())
        btn.move(x, y)
        return btn

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Завершение работы',
            "Уверены что хотите закрыть", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def paintEvent(self, e):
        start_draw_x = 250
        srard_draw_y = 490
        canvas_width = self.width - start_draw_x - 100
        canvas_height = self.height - 100

        print(canvas_width, canvas_height)
        qp = QPainter()
        qp.begin(self)
        self.draw_sys_coor(qp, start_draw_x, srard_draw_y)
        qp.end()

    def drawPoints(self, qp):
        qp.setPen(Qt.red)
        size = self.size()

    def draw_sys_coor(self, qp, s_x, s_y):
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(s_x, s_y, self.width - 100, s_y)
        qp.drawLine(s_x, s_y, s_x, 50)

    def getInteger(self):
        i, okPressed = QInputDialog.getInt(self, "Get integer", "Кол-во единичных отрезков по x", 28, 0, 100, 1)
        if okPressed:
            print(i)


def model_func(arg):
    x = arg
    return(math.sin(x))

app = QApplication(sys.argv)
ex = App(960, 540)
sys.exit(app.exec_())
