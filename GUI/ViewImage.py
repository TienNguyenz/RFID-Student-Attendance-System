# Form implementation generated from reading ui file 'ui/ViewImage.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow
import os


class ViewImage(object):
    idSV = ''

    def __init__(self, id):
        self.idSV = id

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)  # Tăng kích thước cửa sổ để có không gian hiển thị ảnh lớn
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 675, 412))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")

        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout.setObjectName("gridLayout")

        # Tạo QLabel để hiển thị ảnh
        label = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_2)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Căn giữa ảnh trong label
        label.setFixedSize(640, 480)  # Điều chỉnh kích thước của label

        # Tạo đối tượng QPixmap từ file ảnh
        file_path = os.path.join("../image/photo/" + self.idSV + '-barcode1.jpg')  # Chỉ lấy 1 ảnh
        pixmap = QPixmap(file_path)

        # Thay đổi kích thước của ảnh (giữ tỷ lệ gốc, không làm biến dạng)
        scaled_pixmap = pixmap.scaled(label.size(), Qt.AspectRatioMode.KeepAspectRatio,
                                      Qt.TransformationMode.SmoothTransformation)
        label.setPixmap(scaled_pixmap)

        # Đặt QLabel vào ô trong lưới
        self.gridLayout.addWidget(label, 0, 0)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "View Image"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ViewImage('SV007')
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
