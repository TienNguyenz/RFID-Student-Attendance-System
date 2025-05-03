import cv2
import numpy as np
from pyzbar.pyzbar import decode
from PyQt6.QtCore import QThread, pyqtSignal, Qt
from PyQt6.QtWidgets import QMessageBox
from DAL.HinhAnhSV import HinhAnhSV
from BUS.HinhAnhSVBUS import HinhAnhSVBUS
from DAL.SinhVienDAL import SinhVienDAL


class face_dataset(QThread):
    signal = pyqtSignal(np.ndarray)
    cap = None


    def __init__(self, index, id):
        self.index = 1
        self.idSV = id
        super(face_dataset, self).__init__()

    def generateID(self, barcode_data):
        """
        Hàm tạo mã sinh viên từ mã vạch quét được.
        """
        ma = "SV" + barcode_data  # Dùng mã vạch quét được để tạo mã sinh viên
        return ma

    def updateMSSV(self, old_mssv, new_mssv):
        try:
            # Gọi hàm trong SinhVienDAL để thực hiện cập nhật
            return SinhVienDAL.updateMSSV(old_mssv, new_mssv)
        except Exception as e:
            print(f"Lỗi khi cập nhật MSSV: {e}")

    def run(self):
        # Sử dụng camera mặc định
        cam = cv2.VideoCapture(self.index)

        count = 0
        hsBUS = HinhAnhSVBUS()
        hsBUS.delete(self.idSV)  # Xóa ảnh sinh viên trong database

        while True:
            ret, img = cam.read()
            img = cv2.flip(img, 1)  # Lật video theo chiều dọc

            # Quét barcode trong ảnh
            barcodes = decode(img)
            for barcode in barcodes:
                barcode_data = barcode.data.decode("utf-8")
                print(f"Đã phát hiện barcode: {barcode_data}")

                # Lấy mã sinh viên từ barcode và tạo ID
                mssv = self.generateID(barcode_data)  # Sử dụng mã quét được để tạo mã sinh viên

                # Cập nhật MSSV vào cơ sở dữ liệu nếu đã có sinh viên cũ
                old_mssv = self.idSV  # MSSV cũ
                new_mssv= "SV" + barcode_data
                self.updateMSSV(old_mssv, new_mssv)

                # Lưu MSSV vào Excel hoặc Database
                # Bạn có thể thêm logic lưu vào database hoặc Excel ở đây

                # Vẽ hộp xung quanh barcode
                rect_points = barcode.polygon
                if len(rect_points) == 4:
                    pts = np.array(rect_points, dtype=np.int32)
                    pts = pts.reshape((-1, 1, 2))
                    cv2.polylines(img, [pts], True, (0, 0, 255), 5)
                else:
                    # Nếu barcode không có 4 góc, vẽ hình chữ nhật
                    cv2.rectangle(img, (barcode.rect.left, barcode.rect.top),
                                  (barcode.rect.left + barcode.rect.width,
                                   barcode.rect.top + barcode.rect.height), (0, 0, 255), 2)

                # Đặt tên ảnh hoặc lưu ảnh theo barcode nếu cần
                count += 1
                nameFile = f'../image/photo/{mssv}-barcode{count}.jpg'  # Sử dụng MSSV làm tên ảnh
                cv2.imwrite(nameFile, img)

            if ret:
                self.signal.emit(img)

            # Dừng quá trình sau khi quét barcode thành công
            if count >= 5:  # Đảm bảo chỉ chụp một số lượng ảnh nhất định
                arr = np.array([0])
                self.signal.emit(arr)
                break

        cam.release()