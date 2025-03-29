import torch
import cv2
import numpy as np

# Load your trained YOLOv5 model (replace with your trained weights)
model = torch.hub.load('ultralytics/yolov5', 'custom', path='runs/train/exp/weights/best.pt')  # Path to your best.pt weights

# Function to detect objects (like phones) in an image
def detect_phone_in_image(image_path):
    # Load image using OpenCV
    img = cv2.imread(image_path)

    # Perform inference with YOLOv5
    results = model(img)

    # Render the results (draw bounding boxes)
    results.render()

    # Display the result
    cv2.imshow("Phone Detection", results.imgs[0])  # Show the image with detections 
    cv2.waitKey(0)  # Wait for a key press to close the window
    cv2.destroyAllWindows()

    # Save the image with bounding boxes
    cv2.imwrite('detected_phone_output.jpg', results.imgs[0])

    # Print results (optional)
    print(results.pandas().xywh)  # Show the detected object labels and coordinates

# Example usage
image_path = r'C:\path\to\your\image.jpg'  # Update with your image path
detect_phone_in_image(image_path)
