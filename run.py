import sys
import os
import time
import traceback
from importlib import import_module
from highrise.__main__ import *

# BOT SETTINGS
bot_file_name = "Raymgbot"
bot_class_name = "Raymgbot"
room_id = "66bad059afeca0c24b497205"
bot_token ="65bd0b5c01fcde250790eaa593cee5b77bde8525ed49352980dc0d606ac3d256"

my_bot = BotDefinition(getattr(import_module(bot_file_name), bot_class_name)(), room_id, bot_token)

while True:
    try:
        definitions = [my_bot]
        arun(main(definitions))
    except Exception as e:
        print(f"An exception occurred: {e}")
        traceback.print_exc()
    time.sleep(5)

