# Audio Response Evaluator

This project evaluates spoken responses from users based on several linguistic parameters including:
- **Fluency**
- **Vocabulary**
- **Grammar**
- **Topic Relevance**

It uses OpenAI's Whisper for transcription, spaCy for NLP processing, and FastAPI to expose the functionality via a simple API.

---

## 🔧 Features

- 🎙 Upload audio responses (e.g., `.mp3`, `.wav`)
- 🧠 Automatic transcription using Whisper
- ✍️ Evaluate linguistic features (fluency, vocabulary, etc.)
- 🚀 FastAPI-based backend for scalable deployment
- 📊 Returns structured JSON scores per parameter

---

## 📁 Project Structure

```
audio_abex/
├── audio_evaluator.py       # Core logic to analyze transcription
├── main.py                  # FastAPI server
├── utils/                   # Helper functions and tools
├── venv/                    # Virtual environment
└── requirements.txt         # Python dependencies
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/vishalgoyal316/analyze_audio.git
cd analyze_audio
```

### 2. Set up a virtual environment (Python 3.11 recommended)
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 4. Run the server
```bash
uvicorn main:app --reload
```

Visit `http://localhost:8000/docs` for Swagger API documentation.

---

## 📤 API Usage

### `POST /analyze-audio`

**Request:**
- `audio_file`: form-data file upload (audio format)

**Response:**
```json
{
  "fluency": 8.5,
  "grammar": 9.0,
  "vocabulary": 7.8,
  "relevance": 8.2,
  "transcript": "This is the spoken content."
}
```

---

## 🧠 Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/)
- [OpenAI Whisper](https://github.com/openai/whisper)
- [spaCy](https://spacy.io/)
- [PyTorch](https://pytorch.org/)

---

## 📜 License

MIT License. See `LICENSE` file for details.

---

## 🙋‍♂️ Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.
