from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt, QPoint, QPointF, QRectF
from PyQt6.QtGui import QPainter, QPen, QImage
from PyQt6.QtGui import QColor

class Canvas(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WidgetAttribute.WA_StaticContents)
        self.image = QImage(self.size(), QImage.Format.Format_ARGB32)
        self.image.fill(QColor("#2d2d2d"))
        self.drawing = False
        self.last_point = QPoint()
        self.pen_color = QColor("#FFF")
        self.pen_width = 2