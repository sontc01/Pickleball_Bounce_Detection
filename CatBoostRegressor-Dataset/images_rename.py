import os
import re

# Thư mục chứa ảnh
image_folder = "/home/songodric/Documents/2024.2/Internship_Techvico/Pickleball_VAR/bounding_detection/Pickleball-CatBoostRegressor-Dataset/images"

# Duyệt qua tất cả các file trong thư mục
for filename in os.listdir(image_folder):
    old_path = os.path.join(image_folder, filename)

    # Kiểm tra nếu file không phải là ảnh thì bỏ qua
    if not filename.lower().endswith((".jpg", ".png", ".jpeg")):
        continue

    # Tìm pattern của file ảnh cũ
    match = re.match(r"frame_(\d+)_([\dmsh]+)_png\.rf\..+\.jpg", filename)
    if match:
        frame_number = int(match.group(1))  # Lấy số frame
        timestamp = match.group(2)  # Lấy thời gian
        new_filename = f"frame_{frame_number:04d}_{timestamp}.jpg"
        
        # Đường dẫn mới
        new_path = os.path.join(image_folder, new_filename)

        # Đổi tên file
        os.rename(old_path, new_path)
        print(f"✅ Đã đổi: {filename} ➝ {new_filename}")

print("🎯 Hoàn thành đổi tên tất cả file ảnh trong thư mục!")
