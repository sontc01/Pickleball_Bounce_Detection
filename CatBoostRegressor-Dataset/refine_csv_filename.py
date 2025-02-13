import re
import pandas as pd

# Đọc file CSV
csv_path = "org_labels/label_valid.csv"
df = pd.read_csv(csv_path)

def rename_image_file(filename):
    # Tách thông tin frame
    match = re.match(r"frame_(\d+)_([\dmsh]+)_png\.rf\..+\.jpg", filename)
    if match:
        frame_number = int(match.group(1))  # Lấy số frame
        timestamp = match.group(2)          # Lấy thời gian

        # Format số frame thành 4 chữ số
        new_filename = f"frame_{frame_number:04d}_{timestamp}.jpg"
        return new_filename
    return filename  # Trả về filename gốc nếu không khớp

# Áp dụng đổi tên vào cột "file name"
df["file name"] = df["file name"].apply(rename_image_file)

# Hàm chuyển đổi giá trị về int hoặc giữ trống nếu cần
def convert_to_int(value):
    try:
        value = int(float(value))  # Đảm bảo giá trị là int
        return value if value != 0 else ""  # Nếu là 0 thì để trống
    except ValueError:
        return ""  # Giữ trống nếu không hợp lệ

# Chuyển đổi x-coordinate, y-coordinate, status về int hoặc trống
for col in ["x-coordinate", "y-coordinate", "status"]:
    df[col] = df[col].apply(convert_to_int)

# Lưu lại file CSV đã sửa
output_path = "refine_labels/label_valid.csv"
df.to_csv(output_path, index=False)

print(f"✅ File mới đã lưu tại: {output_path}")
