from ultralytics import YOLO
import cv2
import os

# Load weight file
model = YOLO("../yolo_detect/yolopickerball.pt")  # Paste the weight path

# Paste the frames path
input_folder = "/home/songodric/Documents/2024.2/Internship_Techvico/Pickleball_VAR/bounding_detection/dataset_preparation/frames-pickleball-export"
output_folder = "labeled_frames-pickleball-export"
os.makedirs(output_folder, exist_ok=True)

# Scan each image in the folder
for img_file in os.listdir(input_folder):
    img_path = os.path.join(input_folder, img_file)
    results = model(img_path)
    
    img = cv2.imread(img_path)
    h, w, _ = img.shape  # Take the image size

    best_box = None
    best_conf = 0  # Best confidence score

    for result in results:
        for box, conf in zip(result.boxes.xyxy, result.boxes.conf):  # Take bounding box + confidence score
            x1, y1, x2, y2 = map(int, box[:4])
            conf = float(conf)  # Convert confidence into float
            
            if conf > best_conf:  # Check the confidence score
                best_box = (x1, y1, x2, y2)
                best_conf = conf

    
    label_file = os.path.join(output_folder, img_file.replace(".png", ".txt"))  # Create the .txt file
    
    with open(label_file, "w") as f:
        if best_box:
            x1, y1, x2, y2 = map(int, box[:4])
                    
            # Change the coordinates (x1, y1, x2, y2) into format YOLO (cx, cy, w, h)
            cx = (x1 + x2) / 2 / w
            cy = (y1 + y2) / 2 / h
            bw = (x2 - x1) / w
            bh = (y2 - y1) / h
                    
            # Save into format YOLO: class_id cx cy w h
            f.write(f"0 {cx:.6f} {cy:.6f} {bw:.6f} {bh:.6f}\n")

print("Complete create bounding box for pickleball frames!")
