from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt, QPoint, QPointF, QRectF
from PyQt6.QtGui import QPainter, QPen, QImage
from PyQt6.QtGui import QColor

class Canvas(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WidgetAttribute.WA_StaticContents)
        self.image = QImage(self.size(), QImage.Format.Format_ARGB32)
        self.image.fill(QColor("#fff"))
        self.drawing = False
        self.last_point = QPoint()
        self.pen_color = QColor("#f00")
        self.pen_width = 2
    def paintEvent(self, event):
        with QPainter(self) as painter:
            painter.drawImage(event.rect(), self.image, event.rect())
    def resizeEvent(self, event):
        
        if self.width() > self.image.width() or self.height() > self.image.height():
            new_width =max(self.width(), self.image.width())
            max_height = max(self.height(), self.image.height())
            new_image = QImage(new_width, max_height, QImage.Format.Format_ARGB32)
            new_image.fill(QColor("#2d2d2d"))
            with QPainter(new_image) as painter:
                painter.drawImage(0,0,self.image)
            self.image = new_image
        super().resizeEvent(event)
        #self.draw_examples()
       
    def draw_examples(self):
        with QPainter(self.image) as painter:
            painter.setPen(QPen(QColor("#ff00000"),10,Qt.PenStyle.SolidLine,Qt.PenCapStyle.RoundCap,Qt.PenJoinStyle.RoundJoin))
            painter.drawLine(300,0,300,600)
            painter.drawLine(0,300,600,300)
            painter.drawRect(265,265,70,70)
        self.update()
    def mousePressEvent(self, a0):
        if a0.button() == Qt.MouseButton.LeftButton:
            self.last_point = a0.position().toPoint()
            self.drawing = True
    def mouseMoveEvent(self, a0):
        if (a0.buttons() & Qt.MouseButton.LeftButton) and self.drawing:
            self.draw_line_to(a0.position().toPoint())

    def mouseReleaseEvent(self, a0):
        if (a0.button() == Qt.MouseButton.LeftButton) and self.drawing:
            self.draw_line_to(a0.position().toPoint())
            self.drawing=False
    def draw_line_to(self, end_point):
        with QPainter(self.image) as painter:
            painter.setPen(QPen(self.pen_color,self.pen_width,Qt.PenStyle.SolidLine,Qt.PenCapStyle.RoundCap,Qt.PenJoinStyle.RoundJoin))
            painter.drawLine(self.last_point, end_point)
            #painter.drawEllipse(end_point, 30,30)
        self.update()
        self.last_point = end_point
    def clear(self):
        self.image.fill(QColor("#2d2d2d"))
        self.update()