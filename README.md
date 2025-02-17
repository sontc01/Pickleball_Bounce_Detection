# Step 1.1: Data Preparation
**Using OpenCV to trim the video into frames in numerical order and time stamps.** 
###
The developer (aka. me) merge the video of single player match and the video of couple player match into 1 video to easily naming the frames with the mean density is 5 frames per second (FPS).
- Prepare the pickleball video
- Change the "video_path" and "output_folder" filepath
- Run "python3 frames_gen.py" in terminal    


# Step 1.2: Auto label using YOLO
**Using trained YOLO model (yolopickleball.pt) to auto label the ball in frames.** 
### 
The developer using a trained YOLO model in another pickleball dataset, predict bounding boxes in these frames and keep only the box have highest confidence score.
- Install Ultrlytics library
- Change the "model", "input_folder", "output_folder" filepath
- Run "python3 yolo_detect.py" in terminal

# Step 1.3: Refine the Bounding Boxes Annotations using Roboflow
**Using Roboflow to visualize and refine the bounding boxes to best accuracy.** 

# Step 1.4: Create Categories Dataset for CatBoostRegressor model
**Using the videos and frames to label the .csv file consist of 5 categories: "file name", "visibility", "x-coordinate", "y-coordinate", "status".** 
### 
The developer first renames the images in the dataset using "image_renames.py" and make application "visibility_labeltool.py", "status_labeltool.py" to visualize the image and update VC annotations, status annotations of the .csv file.
 - Rename the images in dataset
 - Make the .csv label file with "CBR_Data_Gen.py". Remember to take images and .txt YOLO label format as input.
 - Using "refine_csv_name.py" to make sure that "file name" column in label file is correspond to image's file name.
 - Uisng Tkinter lib to make labeling application "visibility_labeltool.py" and "status_labeltool.py" to accelerate annotating tasks.

# Dataset Summarize
**With the requirements of data format for CatBoostRegressor model, the developer prepare the ".csv" dataset from 2 Pickleball Video in single player and couple player (total 3 minutes). The videos are trimmed into 961 frames and being labeled carefully.** 
 - 5 Categories: "file name", "visibility", "x-coordinate", "y-coordinate", "status"
 - Status categorie consist of 3 states: 0 - Flying; 1 - Hitting: 2 - Bounding
 - The TrackNet model using all 5 categories
 - The Bound Detection application using just 3 categories ("file name", "x-coordinate", "y-coordinate") to detect the "status"
