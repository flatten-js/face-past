import cv2

class Mouth:
    classifier_face = None
    classifier_mouth = None

    def __init__(self, cascade_face, cascade_mouth):
        self.classifier_face = self.__to_classifier(cascade_face)
        self.classifier_mouth = self.__to_classifier(cascade_mouth)

    def __to_classifier(self, cascade_path):
        return cv2.CascadeClassifier(cascade_path)

    def __detect_options(self):
        return dict(scaleFactor=1.11, minNeighbors=3)

    def __detect_face(self, image):
        options = self.__detect_options()
        faces = self.classifier_face.detectMultiScale(image, **options)

        result = []
        for face_coord in faces:
            x, y, w, h = face_coord
            face_image = image[y:y+h, x:x+w]
            result.append((face_image, face_coord))

        return result

    def __filtering(self, n=1, scope=(1, 20), radius=5):
        def output(classifier, image):
            options = self.__detect_options()

            for i in range(*scope):
                min = i * radius
                result = classifier.detectMultiScale(image, **options, minSize=(min, min))

                if len(result) == n:
                    break

            if isinstance(result, tuple):
                return []

            return result.tolist()

        return output

    def __adjust(self, face_coord, mouth_coord, rate=5.25):
        mouth_size = face_coord[2] / rate

        if mouth_size >= mouth_coord[2]:
            mouth_coord[0] -= (mouth_size - mouth_coord[2]) / 2
            mouth_coord[1] -= (mouth_size - mouth_coord[3]) / 2
            mouth_coord[-2:] = [mouth_size] * 2

        return mouth_coord

    def __restore(self, face_coord, mouth_coords):
        coords = []

        for mouth_coord in mouth_coords:
            mouth_coord = self.__adjust(face_coord, mouth_coord)

            zip_coord = zip(face_coord[:2], mouth_coord[:2])
            x, y = list(map(lambda x: sum(x), zip_coord))

            coord = list(map(lambda x: int(x), [x, y, *mouth_coord[-2:]]))
            coords.append(coord)

        return coords

    def __detect_mouth(self, faces):
        filtering = self.__filtering()

        mouths = []
        for (image, coord) in faces:
            mouth_coord = filtering(self.classifier_mouth, image)

            if not mouth_coord:
                continue

            mouths += self.__restore(coord, mouth_coord)

        return mouths

    def detect(self, image_path):
        image = cv2.imread(image_path, 0)
        faces = self.__detect_face(image)

        if not faces:
            return []

        return self.__detect_mouth(faces)
