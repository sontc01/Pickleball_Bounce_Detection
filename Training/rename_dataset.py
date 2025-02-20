import pandas as pd

# Đọc file CSV
data = pd.read_csv('/home/songodric/Documents/2024.2/Internship_Techvico/Pickleball_VAR/bounding_detection/Pickleball-CatBoostRegressor-Dataset/refine_labels/label_total.csv')  # Thay thế bằng đường dẫn thực tế đến file CSV của bạn

# Hàm để tách và chuyển đổi giá trị từ 'file name'
def extract_info(file_name):
    # Tách tên file dựa trên dấu gạch dưới
    parts = file_name.split('_')
    # Lấy giá trị '0031' từ phần thứ hai
    file_num = parts[1]
    # Lấy '00m06s' và tách '0006'
    time_stamp = parts[2].replace('m', '').replace('s.jpg', '')
    return pd.Series([file_num, time_stamp])

# Áp dụng hàm để tạo hai cột mới
data[['file name', 'time stamp']] = data['file name'].apply(extract_info)

# Lưu lại file CSV mới với hai cột đã tách
data.to_csv('/home/songodric/Documents/2024.2/Internship_Techvico/Pickleball_VAR/bounding_detection/Pickleball-CatBoostRegressor-Dataset/refine_labels/label_total_training_test.csv', index=False)  # Thay thế bằng đường dẫn thực tế bạn muốn lưu file

# Hiển thị dataframe đã chuyển đổi
print(data)
