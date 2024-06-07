from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QFrame
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

from entity.parametros import Parametro

class ImageWidget(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        self.setGeometry(10, 10, 350, 350)  # Ajusta el tamaño según tus necesidades
        

    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        # Crear un QLabel para mostrar la imagen
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        
        # Añadir el QLabel al layout
        layout.addWidget(self.image_label)
    
    def set_image(self, image_path):
        if isinstance(image_path, str):
            pixmap = QPixmap(image_path)
            self.image_label.setPixmap(pixmap)
        else:
            print("Error: image_path is not a string")


    def resizeEvent(self, event):
        self.set_image(Parametro.get_instance().path)
        super().resizeEvent(event)

    def fill_values(self):
        self.instance_of_parameters = Parametro().get_instance()
        print(f"fill_values: --> {self.instance_of_parameters}")
        
        # Llenamos las etiquetas con los resultados de las entradas, salidas y parámetros
        self.set_image(self.instance_of_parameters.path)

        

    

