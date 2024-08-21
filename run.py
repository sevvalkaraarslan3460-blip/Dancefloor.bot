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
room_id = "66bad059afeca0c24b497205"
bot_token = "60cd05e713ba823116a9e70f7fbb9418bdbca45e2c057b1fb8bf57c4c265d5f1"

my_bot = BotDefinition(getattr(import_module(bot_file_name), bot_class_name)(), room_id, bot_token)

while True:
    try:
        definitions = [my_bot]
        arun(main(definitions))
    except Exception as e:
        print(f"An exception occurred: {e}")
        traceback.print_exc()
    time.sleep(5)

