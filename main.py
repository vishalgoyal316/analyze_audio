from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
import shutil, os
from audio_evaluator import evaluate_audio_response

app = FastAPI()

@app.post("/evaluate-audio/")
async def evaluate_audio_endpoint(
    audio_file: UploadFile = File(...),
    topic: str = Form(...)
):
    temp_file_path = f"temp_{audio_file.filename}"
    try:
        with open(temp_file_path, "wb") as buffer:
            shutil.copyfileobj(audio_file.file, buffer)

        results = evaluate_audio_response(temp_file_path, topic)
        results["topic"] = topic
        results["filename"] = audio_file.filename

        return JSONResponse(content=results)

    finally:
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
