from fastapi import FastAPI
from api.routes import image

app = FastAPI()

app.include_router(image.router)
