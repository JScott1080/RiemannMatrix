# src/python/discord_functions/discord_bot.py

import discord
from chatbotLogic import get_response, switch_persona, initialize_llama
from __init__ import CURRENT_PERSONA, PERSONAS
from python.constants import DISCORD_BOT_TOKEN, TRAINING_CHAT

TOKEN = DISCORD_BOT_TOKEN  # Replace with your bot token
CHANNEL = TRAINING_CHAT

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Check if the message is in the allowed channel
    allowed_channel_id = CHANNEL # Replace with your channel ID
    if message.channel.id == allowed_channel_id:
        user_input = message.content
        response = get_response(user_input, CURRENT_PERSONA)
        await message.channel.send(response)

client.run(TOKEN)
