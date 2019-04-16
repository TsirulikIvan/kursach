import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication, QMessageBox)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QCoreApplication

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
        start_btn = self.createbutton('Начать моделирование')
        start_btn.setToolTip('Кнопка начала отрисовки модели')
        qbtn = self.createbutton('Выйти', 100, 150)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
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

app = QApplication(sys.argv)
ex = App(960, 540)
sys.exit(app.exec_())
