from pathlib import Path
from collections import Counter
import numpy
import pickle
import face_recognition


class FaceMatcher:
    def __init__(self, encodings_path: str):
        self.encodings_path = Path(encodings_path)
        self.encodings_path.parent.mkdir(exist_ok=True)
        self.encodings_path.touch(exist_ok=True)

    def match_face(self, incoming_encoding: numpy.ndarray) -> str:
        try:
            loaded_encodings = self._get_encodings()
        except Exception:
            raise Exception("there are no known faces yet")

        matches = face_recognition.compare_faces(
            loaded_encodings["encodings"],
            incoming_encoding,
        )
        votes = Counter(
            name
            for match, name in zip(matches, loaded_encodings["names"])
            if match
        )
        if votes:
            return str(votes.most_common(1)[0][0])
        return "Unknown"

    def _get_encodings(self) -> dict:
        try:
            with self.encodings_path.open(mode="rb") as f:
                loaded_encodings = pickle.load(f)
        except EOFError:
            raise Exception("the file is empty")
        return loaded_encodings
