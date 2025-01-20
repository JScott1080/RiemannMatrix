import os
import json
import sqlite3

# Load personalities from the config file
def load_personalities(config_path='config/personas.json'):
    with open(config_path, 'r') as file:
        return json.load(file)

PERSONAS = load_personalities()

# Initialize database for a given persona
def get_memory_db(persona):
    db_path = f'data/memories/{persona}_memory.db'
    if not os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS memory (user_input TEXT, response TEXT)''')
        conn.commit()
        conn.close()
    return sqlite3.connect(db_path)

# Save memory to the database associated with the given persona
def save_memory(persona, user_input, response):
    conn = get_memory_db(persona)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO memory (user_input, response) VALUES (?, ?)", (user_input, response))
    conn.commit()
    conn.close()

# Load memories from the database associated with the given persona
def load_memories(persona):
    conn = get_memory_db(persona)
    cursor = conn.cursor()
    cursor.execute("SELECT user_input, response FROM memory")
    memories = cursor.fetchall()
    conn.close()
    return memories

# Global variables
CURRENT_PERSONA = None  # No persona at startup

TRAINING_CHAT = os  # Replace with your training channel name
