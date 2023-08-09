import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6257940664:AAFVnJUI5UcDC7mym3bwzb8a5h3GI1kFHBw")
API_ID = int(os.environ.get("API_ID", "25982300"))
API_HASH = os.environ.get("API_HASH", "7ef41890f2707de100466b758eff9153")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001878999657"))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5657257558").split())
DB_URL = os.environ.get("DB_URL", "mongodb+srv://Luffy:Malik10_@cluster0.f0cpndf.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "BroadcastBot")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
