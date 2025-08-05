import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7804036800:AAEFKgbGjX2E11ZWmQtMbzZBJxrSMyYVQD0")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "25025064"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "f9970f147d0bdc333ce0c29c40da4bbb")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "7995988644"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "saraswati sharma")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
