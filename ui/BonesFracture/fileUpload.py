from PySide6.QtWidgets import QWidget, QPushButton, QFrame, QLabel, QApplication, QFileDialog
from PySide6.QtCore import Qt, Slot

from components.general.subtitle import SubTittle
from entity.parametros import Parametro
from ui.BonesFracture.installerMenu import MenuFracture

class FrameFileUpload(QWidget):
    def __init__(self):
        super().__init__()
        self.widgets()
        self.enabled = False  # Inicializar el estado de habilitación

    def widgets(self):
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        self.main_frame = QFrame(self)
        self.main_frame.setGeometry(screen_geometry)

        SubTittle(410, 180, 400, 50, "Seleccione un archivo(.png o .jpg)", self)

        self.btn_open_file = QPushButton("Seleccionar archivo JPG", self)
        self.btn_open_file.setStyleSheet(
            """
            QPushButton {
                background-color: #FF0000;
                color: #FFFFFF;
                border: none;
                font-size: 22px;
                font-weight: bold;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #AF0507;
            }
            """
        )
        self.btn_open_file.setGeometry(350, 250, 300, 50)
        self.btn_open_file.setCursor(Qt.PointingHandCursor)
        self.btn_open_file.clicked.connect(self.open_file)

        self.lbl_file_selected = QLabel("Archivo no seleccionado", self)
        self.lbl_file_selected.setGeometry(350, 300, 300, 50)

        self.btn_submit_file = QPushButton("Aceptar", self)
        self.btn_submit_file.setGeometry(700, 250, 150, 50)
        self.btn_submit_file.setStyleSheet(
            """
            QPushButton {
                background-color: #FF0000;
                color: #FFFFFF;
                border: none;
                font-size: 22px;
                font-weight: bold;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #AF0507;
            }
            """
        )
        self.btn_submit_file.setEnabled(False)
        self.btn_submit_file.clicked.connect(self.acept_submit)

    def update_submit_button(self):
        if self.enabled:
            self.btn_submit_file.setStyleSheet(
                """
                QPushButton {
                    background-color: #32A207;
                    color: #FFFFFF;
                    border: none;
                    font-size: 22px;
                    font-weight: bold;
                    border-radius: 10px;
                }
                QPushButton:hover {
                    background-color: #278302;
                }
                """
            )
            self.btn_submit_file.setCursor(Qt.PointingHandCursor)
            self.btn_submit_file.setEnabled(True)

    @Slot()
    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo JPG", "", "Archivos JPEG (*.jpeg);;Archivos JPG (*.jpg);; Archivos PNG (*.png)")
        if filename:
            self.enabled = True
            self.lbl_file_selected.setText(filename)  # Aquí se actualiza la etiqueta con el nombre del archivo
            Parametro.get_instance().path = filename  # Guardar el nombre del archivo en el parámetro
            self.update_submit_button()
            print(f"{filename}")

    @Slot()
    def acept_submit(self):
        filename = self.lbl_file_selected.text()
        print(f"file {filename}")

        self.step2 = MenuFracture()
        self.step2.fill_values_in_input_parameters()



        # parametro = Parametro.get_instance(path=filename)


        # print(f"Llenado de datos: {parametro}")
    