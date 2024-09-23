import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime


video_capture = cv2.VideoCapture(0)
nasir_image = face_recognition.load_image_file("faces/Pic 1.jpg")
nasir_encodings = face_recognition.face_encodings(nasir_image)[0]

second_image = face_recognition.load_image_file("faces/Pic 1.jpg")
second_encodings = face_recognition.face_encodings(second_image)[0]

known_face_encodings= [nasir_encodings, second_encodings]
known_faces = ["nasir", "second"]

students = known_faces.copy()
face_location = []
face_encodings = []

# get the current data and time

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

file = open(f"{current_date}.csv", "w+", newline="")
lnwriter = csv.writer(file)

while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0,0), fx = 0.25, fy = 0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Recognized faces
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)

        best_match_index = np.argmin(face_distance)


        if(matches[best_match_index]):
            name = known_faces[best_match_index]

        if name in known_faces:
            font = cv2.FONT_HERSHEY_SIMPLEX
            bottomLeftCornerOfText = (10, 100)
            fontScale = 1.5
            fontColor = (255, 0, 0)
            thickness = 3
            lineType = 2
            cv2.putText(frame, name + "Present", bottomLeftCornerOfText, font, fontScale, fontColor, thickness, lineType)
            if name in students:
                students.remove(name)
                current_time = now.strftime("%H-%M%S")
                lnwriter.writerow([name, current_time])        
        cv2.imshow("Attendance", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
video_capture.release()
cv2.destroyAllWindows()
file.close()