import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget

class QLabelExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # QMainWindow 내부의 central widget 생성
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # QVBoxLayout을 central widget에 추가
        layout = QVBoxLayout(central_widget)

        for i in range(10):
            label = QLabel(f"Label {i}")
            layout.addWidget(label)

        self.setWindowTitle('QLabel 예제')
        self.setGeometry(100, 100, 400, 400)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QLabelExample()
    ex.show()
    sys.exit(app.exec_())