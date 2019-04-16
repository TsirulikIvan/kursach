import sys
from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(1600, 900)
    w.move(0, 0)
    w.setWindowTitle('Гармонический осциллятор')
    w.show()

    sys.exit(app.exec_())
