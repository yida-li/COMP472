from imageai.Detection import VideoObjectDetection
import os

execution_path = os.getcwd()


video_detector = VideoObjectDetection()
video_detector.setModelTypeAsTinyYOLOv3()
video_detector.setModelPath(os.path.join(execution_path, "yolo-tiny.h5"))
video_detector.loadModel("fastest")


video_detector.detectObjectsFromVideo(input_file_path=os.path.join(execution_path, "dataset3.mp4"),
                                      output_file_path=os.path.join(
                                          execution_path, "dataset3_analysis_fast"),
                                      frames_per_second=5,  minimum_percentage_probability=40)
