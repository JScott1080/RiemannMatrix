from llama import LLaMA
from TTS.api import TTS
import whisper
import json
import sqlite3
from __init__ import CURRENT_PERSONA, PERSONAS, save_memory, load_memories

# Initialize TTS model
tts = TTS(model_name="tts_models/en/ljspeech-glow-tts", vocoder_name="vocoder_models/en/ljspeech/hifigan_v2")

# Initialize STT model
stt_model = whisper.load_model("small")

# Initialize LLaMA model
def initialize_llama():
    model = LLaMA(model_name="llama-3.3")
    return model

llama_model = initialize_llama()

# Function to handle TTS
def synthesize_speech(text):
    output_path = "/tmp/output.wav"
    tts.tts_to_file(text=text, file_path=output_path)
    return output_path

# Function to handle STT
def transcribe_speech(audio_input):
    result = stt_model.transcribe(audio_input)
    return result['text']

# Function to get response from LLaMA
def get_response(input_text, persona=CURRENT_PERSONA):
    if persona is None:
        return "I'm currently inactive. Please load a persona to continue."
    
    response = llama_model.generate(input_text)
    save_memory(persona, input_text, response)
    return response

# Function to switch persona
def switch_persona(new_persona):
    global CURRENT_PERSONA
    if new_persona in PERSONAS:
        CURRENT_PERSONA = new_persona
        print(f"Switched to persona: {CURRENT_PERSONA}")
    else:
        print(f"Persona {new_persona} not found.")

# Example function to run the chatbot logic (for illustration purposes)
def run_chatbot_logic(input_text):
    response = get_response(input_text)
    output_path = synthesize_speech(response)
    return response, output_path

if __name__ == "__main__":
    # Example usage (for illustration purposes)
    input_text = "Hello, how are you?"
    response, output_path = run_chatbot_logic(input_text)
    print(f"Response: {response}")
    print(f"Audio file saved to: {output_path}")
