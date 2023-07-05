from dotenv import load_dotenv
import os

load_dotenv()

# Do not remove these 2 lines:
BOT_TOKEN = os.getenv('BOT_TOKEN')  # You should consider using env variables or a secret manager for this.
APP_NAME = 'bot'
