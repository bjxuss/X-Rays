from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QFrame
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

from entity.parametro2 import Parametro2
from logic.Pneumonia.predict import Predict2



class ValidateFramePneumonia(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        self.setGeometry(30, 30, 350, 350)  # Ajusta el tamaño según tus necesidades

    def setup_ui(self):

        layout = QVBoxLayout(self)

        # Crear un QLabel para mostrar la predicción
        self.prediction_label = QLabel(self)
        self.prediction_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.prediction_label)

    def fill_values_output(self):
        self.instance_of_parameter = Parametro2().get_instance()
        self.image = self.instance_of_parameter.path2

    
        # Obtener la predicción
        self.instace_output = Predict2()

        self.output = self.instace_output.predict_image(self.image)

        # Mostrar la predicción en el QLabel
        self.prediction_label.setText(f"Predicción: {self.output}")   