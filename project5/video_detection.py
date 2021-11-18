from imageai.Detection import VideoObjectDetection
import os

execution_path = os.getcwd()

video_detector = VideoObjectDetection()
video_detector.setModelTypeAsYOLOv3()
video_detector.setModelPath(os.path.join(execution_path, "models/yolo.h5"))
video_detector.loadModel()


video_detector.detectObjectsFromVideo(input_file_path=os.path.join(execution_path, "video/traffic.mp4"), 
output_file_path=os.path.join(execution_path, "video_frame_analysis") ,
  frames_per_second=10,  minimum_percentage_probability=30)

# print(video_path)