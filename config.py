import os

API_ID = API_ID = 20810825

API_HASH = os.environ.get("API_HASH", "707e67f53b4593a3e9b6b424311f84d0")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6737613081:AAEIRA_f_oo9IQ5DUwVybbUHF4rrzI9slrU")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6301693754))

LOG = -1002053318391
try
    ADMINS
    for x in (os.environ.get("ADMINS", "6301693754").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


