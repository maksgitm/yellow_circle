import random
import sys


from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPainter, QColor
from PyQt6 import uic


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Желтая окружность')
        self.draw_el.clicked.connect(self.run)

        self.do_paint = False

    def run(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_ellipse(qp)
            qp.end()

    def draw_ellipse(self, qp):
        h = random.randrange(10, 500)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(250, 100, h, h)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
