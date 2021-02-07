import os
import sys
import numpy as np
import json
import cv2

def cd(*path):
    return os.path.join(os.path.dirname(__file__), *path)

image_path = repr(sys.argv[1])[1:-1]
image_file = cv2.imread(image_path, 0)

cascade_file = cd("./haarcascades/haarcascade_mcs_mouth.xml")
cascade = cv2.CascadeClassifier(cascade_file)

mouth_list = cascade.detectMultiScale(image_file, 1.3, 5)

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

print(json.dumps({ "data": mouth_list }, cls=NumpyEncoder))
