# Form implementation generated from reading ui file 'ui/QuanLyGiangVien.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
import os
from datetime import datetime
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from BUS.GiangVienBUS import GiangVienBUS
from DAL.GiangVien import GiangVien
from BUS.TaiKhoanBUS import TaiKhoanBUS
from check_error import check_error
class UI_QuanLyGiangVien(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(800, 590)
                self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.frmChangeBuoiHoc = QtWidgets.QFrame(parent=self.centralwidget)
                self.frmChangeBuoiHoc.setGeometry(QtCore.QRect(19, 99, 231, 471))
                self.frmChangeBuoiHoc.setStyleSheet("#frmChangeBuoiHoc\n"
        "{\n"
        "    border-width: 2;\n"
        "    border-radius: 5;\n"
        "     border-style: solid;\n"
        "      border-color: #457fca;\n"
        "}")
                self.frmChangeBuoiHoc.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
                self.frmChangeBuoiHoc.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
                self.frmChangeBuoiHoc.setObjectName("frmChangeBuoiHoc")
                self.label_5 = QtWidgets.QLabel(parent=self.frmChangeBuoiHoc)
                self.label_5.setGeometry(QtCore.QRect(10, 30, 211, 21))
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.label_5.setFont(font)
                self.label_5.setStyleSheet("#label_5\n"
        "{\n"
        "    font-weight:bold;\n"
        "}")
                self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.label_5.setObjectName("label_5")
                self.label_11 = QtWidgets.QLabel(parent=self.frmChangeBuoiHoc)
                self.label_11.setGeometry(QtCore.QRect(20, 80, 81, 21))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.label_11.setFont(font)
                self.label_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
                self.label_11.setObjectName("label_11")
                self.label_12 = QtWidgets.QLabel(parent=self.frmChangeBuoiHoc)
                self.label_12.setGeometry(QtCore.QRect(20, 130, 81, 21))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.label_12.setFont(font)
                self.label_12.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
                self.label_12.setObjectName("label_12")
                self.label_13 = QtWidgets.QLabel(parent=self.frmChangeBuoiHoc)
                self.label_13.setGeometry(QtCore.QRect(20, 180, 81, 21))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.label_13.setFont(font)
                self.label_13.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
                self.label_13.setObjectName("label_13")
                self.txtHoTen = QtWidgets.QLineEdit(parent=self.frmChangeBuoiHoc)
                self.txtHoTen.setGeometry(QtCore.QRect(100, 80, 111, 21))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.txtHoTen.setFont(font)                
                self.txtHoTen.setObjectName("txtHoTen")
                self.txtSoDienThoai = QtWidgets.QLineEdit(parent=self.frmChangeBuoiHoc)
                self.txtSoDienThoai.setGeometry(QtCore.QRect(100, 130, 111, 21))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.txtSoDienThoai.setFont(font)                
                self.txtSoDienThoai.setObjectName("txtSoDienThoai")
                self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.frmChangeBuoiHoc)
                self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 300, 171, 51))
                self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
                self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
                self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout.setSpacing(10)
                self.horizontalLayout.setObjectName("horizontalLayout")
                self.btnThem = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
                self.btnThem.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
                self.btnThem.setStyleSheet("#btnThem{\n"
        "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(69, 127, 202, 255), stop:1 rgba(86, 145, 200, 255));\n"
        "color:white;\n"
        "font-weight:bold;\n"
        "border-radius:3px;\n"
        "padding: 5px;\n"
        "}\n"
        "#btnThem:hover{\n"
        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(107, 149, 202, 255), stop:1 rgba(86, 145, 200, 255));\n"
        "}")
                self.btnThem.setObjectName("btnThem")
                self.btnThem.clicked.connect(self.add)
                self.horizontalLayout.addWidget(self.btnThem)
                self.btnSua = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
                self.btnSua.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
                self.btnSua.setStyleSheet("#btnSua{\n"
        "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(69, 127, 202, 255), stop:1 rgba(86, 145, 200, 255));\n"
        "color:white;\n"
        "font-weight:bold;\n"
        "border-radius:3px;\n"
        "padding: 5px;\n"
        "}\n"
        "#btnSua:hover{\n"
        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(107, 149, 202, 255), stop:1 rgba(86, 145, 200, 255));\n"
        "}")
                self.btnSua.setObjectName("btnSua")
                self.btnSua.clicked.connect(self.update)
                self.horizontalLayout.addWidget(self.btnSua)
                self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.frmChangeBuoiHoc)
                self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 350, 171, 51))
                self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
                self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
                self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_2.setSpacing(10)
                self.horizontalLayout_2.setObjectName("horizontalLayout_2")
                self.btnXoa = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
                self.btnXoa.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
                self.btnXoa.setStyleSheet("#btnXoa{\n"
        "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(69, 127, 202, 255), stop:1 rgba(86, 145, 200, 255));\n"
        "color:white;\n"
        "font-weight:bold;\n"
        "border-radius:3px;\n"
        "padding: 5px;\n"
        "}\n"
        "#btnXoa:hover{\n"
        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(107, 149, 202, 255), stop:1 rgba(86, 145, 200, 255));\n"
        "}")
                self.btnXoa.setObjectName("btnXoa")
                self.btnXoa.clicked.connect(self.delete)
                self.horizontalLayout_2.addWidget(self.btnXoa)
                self.btnLamMoi = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
                self.btnLamMoi.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
                self.btnLamMoi.setStyleSheet("#btnLamMoi{\n"
        "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(69, 127, 202, 255), stop:1 rgba(86, 145, 200, 255));\n"
        "color:white;\n"
        "font-weight:bold;\n"
        "border-radius:3px;\n"
        "padding: 5px;\n"
        "}\n"
        "#btnLamMoi:hover{\n"
        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(107, 149, 202, 255), stop:1 rgba(86, 145, 200, 255));\n"
        "}")
                self.btnLamMoi.setObjectName("btnLamMoi")
                self.btnLamMoi.clicked.connect(self.clear)
                self.horizontalLayout_2.addWidget(self.btnLamMoi)
                self.cmbTaiKhoan = QtWidgets.QComboBox(parent=self.frmChangeBuoiHoc)
                self.cmbTaiKhoan.setGeometry(QtCore.QRect(100, 181, 111, 21))
                self.cmbTaiKhoan.setObjectName("cmbTaiKhoan")
                self.cmbTaiKhoan.addItem("","")
                self.frmInfoBuoiHoc = QtWidgets.QFrame(parent=self.centralwidget)
                self.frmInfoBuoiHoc.setGeometry(QtCore.QRect(270, 100, 511, 471))
                self.frmInfoBuoiHoc.setStyleSheet("#frmInfoBuoiHoc\n"
        "{\n"
        "    border-width: 2;\n"
        "    border-radius: 5;\n"
        "     border-style: solid;\n"
        "      border-color: #457fca;\n"
        "}")
                self.frmInfoBuoiHoc.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
                self.frmInfoBuoiHoc.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
                self.frmInfoBuoiHoc.setObjectName("frmInfoBuoiHoc")
                self.frame_3 = QtWidgets.QFrame(parent=self.frmInfoBuoiHoc)
                self.frame_3.setGeometry(QtCore.QRect(20, 10, 471, 81))
                self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.Box)
                self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
                self.frame_3.setObjectName("frame_3")
                self.label_17 = QtWidgets.QLabel(parent=self.frame_3)
                self.label_17.setGeometry(QtCore.QRect(10, 12, 131, 21))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.label_17.setFont(font)
                self.label_17.setObjectName("label_17")
                self.label_18 = QtWidgets.QLabel(parent=self.frame_3)
                self.label_18.setGeometry(QtCore.QRect(10, 40, 101, 21))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.label_18.setFont(font)
                self.label_18.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
                self.label_18.setObjectName("label_18")
                self.cmbOptionFind = QtWidgets.QComboBox(parent=self.frame_3)
                self.cmbOptionFind.setGeometry(QtCore.QRect(110, 40, 101, 21))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.cmbOptionFind.setFont(font)
                self.cmbOptionFind.setObjectName("cmbOptionFind")
                self.cmbOptionFind.addItem("Mã giảng viên", "magiangvien")
                self.cmbOptionFind.addItem("Họ tên", "hoten")
                self.cmbOptionFind.addItem("Số điện thoại", "sodienthoai")
                self.cmbOptionFind.addItem("Mã tài khoản", "mataikhoan")
                self.cmbOptionFind.currentIndexChanged.connect(self.find)
                self.txtFind = QtWidgets.QLineEdit(parent=self.frame_3)
                self.txtFind.setGeometry(QtCore.QRect(220, 40, 231, 21))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.txtFind.setFont(font)
                self.txtFind.setText("")
                self.txtFind.setObjectName("txtFind")
                self.txtFind.textChanged.connect(self.find)
                self.tbwGiangVien = QtWidgets.QTableWidget(parent=self.frmInfoBuoiHoc)
                self.tbwGiangVien.setEnabled(True)
                self.tbwGiangVien.setGeometry(QtCore.QRect(20, 110, 471, 341))
                self.tbwGiangVien.setShowGrid(True)
                self.tbwGiangVien.setGridStyle(QtCore.Qt.PenStyle.SolidLine)
                self.tbwGiangVien.setObjectName("tbwGiangVien")
                self.tbwGiangVien.setColumnCount(4)
                self.tbwGiangVien.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.tbwGiangVien.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.tbwGiangVien.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.tbwGiangVien.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.tbwGiangVien.setHorizontalHeaderItem(3, item)
                self.tbwGiangVien.setEditTriggers(QtWidgets.QTableWidget.EditTrigger.NoEditTriggers)
                self.tbwGiangVien.itemClicked.connect(self.getDataRow) 
                self.frame = QtWidgets.QFrame(parent=self.centralwidget)
                self.frame.setGeometry(QtCore.QRect(-1, -1, 801, 31))
                self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
                self.frame.setObjectName("frame")
                self.btnClose = QtWidgets.QPushButton(parent=self.frame)
                self.btnClose.setGeometry(QtCore.QRect(777, 4, 24, 24))
                self.btnClose.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
                self.btnClose.setText("")
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("../image/icon/close_50px.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.btnClose.setIcon(icon)
                self.btnClose.setIconSize(QtCore.QSize(20, 20))
                self.btnClose.setObjectName("btnClose")
                self.btnMinimize = QtWidgets.QPushButton(parent=self.frame)
                self.btnMinimize.setGeometry(QtCore.QRect(752, 4, 24, 24))
                self.btnMinimize.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
                self.btnMinimize.setText("")
                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap("../image/icon/subtract_50px.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.btnMinimize.setIcon(icon1)
                self.btnMinimize.setIconSize(QtCore.QSize(20, 20))
                self.btnMinimize.setObjectName("btnMinimize")
                self.label_15 = QtWidgets.QLabel(parent=self.frame)
                self.label_15.setGeometry(QtCore.QRect(10, 2, 201, 26))
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.NoAntialias)
                self.label_15.setFont(font)
                self.label_15.setAcceptDrops(False)
                self.label_15.setToolTip("")
                self.label_15.setAutoFillBackground(False)
                self.label_15.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
                self.label_15.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
                self.label_15.setTextFormat(QtCore.Qt.TextFormat.AutoText)
                self.label_15.setScaledContents(False)
                self.label_15.setWordWrap(False)
                self.label_15.setIndent(-1)
                self.label_15.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse)
                self.label_15.setObjectName("label_15")
                self.frmHeader = QtWidgets.QFrame(parent=self.centralwidget)
                self.frmHeader.setGeometry(QtCore.QRect(0, 30, 851, 51))
                self.frmHeader.setAccessibleName("")
                self.frmHeader.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
                self.frmHeader.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
                self.frmHeader.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
                self.frmHeader.setLineWidth(1)
                self.frmHeader.setObjectName("frmHeader")
                self.label_3 = QtWidgets.QLabel(parent=self.frmHeader)
                self.label_3.setGeometry(QtCore.QRect(0, 0, 801, 51))
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(True)
                font.setWeight(75)
                self.label_3.setFont(font)
                self.label_3.setStyleSheet("#label_3\n"
        "{\n"
        "    font-weight:bold;\n"
        "}")
                self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.label_3.setObjectName("label_3")
                self.btnBack = QtWidgets.QPushButton(parent=self.frmHeader)
                self.btnBack.setGeometry(QtCore.QRect(730, 12, 61, 23))
                self.btnBack.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
                self.btnBack.setObjectName("btnBack")
                self.label_2 = QtWidgets.QLabel(parent=self.frmHeader)
                self.label_2.setGeometry(QtCore.QRect(50, 10, 91, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.NoAntialias)
                self.label_2.setFont(font)
                self.label_2.setAcceptDrops(False)
                self.label_2.setToolTip("")
                self.label_2.setAutoFillBackground(False)
                self.label_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
                self.label_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
                self.label_2.setTextFormat(QtCore.Qt.TextFormat.AutoText)
                self.label_2.setScaledContents(False)
                self.label_2.setWordWrap(False)
                self.label_2.setIndent(-1)
                self.label_2.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse)
                self.label_2.setObjectName("label_2")
                self.label_4 = QtWidgets.QLabel(parent=self.frmHeader)
                self.label_4.setGeometry(QtCore.QRect(50, 30, 91, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_4.setFont(font)
                self.label_4.setObjectName("label_4")
                self.btnDark = QtWidgets.QPushButton(parent=self.frmHeader)
                self.btnDark.setGeometry(QtCore.QRect(680, 8, 31, 31))
                self.btnDark.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
                self.btnDark.setText("")
                icon2 = QtGui.QIcon()
                icon2.addPixmap(QtGui.QPixmap("../image/icon/moon_symbol_50px.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.btnDark.setIcon(icon2)
                self.btnDark.setIconSize(QtCore.QSize(20, 20))
                self.btnDark.setObjectName("btnDark")
                self.btnTime = QtWidgets.QPushButton(parent=self.frmHeader)
                self.btnTime.setGeometry(QtCore.QRect(10, 10, 31, 31))
                self.btnTime.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
                self.btnTime.setStyleSheet("#btnTime\n"
        "{\n"
        "background-color: transparent;\n"
        "}")
                self.btnTime.setText("")
                icon3 = QtGui.QIcon()
                icon3.addPixmap(QtGui.QPixmap("../image/icon/time_50px.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.btnTime.setIcon(icon3)
                self.btnTime.setIconSize(QtCore.QSize(20, 20))
                self.btnTime.setObjectName("btnTime")
                self.label_3.raise_()
                self.btnBack.raise_()
                self.label_4.raise_()
                self.label_2.raise_()
                self.btnDark.raise_()
                self.btnTime.raise_()
                MainWindow.setCentralWidget(self.centralwidget)

                self.loadListCmbTaiKhoan()
                self.loadDataQTable()
                self.retranslateUi(MainWindow)
                # tạo timer
                self.timer = QtCore.QTimer()
                self.timer.timeout.connect(self.clock_number)
                # start and update every second
                self.timer.start(1000)
                self.clock_number()
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.label_5.setText(_translate("MainWindow", "THÔNG TIN GIẢNG VIÊN"))
                self.label_11.setText(_translate("MainWindow", "Họ tên"))
                self.label_12.setText(_translate("MainWindow", "Số điện thoại"))
                self.label_13.setText(_translate("MainWindow", "Tài khoản"))
                self.btnThem.setText(_translate("MainWindow", "Thêm"))
                self.btnSua.setText(_translate("MainWindow", "Sửa"))
                self.btnXoa.setText(_translate("MainWindow", "Xóa"))
                self.btnLamMoi.setText(_translate("MainWindow", "Làm mới"))
                self.label_17.setText(_translate("MainWindow", "Hệ thống tìm kiếm:"))
                self.label_18.setText(_translate("MainWindow", "Tìm kiếm theo:"))
                item = self.tbwGiangVien.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "ID giảng viên"))
                item = self.tbwGiangVien.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "Họ tên"))
                item = self.tbwGiangVien.horizontalHeaderItem(2)
                item.setText(_translate("MainWindow", "Số điện thoại"))
                item = self.tbwGiangVien.horizontalHeaderItem(3)
                item.setText(_translate("MainWindow", "Tài khoản"))
                self.label_15.setText(_translate("MainWindow", "Phần mềm điểm danh sinh viên"))
                self.label_3.setText(_translate("MainWindow", "Quản lý giảng viên"))
                self.btnBack.setText(_translate("MainWindow", "Trở về"))

        def loadListCmbTaiKhoan(self):
                tk = TaiKhoanBUS()
                list = tk.get()
                print("Danh sách tài khoản lấy được:", list)
                if list is not None:
                        for row in list:
                                print("Kiểm tra tài khoản:", row[0])  # In từng tài khoản đang kiểm tra
                                if tk.checkNotTaiKhoanAmin(mataikhoan=row[0]):
                                        self.cmbTaiKhoan.addItem(row[1], row[0])
                                        print("Thêm tài khoản vào combobox:", row[1])
        def loadDataQTable(self):                    
                gv = GiangVienBUS()
                list = gv.get()
                tablerow=0
                self.tbwGiangVien.setRowCount(list.__len__())
             
                if list is not None:
                        for row in list:
                                self.tbwGiangVien.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
                                self.tbwGiangVien.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                                self.tbwGiangVien.setItem(tablerow, 2, QtWidgets.QTableWidgetItem("0"+str(row[2])))
                                self.tbwGiangVien.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
                                
                                tablerow+=1
        
        def getDataRow(self):
                cr = self.tbwGiangVien.currentRow()
                self.ma = self.tbwGiangVien.item(cr,0).text()
                self.txtHoTen.setText(self.tbwGiangVien.item(cr,1).text())
                self.txtSoDienThoai.setText(self.tbwGiangVien.item(cr,2).text())
                 # LẤY TÊN TÀI KHOẢN SET COMBOBOX
                tkBUS = TaiKhoanBUS()
                dstentaikhoan = tkBUS.find('mataikhoan',self.tbwGiangVien.item(cr,3).text())
                if dstentaikhoan is not None:
                        for row in dstentaikhoan:
                                tentaikhoan = row[1]
                self.cmbTaiKhoan.setCurrentText(tentaikhoan)

        def clear(self):
                self.txtHoTen.clear()
                self.txtSoDienThoai.clear()
                self.cmbTaiKhoan.setCurrentIndex(0)

        def validate(self, gv:GiangVien, trangthai):        
                if gv._hoten == '' or gv._sodienthoai == '' or gv._mataikhoan == '':
                        QMessageBox.information(self.centralwidget,"Thông báo","Vui lòng nhập đầy đủ thông tin")
                        return False
                if check_error.check_phone(self, input = gv._sodienthoai) == False:
                        QMessageBox.information(self.centralwidget,"Thông báo","Vui lòng nhập số điện thoại đúng định dạng")
                        return False
                if GiangVienBUS.checkExistTaiKhoan(self, mataikhoan=gv._mataikhoan) == False and trangthai == "add":
                        QMessageBox.information(self.centralwidget,"Thông báo","Tài khoản đã được sử dụng")
                        return False
                if GiangVienBUS.checkSoDienThoaiTonTai(self, sodienthoai=gv._sodienthoai) == False:
                        QMessageBox.information(self.centralwidget,"Thông báo","Số điện thoại đã tồn tại")
                        return False
                return True
        
        def add(self):
                gvBUS = GiangVienBUS()
                magiangvien = gvBUS.generateID()
                hoten = self.txtHoTen.text()
                sodienthoai = self.txtSoDienThoai.text()
                taikhoan = self.cmbTaiKhoan.currentData()                                        
                gv = GiangVien(magiangvien, hoten, sodienthoai, taikhoan)
                if self.validate(gv=gv, trangthai="add"):
                        if(gvBUS.add(gv)):
                                QMessageBox.information(self.centralwidget,"Thông báo","Thêm thành công")
                                self.loadDataQTable()
                                self.clear()
                        else:
                                QMessageBox.information(self.centralwidget,"Thông báo","Thêm thất bại")

        def update(self):
                gvBUS = GiangVienBUS()
                magiangvien = self.ma
                hoten = self.txtHoTen.text()
                sodienthoai = self.txtSoDienThoai.text()
                taikhoan = self.cmbTaiKhoan.currentData()
                
                gv = GiangVien(magiangvien, hoten, sodienthoai, taikhoan)
                if self.validate(gv=gv, trangthai="update"):
                        if(gvBUS.update(gv)):
                                QMessageBox.information(self.centralwidget,"Thông báo","Cập nhật thành công")
                                self.loadDataQTable()
                        else:
                                QMessageBox.information(self.centralwidget,"Thông báo","Cập nhật thất bại")

        def delete(self):
                gvBUS = GiangVienBUS()
                if(gvBUS.delete(self.ma)):
                        QMessageBox.information(self.centralwidget,"Thông báo","Xóa thành công")
                        self.loadDataQTable()
                        self.clear()
                else:
                        QMessageBox.information(self.centralwidget,"Thông báo","Xóa thất bại")
        def find(self):
                gv = GiangVienBUS()
                key =  self.cmbOptionFind.currentData()
                value = self.txtFind.text()
                list = gv.find(key, value)
                tablerow=0
                self.tbwGiangVien.setRowCount(list.__len__())
                
                if list is not None:
                        for row in list:
                                self.tbwGiangVien.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
                                self.tbwGiangVien.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                                self.tbwGiangVien.setItem(tablerow, 2, QtWidgets.QTableWidgetItem("0"+str(row[2])))
                                self.tbwGiangVien.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
                                
                                tablerow+=1

        def clock_number(self):
                time = datetime.now()
                format_time = time.strftime("%H:%M:%S")
                self.label_2.setText(format_time)

                format_date = time.strftime("%d/%m/%Y")
                self.label_4.setText(format_date)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UI_QuanLyGiangVien()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
