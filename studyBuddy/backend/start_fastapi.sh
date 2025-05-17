#!/bin/bash
VENV_PATH="./venv"
if [ ! -d "$VENV_PATH" ]; then
    echo "Virtual environment not found at $VENV_PATH"
    exit 1
fi
source $VENV_PATH/bin/activate
uvicorn main:app --host 0.0.0.0 --port 8000