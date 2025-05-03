from PyQt6 import QtCore, QtGui, QtWidgets

class ImageScannerUI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Scanner")
        self.setGeometry(100, 100, 800, 590)  # Adjusted size to match UI_ThongKe

        # Central widget
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)

        # Main layout
        self.main_layout = QtWidgets.QVBoxLayout(self.central_widget)

        # Header Frame
        self.header_frame = QtWidgets.QFrame()
        self.header_frame.setStyleSheet(
            """
            background-color: #f1f1f1;
            border-bottom: 2px solid #ccc;
            """
        )
        self.header_frame.setFixedHeight(51)

        self.header_layout = QtWidgets.QHBoxLayout(self.header_frame)
        self.header_label = QtWidgets.QLabel("Image Scanner System")
        self.header_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.header_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.header_layout.addWidget(self.header_label)

        self.main_layout.addWidget(self.header_frame)

        # Content Frame
        self.content_frame = QtWidgets.QFrame()
        self.content_frame.setStyleSheet(
            """
            border: 1px solid #ddd;
            background-color: #f9f9f9;
            border-radius: 5px;
            padding: 20px;
            """
        )

        # Layout for content
        self.content_layout = QtWidgets.QVBoxLayout(self.content_frame)

        # Folder selection widgets
        self.folder_label = QtWidgets.QLabel("Select a Folder:")
        self.folder_label.setStyleSheet("font-size: 14px; font-weight: bold;")
        self.folder_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)

        self.folder_path = QtWidgets.QLineEdit()
        self.folder_path.setReadOnly(True)
        self.folder_path.setStyleSheet(
            """
            background-color: #e8f0fe;
            border: 1px solid #ccc;
            border-radius: 3px;
            padding: 10px;
            font-size: 14px;
            """
        )

        self.select_folder_button = QtWidgets.QPushButton("Select Folder")
        self.select_folder_button.setStyleSheet(
            """
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            font-size: 14px;
            """
        )
        self.select_folder_button.clicked.connect(self.select_folder)

        folder_layout = QtWidgets.QVBoxLayout()
        folder_layout.addWidget(self.folder_label)
        folder_layout.addWidget(self.folder_path)
        folder_layout.addWidget(self.select_folder_button, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)

        self.content_layout.addLayout(folder_layout)

        # Add content frame to main layout
        self.main_layout.addWidget(self.content_frame, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)

        # Footer Frame
        self.footer_frame = QtWidgets.QFrame()
        self.footer_frame.setStyleSheet(
            """
            background-color: #f1f1f1;
            border-top: 2px solid #ccc;
            """
        )
        self.footer_frame.setFixedHeight(31)

        self.footer_layout = QtWidgets.QHBoxLayout(self.footer_frame)
        self.footer_label = QtWidgets.QLabel("© 2024 Image Scanner UI")
        self.footer_label.setStyleSheet("font-size: 10px;")
        self.footer_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.footer_layout.addWidget(self.footer_label)

        self.main_layout.addWidget(self.footer_frame)

    def select_folder(self):
        try:
            folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Folder")
            if folder:
                self.folder_path.setText(folder)
        except Exception as e:
            print(f"Error selecting folder: {e}")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = ImageScannerUI()
    window.show()
    sys.exit(app.exec())