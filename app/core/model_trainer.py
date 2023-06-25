from pathlib import Path
from fastapi import UploadFile
from core.face_catcher import FaceCatcher
import pickle
import face_recognition
import uuid


class ModelTrainer:
    def __init__(
        self,
        model: str,
        training_path: str,
        output_path: str,
    ):
        self.model = model
        self.training_path = Path(training_path)
        self.training_path.mkdir(exist_ok=True)
        self.output_path = Path(output_path)
        self.output_path.parent.mkdir(exist_ok=True)
        self.output_path.touch(exist_ok=True)
        self.face_catcher = FaceCatcher(model=model)

    async def add_training_image(
        self,
        person_name: str,
        img: UploadFile,
    ) -> None:
        img_path = self._get_img_path(person_name)

        with open(img_path, "wb") as f:
            f.write(await img.read())

    def _get_img_path(self, person_name: str) -> str:
        img_dir = self._get_img_dir(person_name)

        img_name = self._get_img_name()

        return img_dir + "/" + img_name

    def _get_img_dir(self, person_name: str) -> str:
        treated_name = person_name.replace(" ", "-").lower()
        dir = Path(treated_name)
        img_dir = self.training_path.joinpath(dir)
        img_dir.mkdir(parents=True, exist_ok=True)
        return img_dir.__str__()

    def _get_img_name(self) -> str:
        img_id = str(uuid.uuid4())
        return img_id + ".jpg"

    async def encode_known_faces(self) -> None:
        names = []
        encodings = []

        for file_path in self.training_path.glob("*/*"):
            name = file_path.parent.name
            img = face_recognition.load_image_file(file_path)

            face_encodings = self.face_catcher.catch_face(img)
            for encoding in face_encodings:
                names.append(name)
                encodings.append(encoding)

        name_encodings = {"names": names, "encodings": encodings}

        with self.output_path.open(mode="wb") as f:
            pickle.dump(name_encodings, f)
