import cv2

cap = cv2.VideoCapture(0)  # 0 is typically the default webcam
if not cap.isOpened():
    print("Error: Camera is not accessible.")
else:
    print("Camera is working.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break
        cv2.imshow('Test Camera', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
            break
    cap.release()
    cv2.destroyAllWindows()
