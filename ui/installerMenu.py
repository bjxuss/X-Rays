import sys
from PySide6.QtWidgets import QFrame, QMainWindow, QWidget, QVBoxLayout, QPushButton, QStackedWidget, QLabel, QHBoxLayout
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve

from entity.parametros import Parametro
from ui.FrameStep1.FrameImage import ImageWidget
from ui.FrameStep2.FrameValidate import ValidateFrame

class Menu(QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()
        
        self.setWindowTitle("Instalador")
        self.setGeometry(100, 100, 800, 600)
        print("File --> ", Parametro.get_instance().path)
        
        # Estilo de la ventana
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2E3440;
            }
            QPushButton {
                background-color: #4C566A;
                color: #D8DEE9;
                border: 1px solid #D8DEE9;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #5E81AC;
            }
            QLabel {
                color: #D8DEE9;
                font-size: 24px;
            }
            
        """)

        # Configuración del widget principal y layout
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.layout = QHBoxLayout(self.main_widget)
        
        # Menú de botones
        self.menu_buttons = QVBoxLayout()
        self.layout.addLayout(self.menu_buttons)
        
        self.create_menu_button("Inicio", 0)
        self.create_menu_button("Paso 1", 1)
        self.create_menu_button("Paso 2", 2)
        self.create_menu_button("Instalar", 3)
        self.create_menu_button("Finalizar", 4)
        
        # StackedWidget para cambiar entre páginas
        self.stacked_widget = QStackedWidget()
        self.layout.addWidget(self.stacked_widget)

        
        self.instance_image = ImageWidget()
        self.instance_image.set_image(Parametro.get_instance().path)
        print(f"Instance image --> {self.instance_image}")

        self.instance_validate = ValidateFrame()

        self.stacked_widget.addWidget(self.create_page("Bienvenido al Instalador", self.instance_image, True ))
        self.stacked_widget.addWidget(self.create_page("Configuración Paso 1", self.instance_image))
        self.stacked_widget.addWidget(self.create_page("Configuración Paso 2", False))
        self.stacked_widget.addWidget(self.create_page("Proceso de Instalación", False))
        self.stacked_widget.addWidget(self.create_page("Instalación Completa", False))

    def create_menu_button(self, name, index):
        button = QPushButton(name)
        button.clicked.connect(lambda: self.switch_page(index))
        self.menu_buttons.addWidget(button)

    def switch_page(self, index):
        current_index = self.stacked_widget.currentIndex()
        next_page = self.stacked_widget.widget(index)
        
        if current_index < index:
            direction = Qt.Horizontal
        else:
            direction = Qt.Vertical
        
        self.animate_transition(next_page, direction)
        self.stacked_widget.setCurrentIndex(index)
    
    def animate_transition(self, next_page, direction):
        animation = QPropertyAnimation(next_page, b"pos")
        animation.setDuration(500)
        animation.setEasingCurve(QEasingCurve.InOutQuad)
        
        if direction == Qt.Horizontal:
            next_page.move(self.width(), 0)
            animation.setStartValue(next_page.pos())
            animation.setEndValue(self.rect().topLeft())
        else:
            next_page.move(0, self.height())
            animation.setStartValue(next_page.pos())
            animation.setEndValue(self.rect().topLeft())
        
        animation.start()

    # ! Default
    def create_page(self, text, image="", btn_val = False):
        page = QWidget()
        layout = QVBoxLayout(page)
        
        # Crear y configurar un QLabel
        label = QLabel(text, alignment=Qt.AlignCenter)
        
        # Crear y configurar un QFrame
        frame = QFrame()
        frame.setFrameShape(QFrame.Box)
        frame.setFrameShadow(QFrame.Raised)
        frame.setStyleSheet("background-color: #333; border: 1px solid #555;")
        frame.setMinimumHeight(200)

        
        
        # Añadir QLabel y QFrame al layout de la página
        layout.addWidget(label)

        # Añadir la imagen si se proporciona una ruta de imagen
        if image:
            
            # self.button_show_step2 = QPushButton("Validar", self)
            # self.button_show_step2.setStyleSheet("background: blue; color: white; font-size: 25px;")
            # self.button_show_layers.setGeometry(55, 440, 250, 30)
            # self.button_show_layers.clicked.connect(self.show_layers)
            
            layout.addWidget(image)
        
        layout.addWidget(frame)
        
        return page


    
    
    def fill_values_in_input_parameters(self):
        self.instance_image.fill_values()
    
    # def fill_value_in_output_parameter(self):