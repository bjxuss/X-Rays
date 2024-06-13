from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PySide6.QtGui import QPalette, QBrush, QPixmap

class Frame1(QWidget):
    def __init__(self):
        super().__init__()

        # Configurar la ventana principal
        self.setWindowTitle('Menú de Botones Estilizados')
        self.setGeometry(100, 100, 800, 600)

        # # Configurar el widget central
        # central_widget = QWidget(self)
        # self.setCentralWidget(central_widget)

        # Crear y posicionar los botones
        self.button1 = QPushButton('Fracturas', self)
        self.button1.setGeometry(150, 200, 200, 200)  # (x, y, width, height)
        self.button1.setStyleSheet(self.button_style())

        self.button2 = QPushButton('Neumonia', self)
        self.button2.setGeometry(450, 200, 200, 200)  # (x, y, width, height)
        self.button2.setStyleSheet(self.button_style())

        # Establecer la hoja de estilo del fondo
        self.set_background()

    def set_background(self):
        # Crear un QPalette y configurar el fondo con una imagen
        palette = QPalette()
        background_image = QPixmap('ruta/a/tu/imagen.jpg')
        palette.setBrush(QPalette.Window, QBrush(background_image))
        self.setPalette(palette)

    def button_style(self):
        # Estilo CSS para los botones
        return """
        QPushButton {
            background-color: #3498db;
            color: white;
            border-radius: 10px;
            border: 2px solid #2980b9;
            font-size: 16px;
            padding: 10px;
        }
        QPushButton:hover {
            background-color: #2980b9;
        }
        QPushButton:pressed {
            background-color: #1abc9c;
        }
        """