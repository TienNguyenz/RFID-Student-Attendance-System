import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class MainView:
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("Student Card Processing")
        self.root.geometry("500x400")
        self.root.configure(bg="#1e1e2f")
        self.result_text = tk.StringVar()

        # Header
        header_frame = tk.Frame(self.root, bg="#2e2e40", relief=tk.RAISED, bd=2)
        header_frame.pack(fill=tk.X, pady=10)
        tk.Label(
            header_frame,
            text="Điểm danh sự kiện",
            font=("Arial", 20, "bold"),
            fg="white",
            bg="#2e2e40"
        ).pack(pady=10)

        # Body
        body_frame = tk.Frame(self.root, bg="#1e1e2f")
        body_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        # MSSV Reader Label
        tk.Label(
            body_frame,
            text="Quét thẻ",
            font=("Arial", 14, "bold"),
            fg="white",
            bg="#1e1e2f"
        ).pack(pady=10)

        # Process Button
        self.process_button = tk.Button(
            body_frame,
            text="Bắt đầu quét",
            command=self.run_process,
            font=("Arial", 12, "bold"),
            bg="#0078D7",
            fg="white",
            activebackground="#005BB5",
            activeforeground="white",
            relief=tk.RAISED,
            bd=3,
            padx=10,
            pady=5
        )
        self.process_button.pack(pady=10)

        # Result Text Area
        result_frame = tk.Frame(body_frame, bg="#1e1e2f")
        result_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        self.result_label = tk.Text(
            result_frame,
            height=10,
            wrap=tk.WORD,
            bg="#2e2e40",
            fg="white",
            font=("Arial", 12),
            state=tk.DISABLED
        )
        self.result_label.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Footer
        footer_frame = tk.Frame(self.root, bg="#2e2e40", relief=tk.RAISED, bd=2)
        footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
        tk.Label(
            footer_frame,
            text="Developed by [Your Name]",
            font=("Arial", 10),
            fg="white",
            bg="#2e2e40"
        ).pack(pady=5)

    def show_result_dialog(self, title, total_images, success_count,fail_count):
        # Tạo cửa sổ con
        dialog = tk.Toplevel(self.root)
        dialog.title(title)
        dialog.geometry("600x400")  # Thiết lập kích thước cửa sổ
        dialog.configure(bg="#1e1e2f")

        # Tiêu đề
        tk.Label(
            dialog,
            text=title,
            font=("Arial", 16, "bold"),
            fg="white",
            bg="#2e2e40"
        ).pack(pady=10)

        # Vùng hiển thị nội dung
        text_area = tk.Text(
            dialog,wrap=tk.WORD,
            bg="#2e2e40",
            fg="white",
            font=("Arial", 12)
        )
        message=(
        f"Tổng số thẻ đã quét: {total_images}\n"
        f"Số thẻ quét thành công: {success_count}\n"
        f"Số thẻ không quét được: {fail_count}\n\n"
    )
        text_area.insert(tk.END, message)
        text_area.configure(state=tk.DISABLED)  # Chỉ đọc
        text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Nút đóng
        tk.Button(
            dialog,
            text="Đóng",
            command=dialog.destroy,
            font=("Arial", 12, "bold"),
            bg="#0078D7",
            fg="white"
        ).pack(pady=10)

    def run_process(self):
        try:
            # Gọi phương thức và nhận kết quả
            total_cards, success_count, fail_count = self.controller.process_images()

            # Cấu trúc lại chuỗi hiển thị kết quả
            result_summary = (
                f"Tổng số thẻ đã quét: {total_cards}\n"
                f"Số thẻ quét thành công: {success_count}\n"
                f"Số thẻ không quét được: {fail_count}"
            )

            # Hiển thị danh sách MSSV trong giao diện
            result_text = self.controller.get_mssv_list()
            self.result_label.configure(state=tk.NORMAL)
            self.result_label.delete("1.0", tk.END)
            self.result_label.insert(tk.END, result_text)
            self.result_label.configure(state=tk.DISABLED)

            # Hiển thị hộp thoại kết quả
            self.show_result_dialog("Kết quả quét thẻ", total_cards,success_count,fail_count)

        except Exception as e:
            # Hiển thị thông báo lỗi nếu xảy ra
            messagebox.showerror("Error", str(e))

    def show(self):
        self.root.mainloop()