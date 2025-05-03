import os
from tkinter import font

import cv2
import numpy as np
import time
from PyQt6.QtCore import QThread, pyqtSignal, Qt
from PyQt6.QtGui import QPixmap
from pyqt6_plugins.examplebuttonplugin import QtGui
from pyzbar.pyzbar import decode  # Thêm import pyzbar để quét mã vạch
from .SinhVienBUS import SinhVienBUS


class face_recognition(QThread):  # Đổi tên class thành barcode_recognition
    signal = pyqtSignal(np.ndarray)
    cap = None
    masinhvien_save = ''
    Id = ''
    image = ''
    link_image = ''
    cv_img_cur = np.array([0])

    def __init__(self, index):
        self.index = index
        super(face_recognition, self).__init__()



    def run(self):
        self.arr_ID = []
        print("Debug: Bắt đầu khởi động camera...")  # Debug bước khởi động camera
        cap = cv2.VideoCapture(1)
        self.cap = cap

        if not cap.isOpened():
            print("Lỗi: Không thể mở camera!")  # Debug nếu không mở được camera
            return

        print("Debug: Camera đã khởi động thành công.")

        try:
            while True:
                ret, cv_img = cap.read()
                if not ret:
                    print("Lỗi: Không thể đọc khung hình từ camera!")  # Debug lỗi đọc khung hình
                    break

                print("Debug: Đọc khung hình từ camera thành công.")
                print(f"Debug: Kích thước ảnh từ camera: {cv_img.shape}")

                # Quét mã vạch từ khung hình
                decoded_objects = decode(cv_img)
                if not decoded_objects:
                    print("Debug: Không có mã vạch nào được nhận diện.")
                else:
                    for obj in decoded_objects:
                        # Đọc dữ liệu mã vạch
                        barcode_data = obj.data.decode("utf-8")
                        print(f"Debug: Mã vạch nhận diện: {barcode_data}")
                        self.masinhvien_save = "SV" + barcode_data  # Lưu mã sinh viên từ mã vạch

                        # Tìm thông tin sinh viên dựa trên mã vạch
                        ten = ''
                        sv = SinhVienBUS()
                        list = sv.findMaSinhVien(self.masinhvien_save)
                        if list is not None:
                            for row in list:
                                ten = row[1]
                        print(f"Debug: Tên sinh viên: {ten}, Mã sinh viên: {self.masinhvien_save}")

                        # Lưu hình ảnh khi nhận diện mã vạch
                        t = time.localtime()
                        current_time = time.strftime("%H_%M_%S", t)
                        file_name = f"SV{self.masinhvien_save}_{current_time}.jpg"
                        self.link_image = f"../image/diemdanh/{file_name}"
                        cv2.imwrite(self.link_image, cv_img)
                        print(f"Debug: Đã lưu hình ảnh tại {self.link_image}")

                        # Hiển thị mã vạch trên khung hình
                        (x, y, w, h) = obj.rect
                        cv2.rectangle(cv_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        font = cv2.FONT_HERSHEY_SIMPLEX
                        cv2.putText(cv_img, f"{self.masinhvien_save}", (x, y - 10), font, 0.5, (255, 255, 255), 2)

                # Gửi tín hiệu hình ảnh để hiển thị
                if ret:
                    self.signal.emit(cv_img)

        except Exception as e:
            print(f"Lỗi không mong muốn: {e}")
        finally:
            print("Debug: Đóng camera.")
            cap.release()

    def stop(self):
        if self.cap is not None:
            self.cap.release()

        self.cap = None

    def getIDSV(self):
        return self.masinhvien_save

    def getCv_Image_Cur(self):
        return self.cv_img_cur

    def getLink_Image(self):
        return self.link_image

