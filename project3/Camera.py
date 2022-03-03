import cv2
from time import sleep
video_capture = cv2.VideoCapture(0)


while True:
    sleep(0.001)
    ret, frame = video_capture.read()

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

    cv2.imshow(
        'Welcome to the Simplest Camera App\t\t\t\t\t\t press x to exit ', frame)


video_capture.release()
cv2.destroyAllWindows()
