# Step 1: Data Preparation
**Using OpenCV to trim the video into frames in numerical order and time stamps.** 
###
The developer (aka. me) merge the video of single player match and the video of couple player match into 1 video to easily naming the frames with the mean density is 5 frames per second (FPS).
- Prepare the pickleball video
- Change the "video_path" and "output_folder" filepath
- Run "python3 frames_gen.py" in terminal    


# Step 2: Auto label using YOLO
**Using trained YOLO model (yolopickleball.pt) to auto label the ball in frames.** 
### 
The developer using a trained YOLO model in another pickleball dataset, predict bounding boxes in these frames and keep only the box have highest confidence score.
- Install Ultrlytics library
- Change the "model", "input_folder", "output_folder" filepath
- Run "python3 yolo_detect.py" in terminal

# Step 3: Refine the Bounding Boxes Annotations using Roboflow
**Using Roboflow to visualize and refine the bounding boxes to best accuracy.** 

# Step 4: Create Categories Dataset for CatBoostRegressor model
**Using the videos and frames to label the .csv file consist of 5 categories: "file name", "visibility", "x-coordinate", "y-coordinate", "status".** 
### 
The developer using the videos to check when the ball is flying, hitting or bounding (0,1,2) and when the ball is visibility with 4 VC (Visibility Class).
