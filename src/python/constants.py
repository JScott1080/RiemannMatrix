import os

# API Tokens and Keys
DISCORD_BOT_TOKEN = 'ENTER_TOKEN_HERE'
GOOGLE_API_KEY = 'your-google-api-key'

# File Paths
PERSONAS_JSON_PATH = 'config/personas.json'
MEMORY_DB_PATH_TEMPLATE = 'data/memories/{}_memory.db'
LOG_FILE_PATH = 'data/logs/chatbot.log'

# Default Settings
DEFAULT_PERSONA = 'FLC'
DEFAULT_VOICE_MODEL = 'tts_models/en/lj/ljspeech-glow-tts'
DEFAULT_VOCODER = 'vocoder_models/en/ljspeech/hifigan_v2'

# URLs and Endpoints
DISCORD_API_URL = 'https://discord.com/api/v9'
GOOGLE_TRANSLATE_URL = 'https://translation.googleapis.com/language/translate/v2'

# Message Templates
WELCOME_MESSAGE = 'Welcome to the chatbot project!'
HELP_MESSAGE = 'Here are the commands you can use: ...'

# Thresholds and Limits
MAX_MEMORY_ENTRIES = 1000
CHAT_HISTORY_LIMIT = 100

# Timeouts and Intervals
REQUEST_TIMEOUT = 5  # in seconds
MESSAGE_POLL_INTERVAL = 2  # in seconds

TRAINING_CHAT = ''
if not TRAINING_CHAT:
    TRAINING_CHAT = 'ENTER_CHAT_CHANNEL_ID_HERE'
    print('Training chat not set. Using default value:', TRAINING_CHAT)

# Base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Directory paths
CONFIG_DIR = os.path.join(BASE_DIR, 'config')
DATA_DIR = os.path.join(BASE_DIR, 'data')
MEMORIES_DIR = os.path.join(DATA_DIR, 'memories')
LOGS_DIR = os.path.join(DATA_DIR, 'logs')
MODELS_DIR = os.path.join(BASE_DIR, 'models')
LLM_MODEL_DIR = os.path.join(MODELS_DIR, 'llm_model')
TTS_MODEL_DIR = os.path.join(MODELS_DIR, 'tts_model')
TRAINED_VOICE_MODELS_DIR = os.path.join(MODELS_DIR, 'trained_voice_models')
SRC_DIR = os.path.join(BASE_DIR, 'src')
PYTHON_DIR = os.path.join(SRC_DIR, 'python')
TEMPLATES_DIR = os.path.join(PYTHON_DIR, 'web_server', 'templates')
STATIC_DIR = os.path.join(PYTHON_DIR, 'web_server', 'static')

# Other constants
API_URL = 'http://localhost:5000/api'
WEBSOCKET_URL = 'ws://localhost:8000'
