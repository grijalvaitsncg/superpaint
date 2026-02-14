from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6.QtCore import Qt, QPoint, QPointF, QRectF
from PyQt6.QtGui import QPainter, QPen, QImage
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QFileDialog

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
    
    def save_image(self):
        file_path = QFileDialog.getSaveFileName(
            self,
            "Save image",
            "",
            "PNG Files (*.png);;All Files (*)"
        )
        print(file_path)
        if file_path:
            self.image.save(file_path[0])
            QMessageBox.information(self, "Super Paint","Imagen guardada correctamente")
    
    def open_image(self):
        file_path = QFileDialog.getOpenFileName(
            self,
            "Abrir imagen",
            "",
            "PNG Files (*.png);;All Files (*)"
        )
        if  file_path:
            self.image = QImage(file_path[0])
            self.update()
    def draw_grid(self, value):
        with QPainter(self.image) as painter:
            painter.setPen(QPen(QColor("#ff00000"),1,Qt.PenStyle.SolidLine,Qt.PenCapStyle.RoundCap,Qt.PenJoinStyle.RoundJoin))
            w = self.image.width()
            h = self.image.height()
            div = int(w / int(value)) #600/10
            total_l = int(value)
            self.clear()
            for x in range(1,total_l):
                painter.drawLine(div*x,0,div*x,h)
                painter.drawLine(0,div*x,w,div*x)
        self.update()
    def draw_star(self, value):
        self.clear()
        with QPainter(self.image) as painter:
            painter.setPen(QPen(QColor("#fff"),1,Qt.PenStyle.SolidLine,Qt.PenCapStyle.RoundCap,Qt.PenJoinStyle.RoundJoin))
            w = self.image.width()
            h = self.image.height()
            mid_w = w // 2
            mid_h = h // 2
            div = int(mid_w/ int(value)) #300/10
            painter.drawLine(mid_h,0,mid_w,h )
            painter.drawLine(0,mid_h,w,mid_h)
            for x in range(1,value):
                painter.drawLine(mid_w,div*x, (mid_w+ (div*x )),mid_h )
                painter.drawLine(mid_w,div*x, (mid_w- (div*x )),mid_h )
                
        self.update()
    def draw_f(self, value):
        self.clear()
        with QPainter(self.image) as painter:
            painter.setPen(QPen(QColor("#fff"),1,Qt.PenStyle.SolidLine,Qt.PenCapStyle.RoundCap,Qt.PenJoinStyle.RoundJoin))
            w = self.image.width()
            h = self.image.height()
            mid_w = w // 2
            mid_h = h // 2
            div = int(mid_w/ int(value)) #300/10
            painter.drawLine(mid_h,0,mid_w,h )
            painter.drawLine(0,mid_h,w,mid_h)
            for x in range(1,value):
                painter.drawLine()
        self.update()
    
    def draw_keyboard(self,value):
        self.clear()
        with QPainter(self.image) as painter:
           
            w = self.image.width()
            h = self.image.height()
            for x in range(1,value):
                painter.setPen(Qt.PenStyle.NoPen)
                #Dibuja el cuadro blanco
                painter.setBrush("#FFF")
                rect = QRectF(10,10,30,30)
                painter.drawRect(rect)
                #dibuja el cuadro negro
                painter.setPen(Qt.PenStyle.NoPen)
                painter.setBrush("#000")
                rect2 = QRectF(40,10,30,30)
                painter.drawRect(rect2)