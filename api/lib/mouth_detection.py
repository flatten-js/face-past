import os
import sys
import json

from mouth import Mouth

def cd(*path):
    return os.path.join(os.path.dirname(__file__), *path)

def path_parse(path):
    return repr(path)[1:-1]

image_path = path_parse(sys.argv[1])

cascade_path = cd('haarcascades')
face_path = cd(cascade_path, 'lbpcascade_animeface.xml')
mouth_path = cd(cascade_path, 'p945-n1139.xml')

mouth = Mouth(cascade_face=face_path, cascade_mouth=mouth_path)
result = mouth.detect(image_path)

print(json.dumps({ "result": result }))
