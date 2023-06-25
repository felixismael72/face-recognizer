# Face Recognizer

This project is a Python application built with FastAPI that allows you to read images from requests, process them using computer vision techniques, and find matches in a database. It provides an API for image processing and matching operations, enabling you to integrate it with other applications or use it as a standalone service.

## Features

- Read images from requests and process them using computer vision techniques.
- Perform image matching to find similar images in a database.
- API endpoints for uploading images, processing, and retrieving matching results.
- Integration with a database for storing and querying image data.
- Efficient and scalable image processing with FastAPI.

## Requirements

- Python 3.7 or higher
- [Virtualenv](https://virtualenv.pypa.io/) (recommended)
- CMake 3.26 or higher


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
