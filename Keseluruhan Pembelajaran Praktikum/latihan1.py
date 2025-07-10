from PyQt5.QtWidgets import QMainWindow, QApplication
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Initialize and configure custom UI elements
        self.setWindowTitle("PyQt Major Classes Demo")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())