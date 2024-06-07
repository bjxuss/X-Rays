from PySide6.QtWidgets import QLabel

class SubTittle(QLabel):
    def __init__(self, x:int,y:int,xx:int,yy:int, text:str, parent=None):
        super().__init__(parent)
        self.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.setText(text)
        self.setGeometry(x,y,xx,yy)