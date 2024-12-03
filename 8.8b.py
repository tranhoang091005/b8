print("TRẦN DANH HOÀNG")
print("MSSV:235752021610064")

import tkinter as tk

# Hàm xử lý khi nhấn nút "Click Me"
def show_choice():
    choice = var.get()  # Lấy giá trị lựa chọn từ radio button
    result_label.config(text=f"Bạn chọn: {choice}")  # Cập nhật label với lựa chọn

root = tk.Tk()
root.title("Chọn lựa")

# Khai báo biến StringVar để lưu giá trị của các radio button
var = tk.StringVar()

# Tạo các radio button
radio1 = tk.Radiobutton(root, text="Option 1", variable=var, value="1")
radio1.grid(row=0, column=0, padx=10, pady=10)

radio2 = tk.Radiobutton(root, text="Option 2", variable=var, value="2")
radio2.grid(row=1, column=0, padx=10, pady=10)

radio3 = tk.Radiobutton(root, text="Option 3", variable=var, value="3")
radio3.grid(row=2, column=0, padx=10, pady=10)

# Nút "Click Me" để hiển thị lựa chọn
button_click = tk.Button(root, text="Click Me", command=show_choice)
button_click.grid(row=3, column=0, pady=10)

# Label để hiển thị kết quả lựa chọn
result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, pady=10)

root.mainloop()
