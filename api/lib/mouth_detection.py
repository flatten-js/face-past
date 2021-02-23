import os
import sys
import json
import cv2

def cd(*path):
    return os.path.join(os.path.dirname(__file__), *path)

image_path = repr(sys.argv[1])[1:-1]
image = cv2.imread(image_path, 0)

cascade_file = cd("./haarcascades/p945-n1139.xml")
cascade = cv2.CascadeClassifier(cascade_file)

def detect_mouth(n=1, scope=(1, 20), radius=5):
    def options(min):
        return dict(scaleFactor=1.11, minNeighbors=3, minSize=(min, min))

    for i in range(*scope):
        min = i * radius
        mouth_list = cascade.detectMultiScale(image, **options(min))

        if len(mouth_list) == n:
            break

    return mouth_list

result = { "result": detect_mouth().tolist() }

print(json.dumps(result))
