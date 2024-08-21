import sys
import os
import time
import traceback
from importlib import import_module
from highrise.__main__ import *

class WebServer():

  def __init__(self):
    self.app = Flask(__name__)

    @self.app.route('/')
    def index() -> str:
      return "Funcionando"

  def run(self) -> None:
    self.app.run(host='0.0.0.0', port=8080)

  def keep_alive(self):
    t = Thread(target=self.run)
    t.start()


# BOT SETTINGS
bot_file_name = "main"
bot_class_name = "bot"
room_id = "66c54aa75912b02e24d54fa7"
bot_token = "2632b0a291fff7fa33db68d5882567342a7bdbb2d6543512bd11a42144631457"

my_bot = BotDefinition(getattr(import_module(bot_file_name), bot_class_name)(), room_id, bot_token)

while True:
    try:
        definitions = [my_bot]
        arun(main(definitions))
    except Exception as e:
        print(f"An exception occurred: {e}")
        traceback.print_exc()
    time.sleep(5)

