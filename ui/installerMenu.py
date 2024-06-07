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
            QPushButton#completed {
                background-color: #88C0D0;
            }
            QPushButton#current {
                background-color: #5E81AC;
            }
            QPushButton#pending {
                background-color: #4C566A;
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

        self.buttons = []
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

        # Agregar páginas al stacked widget
        self.stacked_widget.addWidget(self.create_page("Bienvenido al Instalador", self.instance_image, 0, True, False))
        self.stacked_widget.addWidget(self.create_page("Configuración Paso 1", self.instance_image, 1, True, True))
        self.stacked_widget.addWidget(self.create_page("Configuración Paso 2", self.instance_validate, 2, True, True))
        self.stacked_widget.addWidget(self.create_page("Proceso de Instalación", self.instance_validate, 3, True, True))
        self.stacked_widget.addWidget(self.create_page("Instalación Completa", None, 4, False, True))

        # Actualizar estado de botones
        self.update_menu_buttons()

    def create_menu_button(self, name, index):
        button = QPushButton(name)
        button.clicked.connect(lambda: self.switch_page(index))
        button.setObjectName("pending")
        self.menu_buttons.addWidget(button)
        self.buttons.append(button)

    def switch_page(self, index):
        current_index = self.stacked_widget.currentIndex()
        next_page = self.stacked_widget.widget(index)

        if current_index < index:
            direction = Qt.Horizontal
        else:
            direction = Qt.Vertical

        self.animate_transition(next_page, direction)
        self.stacked_widget.setCurrentIndex(index)

        # Actualizar estado de botones
        self.update_menu_buttons()

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

    def update_menu_buttons(self):
        current_index = self.stacked_widget.currentIndex()
        for i, button in enumerate(self.buttons):
            if i < current_index:
                button.setObjectName("completed")
            elif i == current_index:
                button.setObjectName("current")
            else:
                button.setObjectName("pending")
            button.setStyle(self.style())

    def create_page(self, text, widget, index, has_next, has_back):
        page = QWidget()
        layout = QVBoxLayout(page)

        # Crear y configurar un QLabel
        label = QLabel(text, alignment=Qt.AlignCenter)
        layout.addWidget(label)

        # Añadir el widget (imagen o validación)
        if widget:
            layout.addWidget(widget)

        # Botones de navegación
        nav_layout = QHBoxLayout()
        if has_back:
            back_button = QPushButton("Atrás")
            back_button.clicked.connect(lambda: self.switch_page(index - 1))
            nav_layout.addWidget(back_button)

        if has_next:
            next_button = QPushButton("Siguiente")
            next_button.clicked.connect(lambda: self.switch_page(index + 1))
            nav_layout.addWidget(next_button)
        else:
            finish_button = QPushButton("Finalizar")
            finish_button.clicked.connect(self.close)
            nav_layout.addWidget(finish_button)

        layout.addLayout(nav_layout)

        return page

 
    def fill_values_in_input_parameters(self):
        self.instance_image.fill_values()
    
    # def fill_value_in_output_parameter(self):