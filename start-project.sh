#!/bin/bash

executionPath=$(pwd)

echo "\
  +-----------------------+
  |   Validating Path     |
  +-----------------------+\
  "

if [[ $executionPath == *"image-processor" ]]; then
  echo "\
  +-----------------------+
  | Cleaning Dependencies |
  +-----------------------+\
  "
  python3 -m pip uninstall -y -r <(pip freeze)
  echo "\
  +-----------------------+
  |     Tyding App Up     |
  +-----------------------+\
  "
  python3 -m pip install -r requirements.txt

  echo "\
  +-----------------------+
  |     Running App       |
  +-----------------------+\
  "
  cd app
  uvicorn main:app --reload
else
  echo "The path is not quite right."
fi
