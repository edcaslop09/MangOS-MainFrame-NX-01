import sys 

from PySide6.QtWidgets import QApplication

from gui.main_window import MainWindow
from gui.theme import get_stylesheet


def iniciar_gui():
    app = QApplication(sys.argv)

    app.setStyleSheet(get_stylesheet())

    ventana = MainWindow()
    ventana.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    iniciar_gui()