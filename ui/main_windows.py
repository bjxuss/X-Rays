from PySide6.QtWidgets import QMainWindow, QApplication, QStackedWidget
from PySide6.QtGui import QScreen

from ui.fileUpload import FrameFileUpload
from ui.installerMenu import Menu



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("X-Rays Bones Fracture")
        self.resize(330, 250)
        self.widget_frame_init()
        self.center_windows()

    def widget_frame_init(self):
        self.apilacion_widgets = QStackedWidget(self)

        # frames or pages
        self.frame_load_file = FrameFileUpload()
        

        self.apilacion_widgets.addWidget(self.frame_load_file)

        self.setCentralWidget(self.apilacion_widgets)
        self.apilacion_widgets.setCurrentWidget(self.frame_load_file) # aquí modifico la ventana que se mostrará primero 

        self.conexiones()

    def conexiones(self):
        self.frame_load_file.btn_submit_file.clicked.connect(self.change_frame2)

    def change_frame2(self):
        self.frame2 = Menu()
        self.apilacion_widgets.addWidget(self.frame2)

        self.apilacion_widgets.setCurrentWidget(self.frame2)

        self.frame2.fill_values_in_input_parameters()
    

    def center_windows(self):
        screen_size = QScreen.availableGeometry(QApplication.primaryScreen())
        self.setGeometry(0, 0, screen_size.width(), screen_size.height())