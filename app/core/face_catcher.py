import numpy
import face_recognition


class FaceCatcher:
    def __init__(self, model: str = "hog"):
        self.model = model

    def catch_face(self, image_array: numpy.ndarray) -> list[numpy.ndarray]:
        face_locations = face_recognition.face_locations(
            image_array,
            model=self.model,
        )
        face_encodings = face_recognition.face_encodings(
            image_array,
            face_locations,
        )
        return face_encodings
