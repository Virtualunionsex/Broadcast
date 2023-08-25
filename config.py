import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6697713258:AAFDfdivj4INPJVDlfI_k7APbYxds4wmGbs")
API_ID = int(os.environ.get("API_ID", "22825629"))
API_HASH = os.environ.get("API_HASH", "e8db542482a1638b4e5b03ed1ddae521")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001932029067"))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "6404342282").split())
DB_URL = os.environ.get("DB_URL", "mongodb+srv://Luffy:Malik10_@cluster0.f0cpndf.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "BroadcastBot")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
