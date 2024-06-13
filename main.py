import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt

from ui.main_windows import MainWindow
# from ui.prueba1 import MainWindow



if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())
