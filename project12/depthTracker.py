import cv2
import mediapipe as mp
import time

mp_facedetector = mp.solutions.face_detection
mp_draw = mp.solutions.drawing_utils

path_model = "models/"
model_name = "model-f6b98070.onnx"
model = cv2.dnn.readNet(path_model + model_name)

flag = True
if (model.empty()):
    flag = False
while flag == True:
    if (model.empty()):
        flag = False

    # missing some configuration from guide
    model.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
    model.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
    cap = cv2.VideoCapture(0)

    with mp_facedetector.FaceDetection(min_detection_confidence=0.2) as face_detection:

        while cap.isOpened():
            success, img = cap.read()
            imgHeight, imgWidth, channels = img.shape

            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = face_detection.process(img)

            if results.detections:
                for id, detection in enumerate(results.detections):
                    mp_draw.draw_detection(img, detection)
                    bBox = detection.location_data.relative_bounding_box

                    h, w, c = img.shape

                    boundBox = int(bBox.xmin * w), int(bBox.ymin *
                                                       h), int(bBox.width * w), int(bBox.height * h)
                    center_point = (
                        boundBox[0] + boundBox[2] / 2, boundBox[1] + boundBox[3] / 2)

            dnnblob = cv2.dnn.blobFromImage(
                img, 1/255., (384, 384), (123.675, 116.28, 103.53), True, False)
            model.setInput(dnnblob)

            depth_map = model.forward()
            depth_map = depth_map[0, :, :]
            depth_map = cv2.resize(depth_map, (imgWidth, imgHeight))
            depth_map = cv2.normalize(
                depth_map, None, 0, 1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)

            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            depth_face = depth_map[int(
                center_point[1]), int(center_point[0])]*-1.5
            cv2.putText(img, "Depth : " + str(round(depth_face, 2)*100),
                        (200, 400), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (159, 43, 104), 3)

            cv2.imshow('Face Detection  ', img)
            cv2.imshow('Depth map', depth_map)

            if cv2.waitKey(1) & 0xFF == ord('x'):
                cap.release()
                cv2.destroyAllWindows()
                flag = False
                break
