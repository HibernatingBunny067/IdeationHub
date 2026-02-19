#!/bin/bash

echo "Activating virtual environment"
source .venv/bin/activate

echo "Starting backend.."
uvicorn backend.main:app --port 6969  --reload &
BACKEND_PID=$!

sleep 2

echo "Starting frontend.."
streamlit run ./frontend/home.py &
FRONTEND_PID=$!

echo "App started"
echo "Backend PID: $BACKEND_PID"
echo "Frontend PID: $FRONTEND_PID"

wait 
