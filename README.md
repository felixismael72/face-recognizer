# Face Recognizer

This project is a Python application built with FastAPI that allows you to read images from requests, process them using computer vision techniques, and find matches in an image storage. It provides an API for image processing, matching operations, and training a face recognition model. 

The app includes a training model endpoint that accepts images and the corresponding person name. By providing images of individuals along with their names, the app can learn and recognize the faces of those individuals in subsequent images. This training capability enables the app to personalize the face recognition functionality and provide accurate identification of known individuals.

With its image processing, matching, and training features, this application can be seamlessly integrated into other applications or used as a standalone service to enhance face recognition capabilities and enable various use cases such as access control, identity verification, or personalized user experiences.

## Features

- Image Processing: Read images from requests and apply computer vision techniques for tasks such as face detection and object recognition.
- Image Matching: Perform image matching operations to find person's faces.
- API Endpoints: Provides API endpoints for uploading images, processing them using the implemented computer vision techniques, and retrieving matching results.
- Face recognition training: Provides a training endpoint so the application can know more faces throughout time.

## Requirements

- Python 3.7 or higher
- [Virtualenv](https://virtualenv.pypa.io/) (recommended)
- CMake 3.26 or higher
- You're gonna need an .env file, check `app/.env.example` to get an idea.


## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/felixismael72/face-recognizer.git
   ```

2. Run the project:
   
   ```bash
   cd image-processor
   chmod +x start-project.sh
   ./start-project.sh
   ```


> ⚠️ **WARNING:** It is strongly recommended to use a virtual environment while running this project. The included bash script manages Python dependencies and may remove some of your existing Python dependencies. To ensure a clean and isolated environment, it is highly advised to set up and activate a virtual environment before executing the script.
