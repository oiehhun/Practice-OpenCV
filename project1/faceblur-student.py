# Import necessary libraries
import cv2
import numpy as np
import os
import urllib.request

# Function to apply Gaussian blur to an image
def apply_blur(img, k):
    return cv2.GaussianBlur(img, (k, k), 0)

# Function to pixelate a specific region in an image
def pixelate_region(image, startX, startY, endX, endY):
    region = image[startY:endY, startX:endX]
    height, width = region.shape[:2]
    temp = cv2.resize(region, (10, 10), interpolation=cv2.INTER_LINEAR)
    pixelated = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)
    image[startY:endY, startX:endX] = pixelated
    return image

# Function to pixelate the face in an image
def pixelate_face(image, blocks=10):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Draw rectangle around the face
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        image = pixelate_region(image, x, y, x + w, y + h)

    return image

# Function to download the Haarcascade file if not exists
def download_haarcascade_file():
    url = 'https://github.com/opencv/opencv/raw/master/data/haarcascades/haarcascade_frontalface_default.xml'
    filename = 'haarcascade_frontalface_default.xml'
    
    if not os.path.exists(filename):
        print(f"Downloading {filename}...")
        urllib.request.urlretrieve(url, filename)
        print(f"{filename} downloaded successfully.")

if __name__ == "__main__":
    # Download Haarcascade file if not exists
    download_haarcascade_file()

    # Load the Haarcascade classifier for face detection
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Capture video stream and apply pixelation to detected faces
    cap = cv2.VideoCapture(0)  # 0 for default webcam

    if not cap.isOpened():
        print("Error: Unable to access the webcam.")
        exit()

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Failed to grab frame.")
            break

        # Apply pixelation to the detected faces
        processed_frame = pixelate_face(frame)

        # Display the processed video
        cv2.imshow('Face Pixelation', processed_frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()
