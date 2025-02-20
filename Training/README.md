# Step 2.1: Data Preparation
**From CatBoostRegressor Dataset, we need to modify data labels from the label file into Catboost format.** 
###
From categorie "file name", the developer split into 2 categories "file name" + "time stamp" in numerical format.
- Prepare the CatBoostRegressor .csv dataset file
- Run rename_dataset.py 
- Using spreadsheet software like exel, gg sheet to make time stamps with 0.2s per step
- Make sure the dataset folder have format game{i}/clip{i}/Label.csv


# Step 2.2: Create features
**Now from "x-coordinate" and "y-coordinate" we can create some features to feed into the model.** 
### 
The developer took 3 consecutive frames, made features like difference between x and y coordinates of neighboring points, distance relations between previous and the following ball points.
- Coordinate difference (x - x_lag), difference inverse (x_lead - x), divide (x_diff / x_diff_inv)
- Using binary test with threshold = 0.5 for prediction function
- Run "python3 bounce_train.py --path_dataset --path_save_model" in terminal

# Step 2.3: Create extend features for better "recall score"
**With the time stamp (0.2s per step) categorie, we can create acceleration features to improve training results.** 
From time stamp, x_diff, y_diff, etc... the developer create velocity feature and acceleration feature.
- Velocity (x_diff / time_diff), velocity inverse (x_diff_inv / time_diff), acceleration (v_diff / time_diff)
- Run "python3 bounce_train_extend.py --path_dataset --path_save_model" in terminal

# Training Summarize
![image](https://github.com/user-attachments/assets/aef79483-c7fd-496c-9599-ca0fc2dfd16c)

**Using 960 rows Pickleball events dataset in .csv format, we can obtain an comparable results hereafter.** 
 - As a baseline, we retrain the model with Tennis Dataset and obtain 4643 rows of test set, accuracy = 0.982 and recall = 0.624 
 - With our Pickleball events dataset, we obtain 98 rows of test set, accuracy = 0.928 and recall = 0.428
 - Then we add extend features and SMOTE (imbalance technique) to improve the sensitivity of model, we obtain 98 rows of test set, accuracy = 0.898 and recall = 0.571
