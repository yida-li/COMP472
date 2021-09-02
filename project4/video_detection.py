from imageai.Detection import VideoObjectDetection
import os

execution_path = os.getcwd()


video_detector = VideoObjectDetection()
video_detector.setModelTypeAsTinyYOLOv3()
video_detector.setModelPath(os.path.join(execution_path, "yolo-tiny.h5"))
video_detector.loadModel()


video_detector.detectObjectsFromVideo(input_file_path=os.path.join(execution_path, "dataset2.mp4"),
                                      output_file_path=os.path.join(
                                          execution_path, "dataset2_analysis"),
                                      frames_per_second=30,  minimum_percentage_probability=30)
