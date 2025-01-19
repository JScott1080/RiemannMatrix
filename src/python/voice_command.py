import speech_recognition as sr
import subprocess
import time
from usb_monitor import monitor_usb_events
from chatbotLogic import switch_persona, synthesize_speech, save_memory, retrieve_memories, get_response

CURRENT_PERSONA = 'AMY'  # Initial persona

# Function to listen for voice commands
def listen_for_command():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("Listening for the voice command...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"Voice command received: {command}")

        # USB Switch Command
        if "switch persona" in command.lower():
            print("Switching persona triggered.")
            print("Please remove the current USB drive and insert the new one.")
            monitor_usb_events()  # Start monitoring USB events

        # Start/Stop Listening
        elif "start listening" in command.lower():
            print("Voice command listener started.")
            start_voice_command_listener()
        elif "stop listening" in command.lower():
            print("Voice command listener stopped.")
            stop_voice_command_listener()  # Implement this function

        # Change Voice/Persona
        elif "change to" in command.lower() and "voice" in command.lower():
            new_persona = command.split("change to ")[1].split(" voice")[0]
            switch_persona(new_persona)
            print(f"Switched to {new_persona} voice.")

        # Query Memory
        elif "what do you remember about" in command.lower():
            topic = command.split("what do you remember about ")[1]
            memories = retrieve_memories(CURRENT_PERSONA, topic)
            print(f"Memories related to {topic}: {memories}")

        # Add Note/Memory
        elif "remember that" in command.lower():
            note = command.split("remember that ")[1]
            save_memory(CURRENT_PERSONA, note, "Note added.")
            print(f"Remembered: {note}")

        # Playback Last Response
        elif "play last response" in command.lower():
            last_response = get_response(llama_model, "Repeat the last response.")
            synthesize_speech(last_response)
            print(f"Playing last response: {last_response}")

    except sr.UnknownValueError:
        print("Could not understand the voice command.")
    except sr.RequestError as e:
        print(f"Error with the speech recognition service: {e}")

if __name__ == "__main__":
    while True:
        listen_for_command()
        time.sleep(1)  # Add a delay to avoid constant polling
