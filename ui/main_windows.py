from PySide6.QtWidgets import QMainWindow, QApplication, QStackedWidget
from PySide6.QtGui import QScreen


from ui.frame1 import Frame1
from ui.BonesFracture.installerMenu import MenuFracture
from ui.Pneumonia.installerMenu2 import MenuPneumonia



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
        # self.frame_load_file = FrameFileUpload()
        

        self.instance_of_frame1 = Frame1()
        self.apilacion_widgets.addWidget(self.instance_of_frame1)
        # self.apilacion_widgets.addWidget(self.frame_load_file)

        self.setCentralWidget(self.apilacion_widgets)
        self.apilacion_widgets.setCurrentWidget(self.instance_of_frame1) # aquí modifico la ventana que se mostrará primero 

        self.conexiones()

    def conexiones(self):
        # self.frame_load_file.btn_submit_file.clicked.connect(self.change_frame2)
        self.instance_of_frame1.button1.clicked.connect(self.change_frame2)
        self.instance_of_frame1.button2.clicked.connect(self.change_frame3)

    def change_frame2(self):
        self.instance_of_menu_bones_fracture = MenuFracture()
        self.apilacion_widgets.addWidget(self.instance_of_menu_bones_fracture)

        self.apilacion_widgets.setCurrentWidget(self.instance_of_menu_bones_fracture)
    
    def change_frame3(self):
        self.instance_of_menu_pneumonia = MenuPneumonia()
        self.apilacion_widgets.addWidget(self.instance_of_menu_pneumonia)

        self.apilacion_widgets.setCurrentWidget(self.instance_of_menu_pneumonia)

        
    

    def center_windows(self):
        screen_size = QScreen.availableGeometry(QApplication.primaryScreen())
        self.setGeometry(0, 0, screen_size.width(), screen_size.height())