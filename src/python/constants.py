# API Tokens and Keys
DISCORD_BOT_TOKEN = 'MTMzMDIzMTU1ODAzMjA2NDU5Mw.GKOOZl.Ta7PVh2CUD0iPcTnNP_ZV2bXkwurk1V-1fb7z0'
GOOGLE_API_KEY = 'your-google-api-key'

# File Paths
PERSONAS_JSON_PATH = 'config/personas.json'
MEMORY_DB_PATH_TEMPLATE = 'data/memories/{}_memory.db'

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
    TRAINING_CHAT = '1330598048300007539'
    print('Training chat not set. Using default value:', TRAINING_CHAT)
