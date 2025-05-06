# need to run pip install opencv-contrib-python
import cv2
import sys
import os
import numpy as np
from tensorflow.keras.models import load_model
import keras
import tensorflow as tf

# Class to get the image from the camera and process it
class GetImage:
    def __init__(self):
        self.runGetImage()

    # Function to get the image from the camera and process it
    def runGetImage(self):
        # Load the cascade
        cascPath = os.path.abspath(os.path.dirname(os.getcwd())) + "/haarcascade_frontalface_alt.xml"
        print(os.path.exists(cascPath))
        faceCascade = cv2.CascadeClassifier(cascPath)

        # Load the model
        model = load_model("emotion_model.keras")

        # capture video from the camera
        video_capture = cv2.VideoCapture(0)

        while True:
            # Capture frame-by-frame
            _, frame = video_capture.read()

            # Convert the frame to grayscale for face detection
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # Convert the frame to RGB for emotion detection
            rgb = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)

            # Detect faces in the frame
            faces = faceCascade.detectMultiScale(
                gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE
            )



            # Draw a rectangle around the faces
            for x, y, w, h in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)        
                
                # Extract the face as a rectangle
                face = gray[y:y+h, x:x+w]

                # Ensure face exists before processing
                if face.size > 0:
                    # Resize the face image to (48, 48)
                    face_resized = cv2.resize(face, (48, 48)) 

                    # Add an additional dimension for channels (1 channel for grayscale)
                    face_input = face_resized.reshape(1, (48, 48)[0], (48, 48)[1], 1)  # Shape (1, 48, 48, 1)

                    # Normalize the image
                    face_input = face_input / 255.0

        
                    # Run the model on the face image and get the predicted emotion
                    result, probability = self.findEmotion(model.predict(face_input))
                    # Text to display on the frame
                    text = result+ ", "+ str(int(probability*100)) + "%"

                    # Draw rectangle around face and label with predicted emotion
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

            # Display the resulting frame
            cv2.imshow("Video", frame)

            # Press 'q' to exit the loop
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        # When everything is done, release the capture
        video_capture.release()
        cv2.destroyAllWindows()


    # Function to find the emotion from the model output
    def findEmotion(self, emotionsInt):
        print(emotionsInt)
        # Get the index of the maximum value in the array
        index = np.argmax(emotionsInt)
        print(index)
        emotions = ["suprise", "sadness", "happy", "fear", "disgust", "contempt", "anger"]
        #Return the emotion and the probability
        return emotions[index], emotionsInt[0][index]
