import glob
import cv2
import shutil
import os
from PIL import Image


def toFrames(path):
    video_capture = cv2.VideoCapture(path)
    still_reading, image = video_capture.read()
    total_frames = 0
    if os.path.exists("frames"):
        # remove previous GIF frame files
        shutil.rmtree("frames")
    try:
        os.mkdir("frames")
    except IOError:
        print('no way this happens')
        return

    while still_reading:
        cv2.imwrite(f"frames/frame_{total_frames:05d}.jpg", image)
        still_reading, image = video_capture.read()
        total_frames += 1


def gif(gif_path, frame_folder="frames"):
    images = glob.glob(f"{frame_folder}/*.jpg")
    images.sort()
    frames = [Image.open(image) for image in images]
    frame_one = frames[0]
    frame_one.save(gif_path, format="GIF", append_images=frames,
                   save_all=True, duration=30, loop=0)


def main():
    toFrames('./test.mp4')
    gif('./test.gif')


if __name__ == "__main__":
    main()
