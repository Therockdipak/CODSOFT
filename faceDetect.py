import cv2
import time

# Load the Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the video capture (0 for webcam, or provide the path to a video file)
cap = cv2.VideoCapture(0)

# Get the current time
start_time = time.time()

# Set the duration to 10 seconds
duration = 10

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    if not ret:
        break

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Check if faces are detected
    if len(faces) > 0:
        # Define data of the person
        person_data = "Name: Dipak\nAge: 30\nOccupation: AI Developer"

        # Print the data to the terminal
        print("Person Data:")
        print(person_data)
        break

    # Display the resulting frame
    cv2.imshow('Face Detection', frame)

    # Break the loop when 10 seconds have passed
    if time.time() - start_time >= duration:
        break

    # Break the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()
