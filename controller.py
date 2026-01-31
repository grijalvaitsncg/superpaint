
from PyQt6.QtGui import QColor

class MainController:
    def __init__(self, main_window, ui):
        self.main_window=main_window
        self.ui=ui
        self.connect_signals()
    
    #declaramos los eventos
    def connect_signals(self):
        self.ui.txtColor.textChanged.connect(self.update_color)
        self.ui.slider.valueChanged.connect(self.update_pincel)

    def update_pincel(self,width):
        print(width)

    def update_color(self):
        color = self.ui.txtColor.toPlainText().strip()
        print(color)
        fondo  = QColor(color)
        if fondo.isValid():
            self.ui.txtColor.setStyleSheet(f"background-color: {color};color:{self.color_inverse(fondo).name()}")
    #F => 255
    def color_inverse(self, color):
        inverse = QColor(255-color.red(), 255-color.green(), 255-color.blue())
        return inverse