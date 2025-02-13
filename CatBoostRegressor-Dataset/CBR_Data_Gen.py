import os
import glob
import pandas as pd

# Đường dẫn thư mục chứa ảnh và label YOLO
image_folder = "/home/songodric/Documents/2024.2/Internship_Techvico/Pickleball_VAR/bounding_detection/SonTC-Ball-Detection-Refine.v3i.yolov8/test/images"  # Thay bằng đường dẫn chứa ảnh
label_folder = "/home/songodric/Documents/2024.2/Internship_Techvico/Pickleball_VAR/bounding_detection/SonTC-Ball-Detection-Refine.v3i.yolov8/test/labels"  # Thay bằng đường dẫn chứa labels YOLO
output_csv = "label_test.csv"  # Đường dẫn lưu file CSV

# Danh sách ảnh trong dataset
image_files = sorted(glob.glob(os.path.join(image_folder, "*.jpg")))

# Danh sách chứa dữ liệu
data = []

for image_path in image_files:
    filename = os.path.basename(image_path)  # Lấy tên file ảnh (VD: 0001.jpg)
    label_path = os.path.join(label_folder, filename.replace(".jpg", ".txt"))  # Đường dẫn file label

    # Mặc định không có bóng
    visibility = 0
    x_pixel, y_pixel, status = "", "", ""  # Để trống khi visibility = 0

    # Nếu file label tồn tại, đọc bounding box
    if os.path.exists(label_path):
        with open(label_path, "r") as f:
            lines = f.readlines()
            if len(lines) > 0:  # Có ít nhất 1 bounding box
                visibility = 1
                # Lấy bounding box đầu tiên
                class_id, x_center, y_center, width, height = map(float, lines[0].split())

                # Chuyển tọa độ từ YOLO format về pixel
                img_width, img_height = 1280, 720  # Cập nhật theo kích thước ảnh của bạn
                x_pixel = int(x_center * img_width)
                y_pixel = int(y_center * img_height)
                status = 0  # Mặc định status = 0 khi có bóng

    # Thêm dữ liệu vào danh sách
    data.append([filename, visibility, x_pixel, y_pixel, status])

# Lưu thành CSV
df = pd.DataFrame(data, columns=["file name", "visibility", "x-coordinate", "y-coordinate", "status"])
df.to_csv(output_csv, index=False)

print(f"✅ Hoàn tất! File CSV lưu tại: {output_csv}")
