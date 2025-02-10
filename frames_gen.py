import cv2
import os

interval = 25/5 # FPS/N => N frames per second!

def extract_frames_with_timestamp(video_path, output_folder, frame_interval=interval):
    """Trim the video and save as frames in numerical order and time stamps."""
    os.makedirs(output_folder, exist_ok=True)
    
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))  # Get the FPS
    frame_index = 0

    if not cap.isOpened():
        print("Error: Cannot open video file. Recheck the filepath and file format.")
    else:
        print("Video open successfully!")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Take the time stamps
        total_seconds = frame_index / fps
        minutes = int(total_seconds // 60)
        seconds = int(total_seconds % 60)

        # Save the frames in numerical order and time stamps.
        if frame_index % frame_interval == 0:
            frame_filename = os.path.join(output_folder, f"frame_{int(frame_index/interval)}_{minutes:02d}m{seconds:02d}s.png")
            cv2.imwrite(frame_filename, frame)

        frame_index += 1

    cap.release()
    print(f"Trimmed {frame_index/interval} frames from video!")

# Main program
video_path = "double-export.mp4"
output_folder = "frames-double-export"

extract_frames_with_timestamp(video_path, output_folder, frame_interval=interval)  
