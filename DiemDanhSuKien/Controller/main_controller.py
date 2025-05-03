
from DiemDanhSuKien.model.image_processing import process_all_images, display_mssv_list

from DiemDanhSuKien.view.main_view import MainView


class MainController:
    def __init__(self):
        self.view = MainView(self)

    def run(self):
        self.view.show()

    def process_images(self):
        return process_all_images(r"D:\Study\Nam4\Python\OpenCV\Doan\ProjectPython-FaceID-main\DiemDanhSuKien\Recources\img")

    def get_mssv_list(self):
        return display_mssv_list()


