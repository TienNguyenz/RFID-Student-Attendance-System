import cv2
import numpy as np
import os
from pyzbar.pyzbar import decode
import pandas as pd  # Import pandas for Excel writing

mssv_list = []  # Global list to store detected MSSVs
detected_images = []

EXCEL_FILE = r"D:\Study\Nam4\Python\OpenCV\Doan\ProjectPython-FaceID-main\DiemDanhSuKien\Recources\DD.xlsx"


def resize_image(image, width=800):
    """ Resize image to a manageable size while keeping aspect ratio """
    height, original_width = image.shape[:2]
    if original_width > width:
        scale = width / original_width
        new_height = int(height * scale)
        resized_image = cv2.resize(image, (width, new_height))
        return resized_image
    return image

def detect_barcode(image):
    """ Detect and decode barcode in the image """
    barcodes = decode(image)
    for barcode in barcodes:
        barcode_data = barcode.data.decode("utf-8")
        if barcode_data.isdigit():
            return barcode_data
    return None

def display_mssv_list():
    """ Display the list of detected MSSVs """
    global mssv_list
    if not mssv_list:
        return "No MSSVs detected yet."
    return "\n".join(mssv_list)

def append_mssv_to_excel(mssv):
    """ Append a single MSSV to the Excel file """
    try:
        df = pd.read_excel(EXCEL_FILE, header=None)  # Đọc file Excel không tiêu đề
    except ValueError:
        df = pd.DataFrame()  # Tạo DataFrame nếu file rỗng

    if not df.empty and mssv in df[0].values:  # Kiểm tra cột đầu tiên
        print(f"MSSV {mssv} already exists in Excel.")
    else:
        new_row = pd.DataFrame([[mssv]])  # Thêm MSSV vào DataFrame
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False, header=False)
        print(f"MSSV {mssv} appended to Excel.")

def rename_image(image_path, detected_mssv):
    """ Rename the image file based on the detected MSSV, if not already existing """
    directory, original_name = os.path.split(image_path)
    new_name = f"{detected_mssv}.jpg"
    new_path = os.path.join(directory, new_name)

    print(f"Attempting to rename {image_path} to {new_path}")
    try:
        if not os.path.exists(new_path):
            os.rename(image_path, new_path)
            print(f"Renamed {original_name} to {new_name}")
        else:
            print(f"File {new_name} already exists. Skipping rename.")
    except PermissionError as e:
        print(f"Permission denied while renaming {original_name} to {new_name}: {e}")
    except FileNotFoundError as e:
        print(f"File not found: {image_path}: {e}")
    except Exception as e:
        print(f"Unexpected error while renaming {original_name} to {new_name}: {e}")



def process_image(image_path):
    global mssv_list
    image = cv2.imread(image_path)
    if image is None:
        print(f"Unable to load the image: {image_path}")
        return

    resized_image = resize_image(image)
    detected_mssv = detect_barcode(resized_image)
    if detected_mssv:
        print(f"Detected MSSV (Barcode): {detected_mssv}")
        mssv_list.append(detected_mssv)
        append_mssv_to_excel(detected_mssv)
        rename_image(image_path, detected_mssv)
        return True
    else:
        print("No barcode detected.")
        return False

def process_all_images(directory):
        global detected_images
        if not os.path.exists(directory):
            print("The specified directory does not exist.")
            print(directory)
            return

        detected_images = [os.path.join(directory, f) for f in os.listdir(directory) if
                           f.endswith(".jpg") or f.endswith(".png")]

        total_images = len(detected_images)
        success_count = 0
        fail_count = 0

        for index, image_path in enumerate(detected_images):
            print(f"Processing image {index + 1}/{total_images}: {image_path}")
            if process_image(image_path) == True:
                success_count += 1
            else:
                fail_count += 1

        summary_message = (
            f"Tổng số thẻ đã quét: {total_images}\n"
            f"Số thẻ quét thành công: {success_count}\n"
            f"Số thẻ không quét được: {fail_count}\n\n"
        )

        return total_images, success_count, fail_count

if __name__ == "__main__":
        directory = "C:/Users/hvu31/Downloads/ProjectPython-FaceID-main/DiemDanhSuKien/Recources/img"
        result = process_all_images(directory)
        print(result)
        if result is not None:
            total_images, success_count, fail_count = result
            print(f"Tổng số thẻ đã quét: {total_images}")
            print(f"Số thẻ quét thành công: {success_count}")
            print(f"Số thẻ không quét được: {fail_count}")
        else:
            print("Không có kết quả nào được trả về.")