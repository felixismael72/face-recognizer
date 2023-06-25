from fastapi import APIRouter, File, UploadFile, Response, Form
from ..utils.image_processor import ImageProcessor
import json
from core.face_catcher import FaceCatcher
from core.face_matcher import FaceMatcher
from core.model_trainer import ModelTrainer
from config import FACE_RECOGNITION_MODEL, ENCODINGS_PATH, TRAINING_PATH

router = APIRouter()


@router.post("/train-model")
async def train_model(
    person_name: str = Form(...),
    image: UploadFile = File(...),
):
    if not person_name.strip():
        content = json.dumps(
            {"msg": "the person name must be provided"},
        )
        return Response(content=content, status_code=400)

    model_trainer = ModelTrainer(
        FACE_RECOGNITION_MODEL,
        TRAINING_PATH,
        ENCODINGS_PATH,
    )
    await model_trainer.add_training_image(
        person_name,
        image,
    )

    await model_trainer.encode_known_faces()

    return {"msg": "new faces were encoded"}


@router.post("/recognize-face")
async def recognize_face(image: UploadFile = File(...)):
    img_processor = ImageProcessor()
    img_array = await img_processor.to_cv_image(image=image)

    face_catcher = FaceCatcher(FACE_RECOGNITION_MODEL)
    faces = face_catcher.catch_face(image_array=img_array)

    face_owners = []

    face_matcher = FaceMatcher(ENCODINGS_PATH)
    for face in faces:
        try:
            face_owners.append(face_matcher.match_face(face))
        except Exception:
            content = json.dumps(
                {"msg": "there are no known faces yet"}
            )
            return Response(content=content, status_code=400)

    return {"face owners": face_owners}
