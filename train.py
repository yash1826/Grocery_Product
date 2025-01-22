import os
import subprocess

dataset_base_path = "D:/ML/Projects/GROCERY_PRODUCT/dataset"
train_path = os.path.join(dataset_base_path, "train")
val_path = os.path.join(dataset_base_path, "val")
data_yaml_path = "D:/ML/Projects/GROCERY_PRODUCT/data.yaml"

def check_paths(paths):
    for path in paths:
        if not os.path.exists(path):
            print(f"Error: {path} does not exist.")
            return False
    return True

if check_paths([train_path, val_path, data_yaml_path]):
    print("Dataset paths are correct!")
else:
    exit("Exiting due to incorrect dataset paths.")

yolov5_dir = "yolov5"
if not os.path.exists(yolov5_dir):
    print("Cloning YOLOv5 repository...")
    subprocess.run(["git", "clone", "https://github.com/ultralytics/yolov5.git"])

os.chdir(yolov5_dir)

print("Installing dependencies...")
subprocess.run([os.sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

print("Starting training...")
train_command = [
    "python", "train.py", 
    "--img", "640", 
    "--batch", "16", 
    "--epochs", "50", 
    "--data", data_yaml_path, 
    "--weights", "yolov5s.pt"
]
subprocess.run(train_command)

print("Training complete. Model weights saved in 'runs/train/exp/weights/'.")
