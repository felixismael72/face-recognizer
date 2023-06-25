from fastapi import UploadFile
import numpy
import cv2


class ImageProcessor:
    def __init__(self):
        pass

    async def to_cv_image(self, image: UploadFile) -> numpy.ndarray:
        image_data = await image.read()
        np_array = numpy.frombuffer(image_data, numpy.uint8)
        cv_image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
        return cv_image
