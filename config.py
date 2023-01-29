# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "1240066432"))
API_HASH = os.environ.get("API_HASH", "113378543a8c43310ff96d22cc95061f")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6047286645:AAG5Iv_LCWaHGPFG4_JXtyiRA_MRtVm2za4")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("1240066432")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "harmish")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://harmish:harmish7777@cluster0.jh22asn.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "1240066432")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(Id Owned Id)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001240066432")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "main_movie_hub") # For Force Subscription
BROADCPAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", 'https://telegra.ph/file/dc652fe85ec8b8ae9a1d7.jpg') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
