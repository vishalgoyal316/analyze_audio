import whisper
import spacy
import textstat
import language_tool_python
import difflib
import json
import argparse
import os

import warnings
warnings.filterwarnings("ignore")

# Load models
whisper_model = whisper.load_model("base")
nlp = spacy.load("en_core_web_sm")
grammar_tool = language_tool_python.LanguageTool('en-US')

def transcribe_audio(file_path):
    result = whisper_model.transcribe(file_path)
    return result["text"]

def evaluate_fluency(text):
    words = text.split()
    num_words = len(words)
    pauses = text.count(",") + text.count("...") + text.count("-")
    fluency_score = max(0, 10 - (pauses / max(1, num_words)) * 50)
    return round(min(fluency_score, 10), 2)

def evaluate_vocabulary(text):
    words = text.split()
    unique_words = set(words)
    diversity = len(unique_words) / max(len(words), 1)
    vocab_score = round(min(diversity * 20, 10), 2)
    return vocab_score

def evaluate_grammar(text):
    matches = grammar_tool.check(text)
    errors = len(matches)
    total_sentences = max(1, text.count('.') + text.count('!') + text.count('?'))
    grammar_score = max(0, 10 - (errors / total_sentences) * 2)
    return round(min(grammar_score, 10), 2)

def evaluate_relevance(text, topic):
    text_doc = nlp(text)
    topic_doc = nlp(topic)
    similarity = text_doc.similarity(topic_doc)
    return round(similarity * 10, 2)

def evaluate_audio_response(audio_path, topic):
    transcript = transcribe_audio(audio_path)

    return {
        "transcript": transcript,
        "fluency": evaluate_fluency(transcript),
        "vocabulary": evaluate_vocabulary(transcript),
        "grammar": evaluate_grammar(transcript),
        "relevance": evaluate_relevance(transcript, topic)
    }

if 0: 
    def save_scores_to_json(scores: dict, audio_filename: str, output_dir: str = "."):
        # Extract the base name without extension
        base_name = os.path.splitext(os.path.basename(audio_filename))[0]
        output_path = os.path.join(output_dir, f"{base_name}_scores.json")
        
        # Save to JSON file
        with open(output_path, 'w') as f:
            json.dump(scores, f, indent=4)
        
        print(f"[✅] Scores saved to {output_path}")
    

    if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("--audio", type=str, required=True, help="Path to the audio file")
        parser.add_argument("--topic", type=str, required=True, help="Topic or question for relevance analysis")
        args = parser.parse_args()
    
        scores = evaluate_audio_response(args.audio, args.topic)
        print(json.dumps(scores, indent=2))
        save_scores_to_json(scores, args.audio)
