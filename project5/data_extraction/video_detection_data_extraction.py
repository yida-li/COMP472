from imageai.Detection import VideoObjectDetection
import os

execution_path = os.getcwd()

log = []


video_detector = VideoObjectDetection()
video_detector.setModelTypeAsYOLOv3()
video_detector.setModelPath(os.path.join(execution_path, "models/yolo.h5"))
video_detector.loadModel("fast")


def forFrame(frame_number, output_array, output_count):
    print("------------Frame Analytics --------------")


def forMinute(minute_number, output_arrays, count_arrays, average_output_count):
    print("------------END OF A MINUTE but not really--------------")


def forSeconds(second_number, output_arrays, count_arrays, average_output_count):

    log.append(output_arrays)
    log.append({"------------END OF SECOND ": second_number})


video_detector.detectObjectsFromVideo(
    input_file_path=os.path.join(execution_path, "dataset1.mp4"),
    output_file_path=os.path.join(
        execution_path, "dataset1_object_extraction"),
    frames_per_second=5,
    per_second_function=forSeconds,
    per_frame_function=forFrame,
    per_minute_function=forMinute,
    minimum_percentage_probability=30,
    detection_timeout=20
)


with open('extracted_data.txt', 'w') as f:
    for item in log:
        f.write("%s\n" % item)
