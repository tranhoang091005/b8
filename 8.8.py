print("TRẦN DANH HOÀNG")
print("MSSV:235752021610064")

import tkinter as tk

# Hàm để hiển thị thông tin khi nhấn nút "Hiển thị"
def display_info():
    name = name_entry.get()
    dob = dob_entry.get()
    mssv = mssv_entry.get()
    major = major_entry.get()

    # Cập nhật nội dung nhãn thông tin với các giá trị người dùng nhập vào
    info_label.config(text=f"Họ và Tên: {name}\nNgày Sinh: {dob}\nMSSV: {mssv}\nNgành Học: {major}")

# Tạo cửa sổ GUI
root = tk.Tk()

# Tiêu đề cửa sổ
root.title("Thông Tin Cá Nhân")

# Kích thước cửa sổ
root.geometry("400x300")

# Tạo nhãn cho form
label_name = tk.Label(root, text="Họ và Tên:")
label_name.grid(row=0, column=0, padx=10, pady=10, sticky="w")

label_dob = tk.Label(root, text="Ngày Sinh (DD/MM/YYYY):")
label_dob.grid(row=1, column=0, padx=10, pady=10, sticky="w")

label_mssv = tk.Label(root, text="MSSV:")
label_mssv.grid(row=2, column=0, padx=10, pady=10, sticky="w")

label_major = tk.Label(root, text="Ngành Học:")
label_major.grid(row=3, column=0, padx=10, pady=10, sticky="w")

# Tạo các ô nhập liệu
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

dob_entry = tk.Entry(root)
dob_entry.grid(row=1, column=1, padx=10, pady=10)

mssv_entry = tk.Entry(root)
mssv_entry.grid(row=2, column=1, padx=10, pady=10)

major_entry = tk.Entry(root)
major_entry.grid(row=3, column=1, padx=10, pady=10)

# Tạo nút để hiển thị thông tin
display_button = tk.Button(root, text="Hiển thị", command=display_info)
display_button.grid(row=4, column=0, columnspan=2, pady=10)

# Nhãn để hiển thị thông tin đã nhập
info_label = tk.Label(root, text="", font=("Helvetica", 12))
info_label.grid(row=5, column=0, columnspan=2, pady=10)

# Chạy ứng dụng GUI
root.mainloop()
