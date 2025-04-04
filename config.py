from os import environ

API_ID = int(environ.get("API_ID", "6681cd17e17fb536d00bfad2bd9f0cd6"))
API_HASH = environ.get("API_HASH", "22193332")
BOT_TOKEN = environ.get("BOT_TOKEN", "7509459901:AAHLb7yGn0YhHasiOVM8UdFioeZX0v9gnFY")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002206934353"))
ADMINS = int(environ.get("ADMINS", "6947378236"))
DB_URI = environ.get("DB_URI", "mongodb+srv://beanonymoushacker09:q9gxQwIZDCmVOycI@cluster0.ej0gk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "autoacceptbot")
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', True))
IS_FSUB = bool(environ.get("FSUB", True))
AUTH_CHANNELS = environ.get("AUTH_CHANNEL", "")
AUTH_CHANNELS = [int(channel_id) for channel_id in AUTH_CHANNELS.split(",")]
