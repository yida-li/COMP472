import numpy as np
import face_recognition as fr
import cv2
from time import sleep
video_capture = cv2.VideoCapture(0)

yida = fr.load_image_file("happiness.PNG")
yida_face = fr.face_encodings(yida)[0]

yida1 = fr.load_image_file("sorrow.PNG")
yida_face1 = fr.face_encodings(yida1)[0]

yida2 = fr.load_image_file("stunned.PNG")
yida_face2 = fr.face_encodings(yida2)[0]

known_face_encondings = [yida_face]
known_face_encondings1 = [yida_face1]
known_face_encondings2 = [yida_face2]

Identifier1 = (50, 146, 168)
my_favorite_hex = (252, 3, 115)
Tag = ["yida found"]

while True: 
    sleep(0.05)    
    ret, frame = video_capture.read()
    rgb_frame = frame[:, :, ::-1]
    face_locations = fr.face_locations(rgb_frame)
    face_encodings = fr.face_encodings(rgb_frame, face_locations)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

    for (x, r, y, l), face_encoding in zip(face_locations, face_encodings):
        name = " "
        matches = fr.compare_faces(known_face_encondings, face_encoding)    
        face_distances = fr.face_distance(known_face_encondings, face_encoding)


        matches1 = fr.compare_faces(known_face_encondings1, face_encoding)    
        face_distances1 = fr.face_distance(known_face_encondings1, face_encoding)

        matches2 = fr.compare_faces(known_face_encondings2, face_encoding)    
        face_distances2 = fr.face_distance(known_face_encondings2, face_encoding)




        best_match_index = np.argmin(face_distances)
        best_match_index1 = np.argmin(face_distances1)
        best_match_index2 = np.argmin(face_distances2)

        if matches[best_match_index]:
            name = Tag[best_match_index]
        elif matches1[best_match_index1]:
            name = Tag[best_match_index1] 
        elif matches2[best_match_index2]:
            name = Tag[best_match_index1]               

        cv2.rectangle(frame, (l, x), (r, y), Identifier1, 1)
        cv2.putText(frame, name, (l, x-11), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.0, my_favorite_hex, 1)

    cv2.imshow('face recognition                                       enter x to exit ', frame)


video_capture.release()
cv2.destroyAllWindows()