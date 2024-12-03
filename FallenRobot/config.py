class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 6
    API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"

    CASH_API_KEY = ""  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = ""  # A sql database url from elephantsql.com

    EVENT_LOGS = ()  # Event logs channel to note down important bot level events

    MONGO_DB_URI = ""  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://files.catbox.moe/i6fdqj.jpg"

    SUPPORT_CHAT = "https://t.me/+DPnoiS4x3mhmZmE1"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = ""  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = ""  # Get this value from https://timezonedb.com/api

    OWNER_ID = 7221498454  # User id of your telegram account (Must be integer)

    OWNER_USERNAME = "Anime_cath"

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = [7526369190]  # User id of sudo users
    DEV_USERS = [7526369190]  # User id of dev users
    DEMONS = [7526369190]  # User id of support users
    TIGERS = [7526369190]  # User id of tiger users
    WOLVES = [7526369190]  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
