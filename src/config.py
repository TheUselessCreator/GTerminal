import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_LINK = os.getenv("DISCORD_LINK")
GITHUB_LINK = os.getenv("GITHUB_LINK")
STEAM_PATH = os.getenv("STEAM_PATH")

# Expand %USERNAME% in Downloads folder path
raw_downloads = os.getenv("DOWNLOADS_FOLDER", "C:\\Users\\%USERNAME%\\Downloads")
DOWNLOADS_FOLDER = os.path.expandvars(raw_downloads)

# BepInEx plugins path
BEPINEX_PLUGIN_PATH = os.path.join(STEAM_PATH, "BepInEx", "plugins")
