import os
import cv2

output_path = "D:/ML/Projects/GROCERY_PRODUCT/yolov5/runs/detect"

if not os.path.exists(output_path):
    print(f"Output path '{output_path}' not found. Ensure detection has been run and results are saved.")
else:
    image_files = [f for f in os.listdir(output_path) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]

    if not image_files:
        print(f"No images found in the directory '{output_path}'.")
    else:
        print(f"Displaying {len(image_files)} detected images from: {output_path}")

        for image_file in image_files:
            image_path = os.path.join(output_path, image_file)
            image = cv2.imread(image_path)

            if image is None:
                print(f"Failed to read image: {image_path}")
                continue

            cv2.imshow("Detection Result", image)
            print(f"Displaying: {image_file}")
            key = cv2.waitKey(0)

            if key == ord('q'):
                print("Exiting visualization.")
                break

        cv2.destroyAllWindows()
        print("Visualization complete.")
