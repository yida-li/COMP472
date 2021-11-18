from imageai.Detection import VideoObjectDetection
import os

execution_path = os.getcwd()

log = []


video_detector = VideoObjectDetection()
video_detector.setModelTypeAsTinyYOLOv3()
video_detector.setModelPath(os.path.join(
    execution_path, "./models/yolo-tiny.h5"))
video_detector.loadModel("fast")


def forSeconds(second_number, output_arrays, count_arrays, average_output_count):

    log.append({"------------ Second ": second_number})
    log.append(output_arrays)


video_detector.detectObjectsFromVideo(input_file_path=os.path.join(execution_path, "./path1/phase8.mp4"),
                                      output_file_path=os.path.join(
                                          execution_path, "./path1/phase8_analysis"),
                                      per_second_function=forSeconds,
                                      frames_per_second=30,
                                      minimum_percentage_probability=20)

with open('./path1/phase8_data.txt', 'w') as f:
    for item in log:
        f.write("%s\n" % item)