import discord
import json
import os
import sqlite3
from chatbotLogic import get_response, switch_persona, initialize_llama
from __init__ import CURRENT_PERSONA, PERSONAS, save_memory, load_memories

TOKEN = 'YOUR_DISCORD_BOT_TOKEN'  # Replace with your bot token

# Load personalities from the config file
with open('config/personas.json', 'r') as file:
    personas = json.load(file)

intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)

# Initialize LLaMA model
llama_model = initialize_llama()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

def get_memory_db(persona):
    db_path = f'data/memories/{persona}_memory.db'
    if not os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS memory (user_input TEXT, response TEXT)''')
        conn.commit()
        conn.close()
    return sqlite3.connect(db_path)

def save_memory(persona, user_input, response):
    conn = get_memory_db(persona)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO memory (user_input, response) VALUES (?, ?)", (user_input, response))
    conn.commit()
    conn.close()

def load_memories(persona):
    conn = get_memory_db(persona)
    cursor = conn.cursor()
    cursor.execute("SELECT user_input, response FROM memory")
    memories = cursor.fetchall()
    conn.close()
    return memories

def get_llama_response(input_text, persona='AMY'):
    # Generate response using LLaMA
    response = get_response(llama_model, input_text)
    # Save the interaction in the memory database
    save_memory(persona, input_text, response)
    return response

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    user_input = message.content
    persona = 'AMY'  # You can add logic to select a persona based on the user or channel
    response = get_llama_response(user_input, persona)
    await message.channel.send(response)

client.run(TOKEN)
