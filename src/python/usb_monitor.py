# src/python/usb_monitor.py

import pyudev
import os
import subprocess
import time

# Function to switch persona
def switch_persona(persona):
    global CURRENT_PERSONA
    CURRENT_PERSONA = persona
    print(f"Persona switched to: {CURRENT_PERSONA}")

# Function to check for USB and read persona from file
def check_usb_for_persona():
    usb_path = "/mnt/usb_drive"  # Example mount point
    persona_file = "current_persona.txt"
    try:
        with open(os.path.join(usb_path, persona_file), 'r') as file:
            new_persona = file.read().strip()
            return new_persona
    except FileNotFoundError:
        print("Persona file not found on USB drive.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None

# Function to monitor USB events
def monitor_usb_events():
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by(subsystem='block', device_type='partition')

    for device in iter(monitor.poll, None):
        if device.action == 'remove':
            print(f"USB device removed: {device.device_node}")
            print("Waiting for new USB drive insertion...")
        elif device.action == 'add':
            print(f"USB device added: {device.device_node}")
            time.sleep(3)  # Wait for the USB drive to be fully recognized
            new_persona = check_usb_for_persona()
            if new_persona:
                switch_persona(new_persona)
            break
