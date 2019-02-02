import cv2
import numpy

imgIndex = 0
face_cascade = cv2.CascadeClassifier('face_detect_classifier.xml')
video = cv2.VideoCapture(0)
while True:
    check, frame = video.read()
    faces = face_cascade.detectMultiScale(frame, scaleFactor= 1.05, minNeighbors= 3)
    if type(faces) is numpy.ndarray:
        for x, y, w, h in faces:
            image = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        print("Face detected...")
        cv2.imwrite('attachmentImg'+str(imgIndex)+'.png', image, params=None)
        imgIndex = imgIndex + 1
    else:
        print("No face detected...")
    cv2.imshow("Face detector", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()