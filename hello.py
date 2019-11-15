from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor
from random import choice
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        window = InitUi(self)
        window.create()

    def button(self):
        self.update()

    def paintEvent(self, QPaintEvent):
        qp = QPainter()
        qp.begin(self)
        self.circles(qp)
        qp.end()

    def circles(self, qp):
        for i in range(10):
            qp.setBrush(QColor(choice(range(255)), choice(range(255)), choice(range(255))))
            size = choice(range(300))
            qp.drawEllipse(choice(range(300)), choice(range(300)),
                           size, size)


class InitUi:
    def __init__(self, window):
        self.window = window

    def create(self):
        self.window.setFixedSize(500, 500)
        self.window.btn = QPushButton('Круги', self.window)
        self.window.btn.resize(101, 23)
        self.window.btn.move(200, 460)
        self.window.btn.clicked.connect(self.window.button)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
