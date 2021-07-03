from keras.models import load_model
from time import sleep
from keras.preprocessing.image import img_to_array
import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')
classifier =load_model(r'sampleTrainingModel.h5')
emotion_labels = ['Grrrr','Disgust','Fear','feelsgoodman','Basic Bitch', 'feelsbadman', 'PogChamp']
Joy = (168, 168, 50)
Shocked = (168, 50, 127)
Melancholy = (50, 168, 58)
Hatred = (168, 50, 50)
Simp = (119, 50, 168)
Identifier1 = (50, 146, 168)
Unfiltered=(50, 168, 144)


cap = cv2.VideoCapture(0)

def make_1080p():
    cap.set(3, 1920)
    cap.set(4, 1080)

def make_720p():
    cap.set(3, 1280)
    cap.set(4, 720)

def make_480p():
    cap.set(3, 640)
    cap.set(4, 480)

make_1080p()
while True:
    sleep(0.05)
    _, frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break 

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),Identifier1,2)
        face_region = gray[y:y+h,x:x+w]
        face_region = cv2.resize(face_region,(48,48),interpolation=cv2.INTER_AREA)



        if np.sum([face_region])!=0:
            object = face_region.astype('float')/255.0
            object = img_to_array(object)
            object = np.expand_dims(object,axis=0)
            prediction = classifier.predict(object)[0]
            label=emotion_labels[prediction.argmax()]            
            label_position = (x,y)
            if(label=='Basic Bitch'):
                cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_COMPLEX_SMALL,1,Simp,2)
            elif(label=='Grrrr'):
                cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_COMPLEX_SMALL,1,Hatred,2)
            elif(label=='PogChamp'):
                cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_COMPLEX_SMALL,1,Shocked,2)
            elif(label=='feelsgoodman'):
                cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_COMPLEX_SMALL,1,Joy,2)
            elif(label=='feelsbadman'):
                cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_COMPLEX_SMALL,1,Melancholy,2)
            else:
                cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_COMPLEX_SMALL,1,Unfiltered,2)                                
    cv2.imshow('Emotions                                       enter x to exit ',frame)    

cap.release()
cv2.destroyAllWindows()