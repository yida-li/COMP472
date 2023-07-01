import cv2
from time import sleep
video_capture = cv2.VideoCapture(0)


def take_picture(frame):
    # Save the frame as an image file
    cv2.imwrite("picture.PNG", frame)
    print("Picture taken!")


while True:
    sleep(0.001)
    ret, frame = video_capture.read()

    key = cv2.waitKey(1) & 0xFF

    if key == ord('x'):
        break
    elif key == ord('p'):  # Press 'p' to take a picture
        take_picture(frame)
    
    cv2.imshow(
        'Welcome to the Simplest Camera App\t\t\t\t\t\t press x to exit ', frame)


video_capture.release()
cv2.destroyAllWindows()
