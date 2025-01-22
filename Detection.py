import os
import cv2
import subprocess

image_path = "D:/ML/Projects/GROCERY_PRODUCT/dataset/valid"
weights_path = "D:/ML/Projects/GROCERY_PRODUCT/runs/train/exp/weights/best.pt"
output_path = "D:/ML/Projects/GROCERY_PRODUCT/yolov5/runs/results"

os.makedirs(output_path, exist_ok=True)

subprocess.run([
    "python", "detect.py",
    "--weights", weights_path,
    "--img", "640",
    "--conf", "0.4",
    "--source", image_path,
    "--project", output_path,
    "--name", "results",
    "--exist-ok"
])

results_folder = os.path.join(output_path, "results")

if os.path.exists(results_folder):
    for image_file in os.listdir(results_folder):
        file_path = os.path.join(results_folder, image_file)
        if os.path.isfile(file_path) and image_file.lower().endswith((".jpg", ".png")):
            image = cv2.imread(file_path)
            cv2.imshow("Detection Result", image)
            cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print(f"Results folder not found: {results_folder}")
