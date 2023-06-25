from dotenv import dotenv_values

config = dotenv_values(".env")

FACE_RECOGNITION_MODEL = str(config.get("FACE_RECOGNITION_MODEL"))
ENCODINGS_PATH = str(config.get("ENCODINGS_PATH"))
TRAINING_PATH = str(config.get("TRAINING_PATH"))
