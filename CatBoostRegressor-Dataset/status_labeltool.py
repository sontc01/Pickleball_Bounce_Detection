import os
import pandas as pd
import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk

# Cấu hình đường dẫn
IMAGE_FOLDER = "/home/songodric/Documents/2024.2/Internship_Techvico/Pickleball_VAR/bounding_detection/Pickleball-CatBoostRegressor-Dataset/images"
CSV_FILE = "/home/songodric/Documents/2024.2/Internship_Techvico/Pickleball_VAR/bounding_detection/Pickleball-CatBoostRegressor-Dataset/refine_labels/label_total.csv"

# Đọc file CSV
df = pd.read_csv(CSV_FILE)
file_names = df["file name"].tolist()
current_index = 0

# Hàm load ảnh
def load_image(index):
    global img_label, img_display, status_label

    if 0 <= index < len(file_names):
        file_name = file_names[index]
        img_path = os.path.join(IMAGE_FOLDER, file_name)

        # Lấy giá trị status tương ứng
        status = df.loc[df["file name"] == file_name, "status"].values[0]

        # Nếu file tồn tại, hiển thị ảnh
        if os.path.exists(img_path):
            image = Image.open(img_path)
            image = image.resize((1000, 1000))
            img_display = ImageTk.PhotoImage(image)
            img_label.config(image=img_display)
            img_label.image = img_display
            info_label.config(text=f"File: {file_name}\nIndex: {index+1}/{len(file_names)}")
            status_label.config(text=f"Status: {status}")
        else:
            info_label.config(text=f"File không tồn tại: {file_name}")
            status_label.config(text="Status: N/A")
    else:
        info_label.config(text="Hết danh sách ảnh!")
        status_label.config(text="Status: N/A")

def update_status(value, event=None):
    global current_index
    if current_index < 0 or current_index >= len(file_names):
        return  # Tránh lỗi truy cập ngoài phạm vi

    file_name = file_names[current_index]

    # Cập nhật giá trị trong dataframe
    df.loc[df["file name"] == file_name, "status"] = value

    # Lưu lại file CSV
    df.to_csv(CSV_FILE, index=False)

    # Cập nhật giao diện
    status_label.config(text=f"Status: {value}")

# Chuyển ảnh tiếp theo
def next_image(event=None):
    global current_index
    if current_index < len(file_names) - 1:
        current_index += 1
        load_image(current_index)

# Quay lại ảnh trước
def prev_image(event=None):
    global current_index
    if current_index > 0:
        current_index -= 1
        load_image(current_index)

def key_event(event):
    global current_index
    
    file_name = file_names[current_index]
    
    if event.keysym in ["Up", "Down"]:
        # Lấy giá trị status hiện tại
        current_status = df.loc[df["file name"] == file_name, "status"].values[0]
        
        if event.keysym == "Up":
            new_status = min(2, current_status + 1)  # Giới hạn tối đa 2
        elif event.keysym == "Down":
            new_status = max(0, current_status - 1)  # Giới hạn tối thiểu 0
        
        update_status(new_status)  # Cập nhật giá trị mới
    
    elif event.keysym == "Left":  
        prev_image()

    elif event.keysym == "Right":  
        next_image()

# Tạo giao diện
root = tk.Tk()
root.title("Image Viewer from CSV")
root.geometry("600x700")

# Label hiển thị ảnh
img_label = Label(root)
img_label.pack()

# Label hiển thị thông tin
info_label = Label(root, text="", font=("Arial", 12))
info_label.pack()

# Label hiển thị status
status_label = Label(root, text="Status: ", font=("Arial", 12, "bold"))
status_label.pack()

# Gán phím tắt
root.bind("<Up>", key_event)     # Tăng status
root.bind("<Down>", key_event)   # Giảm status
root.bind("<Right>", key_event)  # Chuyển ảnh tiếp theo
root.bind("<Left>", key_event)   # Quay lại ảnh trước

# Load ảnh đầu tiên
load_image(current_index)

# Chạy ứng dụng
root.mainloop()
