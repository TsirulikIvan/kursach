import sys
from PyQt5.QtWidgets import(QWidget, QToolTip,
    QPushButton, QApplication)
from PyQt5.QtGui import QIcon


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
        self.setGeometry(300, 150, self.width, self.height)
        self.setWindowTitle('Осциллятор')
        self.setWindowIcon(QIcon('icon.png'))
        btn1 = self.createbutton()
        self.show()

    def createbutton(self, name='Кнопка', x=100, y=50):
        '''
        Создает новую кнопку
        '''
        btn = QPushButton(name, self)
        btn.resize(btn.sizeHint())
        btn.move(x, y)
        return btn

app = QApplication(sys.argv)
ex = App(960, 540)
sys.exit(app.exec_())
