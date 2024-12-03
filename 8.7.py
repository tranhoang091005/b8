print("TRẦN DANH HOÀNG")
print("MSSV:235752021610064")

import tkinter
import random

# Danh sách các màu có thể có
colours = ['Red','Blue','Green','Pink','Black', 
           'Yellow','Orange','White','Purple','Brown']  
score = 0

# Thời gian chơi ban đầu là 120 giây
timeleft = 120

# Hàm bắt đầu trò chơi khi nhấn Enter
def startGame(event):  
    if timeleft == 120:  # Bắt đầu đếm ngược khi lần đầu chơi
        countdown()  # Bắt đầu đếm ngược
    nextColour()  # Chọn màu tiếp theo

# Hàm chọn màu tiếp theo
def nextColour():  
    global score
    global timeleft

    # Nếu thời gian trò chơi còn lại
    if timeleft > 0:
        e.focus_set()  # Làm cho ô nhập liệu có thể nhận input

        # Kiểm tra nếu người chơi nhập đúng màu (chú ý phân biệt chữ hoa và chữ thường)
        if e.get().lower() == colours[1].lower():  
            score += 2  # Tăng điểm khi đoán đúng

        else:
            score -= 1  # Giảm điểm khi đoán sai

        e.delete(0, tkinter.END)  # Xóa ô nhập liệu

        random.shuffle(colours)  # Xáo trộn danh sách màu

        # Cập nhật màu và tên màu
        label.config(fg = str(colours[1]), text = str(colours[0]))

        # Cập nhật điểm số
        scoreLabel.config(text = "Score: " + str(score))

# Hàm đếm ngược thời gian
def countdown():  
    global timeleft

    # Nếu thời gian còn lại
    if timeleft > 0:
        timeleft -= 1  # Giảm 1 giây
        timeLabel.config(text = "Time left: " + str(timeleft))  # Cập nhật thời gian

        # Gọi lại hàm countdown sau 1 giây
        timeLabel.after(1000, countdown)

# Tạo cửa sổ GUI
root = tkinter.Tk()

# Tiêu đề cửa sổ
root.title("COLORGAME")

# Kích thước cửa sổ
root.geometry("375x300")

# Thêm hướng dẫn cho người chơi
instructions = tkinter.Label(root, text = "Type in the colour of the words, and not the word text!",
                             font = ('Helvetica', 12))
instructions.pack()

# Thêm nhãn điểm
scoreLabel = tkinter.Label(root, text = "Press enter to start", font = ('Helvetica', 12))
scoreLabel.pack()

# Thêm nhãn thời gian
timeLabel = tkinter.Label(root, text = "Time left: " + str(timeleft), font = ('Helvetica', 12))
timeLabel.pack()

# Thêm nhãn hiển thị màu sắc
label = tkinter.Label(root, font = ('Helvetica', 60))
label.pack()

# Thêm ô nhập liệu cho người chơi nhập màu
e = tkinter.Entry(root)

# Kết nối sự kiện nhấn Enter để bắt đầu trò chơi
root.bind('<Return>', startGame)

e.pack()

# Đặt focus vào ô nhập liệu
e.focus_set()

# Chạy ứng dụng GUI
root.mainloop()
