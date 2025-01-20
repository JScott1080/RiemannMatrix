import argparse
import threading
import time
import subprocess
from voice_command import listen_for_command
from usb_monitor import monitor_usb_events, check_usb_for_persona
from python.Discord.discord_bot import run_discord_bot
from chatbotLogic import run_chatbot_logic, switch_persona, initialize_llama
from __init__ import CURRENT_PERSONA, PERSONAS

# Function to run the voice command listener in a separate thread
def start_voice_command_listener():
    thread = threading.Thread(target=listen_for_command)
    thread.start()

# Function to run the USB monitor in a separate thread
def start_usb_monitor():
    thread = threading.Thread(target=monitor_usb_events)
    thread.start()

# Function to start the Unreal project
def start_unreal_project():
    print("Starting Unreal Project...")
    subprocess.run(["path_to_your_unreal_project_launcher", "arg1", "arg2"])

# Function to start C++ components
def start_cpp_components():
    print("Starting C++ Components...")
    subprocess.run(["path_to_your_cpp_executable", "arg1", "arg2"])

# Function to wait for USB and initialize persona
def wait_for_usb_and_init_persona():
    while True:
        usb_persona = check_usb_for_persona()
        if usb_persona:
            switch_persona(usb_persona)
            break
        time.sleep(1)  # Check every second

# Main function to start all processes
def main(args):
    if args.persona:
        switch_persona(args.persona)
        print(f"Starting AI with persona: {CURRENT_PERSONA}")
    else:
        print(f"Starting AI with initial persona: {CURRENT_PERSONA}")

    if args.mode == 'discord':
        run_discord_bot()  # Start the Discord bot

    if args.mode == 'event':
        wait_for_usb_and_init_persona()  # Wait for USB and initialize persona
        start_voice_command_listener()  # Start voice command listener
        start_usb_monitor()  # Start USB monitor
        start_unreal_project()  # Start Unreal project
        start_cpp_components()  # Start C++ components

    while True:
        time.sleep(1)  # Keep the main thread alive

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start AI components.")
    parser.add_argument('--mode', choices=['discord', 'event'], required=False, help='Mode to run the AI components: discord or event')
    parser.add_argument('--persona', type=str, help='Persona to start with (optional)')

    args = parser.parse_args()

    if not args.mode:
        print("Running in default mode. Waiting for USB or command.")
        wait_for_usb_and_init_persona()

    main(args)
