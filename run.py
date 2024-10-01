import sys
import os
import time
import traceback
from importlib import import_module
from highrise.__main__ import *

# BOT SETTINGS
bot_file_name = "MGBot"
bot_class_name = "MGBot"
room_id = "66d2726b2e80dd1f614c4dbb"
bot_token ="432f23df3fc5076fe6c95ade994a533c9d473ecdb56acc31346899a94d6aaa6d"

my_bot = BotDefinition(getattr(import_module(bot_file_name), bot_class_name)(), room_id, bot_token)

while True:
    try:
        definitions = [my_bot]
        arun(main(definitions))
    except Exception as e:
        print(f"An exception occurred: {e}")
        traceback.print_exc()
    time.sleep(5)

