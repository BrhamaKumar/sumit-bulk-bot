import os

API_ID = API_ID = 18429621

API_HASH = os.environ.get("API_HASH", "2034b81303744d1dd2c7ffc02e21cfe2")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6855105570:AAFcqA756t3CZzMwzwNM08fTeUFj9P8vBRI")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5411073064))

LOG = -1001566403795

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5411073064").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


