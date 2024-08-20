import asyncio
import time
from asyncio import run as arun

from highrise.__main__ import *

from equip import equip
from keep_alive import keep_alive
from remove_outfit import remove

keep_alive()
from highrise import *
from highrise import BaseBot, Position
from highrise.models import *
from highrise.models import (
  AnchorPosition,
  Position,
  SessionMetadata,
  User,
)

#  YOU CAN CHANGR VIP LIST RAY
vip = [
    "iced_yu","Damn_snake","love_cant_relate","RayMg","FallonXOXO"
]

class Bot(BaseBot):

  def __init__(self):

    self.user_teleport_position = Position(x=1.5, y=0.25, z=14.5, facing='FrontRight')
    self.user_teleport_position2 = Position(x=5.5, y=10.0, z=3.5, facing='FrontRight')
    self.user_teleport_position3 = Position(x=10.5, y=14.75, z=4.5, facing='FrontLeft')
    self.bar = Position(x=15.0, y=0.25, z=2.5, facing='FrontLeft')

    self.user_loops = {}



  async def on_start(self, session_metadata: SessionMetadata) -> None:

    print("hi im alive?")
    self.highrise.tg.create_task(
        self.highrise.teleport(
            session_metadata.user_id,
        Position(x=15.0, y=0.25, z=2.5, facing='FrontLeft')))



  async def get_users(self, selected_users, default_user):
    target_users = []
    if len(selected_users) == 0:
      return [default_user]

    users = await self.highrise.get_room_users()
    for user in users.content:
      if user[0].username in selected_users:
        target_users.append(user[0])
    return target_users

  async def on_user_join(self, user: User,position: Position | AnchorPosition) -> None:
          await self.highrise.send_whisper(user.id, f"welcome to the room {user.username}!")


  emote_dict = {
      "blow": {
          "emote": "emote-headblowup",
          "delay": 11.667537
      },
      "skate": {
          "emote": "emote-iceskating",
          "delay": 7.299156
      },
      "boxer": {
          "emote": "emote-boxer",
          "delay": 5.555702
      },
      "tired": {
          "emote": "emote-tired",
          "delay": 10
      },
      "dance": {
          "emote": "dance-macarena",
          "delay": 12.5
      },
      "loopsit": {
          "emote": "idle-loop-sitfloor",
          "delay": 10
      },
      "weird": {
          "emote": "dance-weird",
          "delay": 22
      },
      "laugh": {
          "emote": "emote-laughing",
          "delay": 3
      },
      "kiss": {
          "emote": "emote-kiss",
          "delay": 3
      },
      "wave": {
          "emote": "emote-wave",
          "delay": 10
      },
      "teleport": {
          "emote": "emote-teleporting",
          "delay": 12.5
      },
      "hot": {
          "emote": "emote-hot",
          "delay": 4.8
      },
      "shopping": {
          "emote": "dance-shoppingcart",
          "delay": 5
      },
      "greedy": {
          "emote": "emote-greedy",
          "delay": 4.8
      },
      "float": {
          "emote": "emote-float",
          "delay": 9.3
      },
      "celebrate": {
          "emote": "emoji-celebrate",
          "delay": 4
      },
      "wop": {
          "emote": "dance-tiktok11",
          "delay": 11
      },
      "swordfight": {
          "emote": "emote-swordfight",
          "delay": 6
      },
      "sexy": {
            "emote": "dance-sexy",
            "delay": 6
        },

      "shy": {
          "emote": "emote-shy",
          "delay": 10
      },
      "tiktok2": {
          "emote": "dance-tiktok2",
          "delay": 11
      },
      "charging": {
          "emote": "emote-charging",
          "delay": 8.5
      },
      "worm": {
          "emote": "emote-snake",
          "delay": 6
      },
      "russian": {
          "emote": "dance-russian",
          "delay": 10.3
      },
      "sad": {
          "emote": "emote-sad",
          "delay": 10
      },
      "cursing": {
          "emote": "emoji-cursing",
          "delay": 2.5
      },
      "flex": {
          "emote": "emoji-flex",
          "delay": 3
      },
      "gagging": {
          "emote": "emoji-gagging",
          "delay": 6
      },
      "tiktok8": {
          "emote": "dance-tiktok8",
          "delay": 11
      },
      "kpop": {
          "emote": "dance-blackpink",
          "delay": 7
      },
      "pennywise": {
          "emote": "dance-pennywise",
          "delay": 1.5
      },
      "bow": {
          "emote": "emote-bow",
          "delay": 3.3
      },
      "curtsy": {
          "emote": "emote-curtsy",
          "delay": 2.8
      },
      "snowangel": {
          "emote": "emote-snowangel",
          "delay": 6.8
      },
      "energyball": {
          "emote": "emote-energyball",
          "delay": 8.3
      },
      "frog": {
          "emote": "emote-frog",
          "delay": 15
      },
      "cute": {
          "emote": "emote-cute",
          "delay": 7.3
      },
      "tiktok9": {
          "emote": "dance-tiktok9",
          "delay": 13
      },
      "shuffle": {
          "emote": "dance-tiktok10",
          "delay": 9
      },
      "pose7": {
          "emote": "emote-pose7",
          "delay": 5.3
      },
      "pose8": {
          "emote": "emote-pose8",
          "delay": 4.6
      },
      "casual": {
          "emote": "idle-dance-casual",
          "delay": 9.7
      },
      "pose1": {
          "emote": "emote-pose1",
          "delay": 3
      },
      "pose3": {
          "emote": "emote-pose3",
          "delay": 4.7
      },
      "pose5": {
          "emote": "emote-pose5",
          "delay": 5
      },
      "cutey": {
          "emote": "emote-cutey",
          "delay": 3.5
      },
      "model": {
          "emote": "emote-model",
          "delay": 6.3
      },
      "astro": {
          "emote": "emote-astronaut",
          "delay": 0
      },  # No delay specified, set to 0
      "guitar": {
          "emote": "emote-punkguitar",
          "delay": 10
      },
      "fashionista": {
          "emote": "emote-fashionista",
          "delay": 6
      },
      "uwu": {
          "emote": "idle-uwu",
          "delay": 25
      },
      "wrong": {
          "emote": "dance-wrong",
          "delay": 13
      },
      "sayso": {
          "emote": "idle-dance-tiktok4",
          "delay": 16
      },
      "maniac": {
          "emote": "emote-maniac",
          "delay": 5.5
      },
      "enthused": {
          "emote": "idle-enthusiastic",
          "delay": 16.5
      },
      "happy": {
          "emote": "emote-happy",
          "delay": 0
      },  # No delay specified, set to 0
      "timejump": {
          "emote": "emote-timejump",
          "delay": 1.9
      },  # No delay specified, set to 0
      "creepy": {
          "emote": "dance-creepypuppet",
          "delay": 10
      },
      "sleigh": {
          "emote": "emote-sleigh",
          "delay": 9
      },  # No delay specified, set to 0
      "singing": {
          "emote": "idle_singing",
          "delay": 12
      },
      "anime": {
          "emote": "dance-anime",
          "delay": 8.4
      },  # No delay specified, set to 0
      "hyped": {
          "emote": "emote-hyped",
          "delay": 6.7
      },  # No delay specified, set to 0
      "jingle": {
          "emote": "dance-jinglebell",
          "delay": 11.8
      },  # No delay specified, set to 0
      "snowball": {
          "emote": "emote-snowball",
          "delay": 6
      },
      "cutesalute": {
          "emote": "emote-cutesalute",
          "delay": 22.321055
      },
      "enthused": {
          "emote": "idle-enthusiastic",
          "delay": 15.941537
      },
      "salute": {
          "emote":"emote-salute",
          "delay": 3
      },
      "pushit": {
          "emote": "dance-employee",
          "delay": 8
      },
      "gift": {
          "emote": "emote-gift",
          "delay": 5.8
      },
      "touch": {
          "emote": "dance-touch",
          "delay": 10.000
      },
      "creepycute": {
          "emote": "emote-creepycute",
          "delay": 7.902453
      },
      "kawai": {
          "emote": "dance-kawai",
          "delay": 7.9
      },
      "scritchy": {
          "emote":"idle-wild",
          "delay": 26.422824},
      "nervous":
      {"emote":"idle-nervous",
      'delay': 21.714221},
      "toilet":
        {"emote":"idle-toilet",
        'delay': 32.174447},

      "superpose":
        {"emote":"emote-superpose",
        'delay': 4.530791}
  }

  async def send_emote_continuously(self, emote_data: dict,
                                    user_id: int) -> None:
    try:
      while user_id in self.user_loops:
        await self.highrise.send_emote(emote_data["emote"], user_id)
        await asyncio.sleep(emote_data["delay"])
    except asyncio.CancelledError:
      pass
    except Exception as e:
      print(f"An error occurred in send_emote_continuously: {e}")
      self.user_loops.pop(user_id, None)

  def _get_emote_commands_list(self):
    emotes_list = list(self.emote_dict.keys())
    unique_emotes = set(emotes_list)  # To ensure there are no duplicates
    formatted_list = ', '.join(unique_emotes)
    return f"You can use the following emotes: {formatted_list}. Just type the emote you want to use in the chat!"

# OK THIS ONE IS FOR MAKING EVRYON IN ROOM EMOTE YOU JUST WHISPER TO BOT EMOTE NAME 
  async def on_whisper(self, user: User, message: str) -> None:
    print(f"[WHISPER] {user.username}: {message}")
    if user.username in vip:
      message = message.strip().lower()
      if message == "stop":
        # Cancel all ongoing loops for all users
        for _user_id, loop_data in list(self.user_loops.items()):
          loop_data['loop'].cancel()
        self.user_loops = {}  # Clear the loops dictionary
      else:
        words = message.split()
        if words and words[0] in self.emote_dict:
          command = self.emote_dict[words[0]]
          if len(words) > 1 and words[1] == "loop":
            # Loop command detected, initiate emote loop for all users
            room_users_res = await self.highrise.get_room_users()
            for item in room_users_res.content:
              room_user = item[0]
              if room_user.id not in self.user_loops:
                loop_task = asyncio.create_task(
                    self.send_emote_continuously(command, room_user.id))
                self.user_loops[room_user.id] = {
                    'command': command,
                    'loop': loop_task
                }
            # Notify all users that the emote loop has started
            await self.highrise.chat(
                f"Emote loop for '{words[0]}' started by {user.username}.")
          elif not words[1:]:
            # If no additional commands after the emote, send it once
            room_users_res = await self.highrise.get_room_users()
            for item in room_users_res.content:
              room_user = item[0]
              await self.highrise.send_emote(command["emote"], room_user.id)

# I COMMENTED THE CODE BELOW BECAUSE IT HELPS TRACK USERS POSITIONS SO I CAN COPY AND SET NEW POSITION FOR BOT

  # async def on_user_move(self, user: User, pos: Position) -> None:
  #     print (f"{user.username} moved to {pos}")



# THIS IS FOR REMOVING BOTS CLOTHES LOL
  async def on_chat(self, user: User, message: str) -> None:
      if message.startswith("/remove") and user.username :
          await remove(self, user, message)
        #   THIS IS FOR EQUIPING NEW BOT ITEMS OR CLOTHES YOU SAY /equip item <name> 
      if message.startswith("/equip") and user.username == "iced_yu":
          await equip(self, user, message)
      if user.username in vip:
          # Split the message to get the command and selected users
          operation = message.split('@')
          command = operation[0].strip()
          selected_users = [u.strip() for u in operation[1:]]

          # Handle emote commands
          if command.startswith("!") and command[1:] in self.emote_dict:
              emote_name = command[1:]  # Remove '!' from the command to get the emote name
              command_info = self.emote_dict[emote_name]

              # Send emote to all targeted users
              target_users = await self.get_users(selected_users, user)
              for target_user in target_users:
                  await self.highrise.send_emote(command_info["emote"], target_user.id)

      if message.startswith("!wallet") and user.username in vip:
          wallet = (await self.highrise.get_wallet()).content
          await self.highrise.chat(f"The bot wallet contains {wallet[0].amount} {wallet[0].type}")

# OK RAY THIS ONLY WORKS FOR ROOM ONWER ONLY YOU CAN ADD PEOPLE AS MOD IN ROOOMS REPLACE TEXT IN WUOTES WITH USERNAME
      if message.startswith("!promote"):
          if user.username != "YOUR USERNAME HERE":
              await self.highrise.chat("You do not have permission to use this command.")
              return

          parts = message.split()
          if len(parts) != 3:
              await self.highrise.chat("Invalid promote command format.")
              return

          command, username, role = parts
          if "@" in username:
              username = username[1:]  # Remove '@' if present

          if role.lower() not in ["moderator", "designer"]:
              await self.highrise.chat("Invalid role, please specify a valid role.")
              return

          # Check if user is in the room
          room_users = (await self.highrise.get_room_users()).content
          user_id = None
          for room_user, pos in room_users:
              if room_user.username.lower() == username.lower():
                  user_id = room_user.id
                  break

          if user_id is None:
              await self.highrise.chat("User not found, please specify a valid user.")
              return

          # Promote user
          permissions = await self.highrise.get_room_privilege(user_id)
          setattr(permissions, role.lower(), True)
          try:
              await self.highrise.change_room_privilege(user_id, permissions)
              await self.highrise.chat(f"{username} has been promoted to {role}.")
          except Exception as e:
              await self.highrise.chat(f"Error: {e}")
              return

      if message.startswith("!demote"):
          if user.username in vip:
              await self.highrise.chat("You do not have permission to use this command.")
              return

          parts = message.split()
          if len(parts) != 3:
              await self.highrise.chat("Invalid demote command format.")
              return

          command, username, role = parts
          if "@" in username:
              username = username[1:]  # Remove '@' if present

          if role.lower() not in ["moderator", "designer"]:
              await self.highrise.chat("Invalid role, please specify a valid role.")
              return

          # Check if user is in the room
          room_users = (await self.highrise.get_room_users()).content
          user_id = None
          for room_user, pos in room_users:
              if room_user.username.lower() == username.lower():
                  user_id = room_user.id
                  break

          if user_id is None:
              await self.highrise.chat("User not found, please specify a valid user.")
              return

          # Demote user
          permissions = await self.highrise.get_room_privilege(user_id)
          setattr(permissions, role.lower(), False)
          try:
              await self.highrise.change_room_privilege(user_id, permissions)
              await self.highrise.chat(f"{username} has been demoted from {role}.")
          except Exception as e:
              await self.highrise.chat(f"Error: {e}")
              return

      message = message.strip()
      print(user.username + ": " + message)
      operation = message.split('@')
      command = operation[0].strip()
      selected_users = [u.strip() for u in operation[1:]]

      if message.strip() == "!commands":
          vip_commands_list = "\n".join([
              "!teleport - Teleport to a specific location",
              "!down - Teleport down",
              "!vip - Teleport to a VIP area",
              "!bar - Teleport to the bar"
              # Add more commands as needed
          ])
          await self.highrise.send_whisper(user.id, f"Here are the VIP commands:\n{vip_commands_list}")

      if command == "!summon" and selected_users:
          if user.username in vip:  # Check if the user is a VIP
              target_username = selected_users[0]
              # Get the position of the user who issued the command
              current_users = await self.highrise.get_room_users()
              issuing_user_position = None
              target_user_id = None

              for current_user, pos in current_users.content:
                  if current_user.username == user.username:
                      if isinstance(pos, Position):
                          issuing_user_position = pos
                  if current_user.username == target_username:
                      target_user_id = current_user.id

              if issuing_user_position and target_user_id:
                  # Teleport the target user to the position of the issuing user
                  await self.highrise.teleport(target_user_id, issuing_user_position)
                  print(f"Teleported {target_username} to {user.username}'s position")
              else:
                  print(f"Could not find valid positions for users: {user.username} or {target_username}")
          else:
              print(f"{user.username} does not have permission to use !summon")

      else:
          target_users = await self.get_users(selected_users, user)
          for target_user in target_users:
              if command == "!teleport" and user.username in vip:
                  await self.highrise.teleport(target_user.id, self.user_teleport_position2)
              elif command == "!down" and user.username in vip:
                  await self.highrise.teleport(target_user.id, self.user_teleport_position)
              elif command == "!vip" and user.username in vip:
                  await self.highrise.teleport(target_user.id, self.user_teleport_position3)
              elif command == "!bar" and user.username in vip:
                  await self.highrise.teleport(target_user.id, self.bar)

      if message == "emotes":
          emotes_list = list(self.emote_dict.keys())
          chunk_size = 10  # This is an example, adjust the chunk size based on the game's limits
          chunks = [emotes_list[i:i + chunk_size] for i in range(0, len(emotes_list), chunk_size)]
          for chunk in chunks:
              emote_message = ', '.join(chunk)
              await self.highrise.send_whisper(user.id, emote_message)
              await asyncio.sleep(1)

      elif message.lower() == "stop":
          # Handle stop command in a case-insensitive manner
          loop_data = self.user_loops.pop(user.id, None)
          if loop_data is not None:
              loop_data['loop'].cancel()

      else:
          words = message.split()
          if len(words) >= 3 and words[0] == "!emote" and words[1] in self.emote_dict:
              emote_name = words[1]
              mention_username = words[2].strip('@')

              # Find user ID based on username
              mention_user = await self.highrise.get_user_by_name(mention_username)

              if mention_user:
                  emote_data = self.emote_dict[emote_name]
                  await self.highrise.send_emote(emote_data["emote"], mention_user.id)
              else:
                  await self.highrise.send_whisper(user.id, f"User {mention_username} not found.")
          elif len(words) >= 1 and words[0] in self.emote_dict:
              command = self.emote_dict[words[0]]
              if "loop" in words:
                  # Check if there is already an active loop for the user
                  if user.id in self.user_loops:
                      # If there's an existing loop, cancel it before starting a new one
                      self.user_loops[user.id]['loop'].cancel()
                  # Start a new loop
                  loop_task = asyncio.create_task(self.send_emote_continuously(command, user.id))
                  self.user_loops[user.id] = {'command': command, 'loop': loop_task}
              else:
                  # Send the emote only once if the message contains only the emote name
                  await self.highrise.send_emote(command["emote"], user.id)

          if message.startswith("!kick"):
              if user.username in vip:
                  pass
              else:
                  await self.highrise.chat("You do not have permission to use this command.")
                  return
              # Separate message into parts
              parts = message.split()
              # Check if message is valid "kick @username"
              if len(parts) != 2:
                  await self.highrise.chat("Invalid kick command format.")
                  return
              # Checks if there's a @ in the message
              if "@" not in parts[1]:
                  username = parts[1]
              else:
                  username = parts[1][1:]
              # Check if user is in room
              room_users = (await self.highrise.get_room_users()).content
              for room_user, pos in room_users:
                  if room_user.username.lower() == username.lower():
                      user_id = room_user.id
                      break
              if "user_id" not in locals():
                  await self.highrise.chat("User not found, please specify a valid user and coordinate")
                  return
              # Kick user
              try:
                  await self.highrise.moderate_room(user_id, "kick")
              except Exception as e:
                  await self.highrise.chat(f"{e}")
                  return
              # Send message to chat
              await self.highrise.chat(f"{username} has been kicked from the room.")


# OK CHECK TEXT IN QUOTES, FIRST LINE AND REPLACE WITH YOR USERNAME
      if message.lower().startswith("!tipme ") and user.username=="USERNAME HERE":
            try:
                amount_str = message.split(" ")[1]
                amount = int(amount_str)
                bars_dictionary = {
                    10000: "gold_bar_10k",
                    5000: "gold_bar_5000",
                    1000: "gold_bar_1k",
                    500: "gold_bar_500",
                    100: "gold_bar_100",
                    50: "gold_bar_50",
                    10: "gold_bar_10",
                    5: "gold_bar_5",
                    1: "gold_bar_1"
                }
                fees_dictionary = {
                    10000: 1000,
                    5000: 500,
                    1000: 100,
                    500: 50,
                    100: 10,
                    50: 5,
                    10: 1,
                    5: 1,
                    1: 1
                }
                # Get bot's wallet balance
                bot_wallet = await self.highrise.get_wallet()
                bot_amount = bot_wallet.content[0].amount
                # Check if bot has enough funds
                if bot_amount < amount:
                    await self.highrise.chat("Not enough funds in the bot's wallet.")
                    return
                # Convert amount to bars and calculate total
                tip = []
                total = 0
                for bar in sorted(bars_dictionary.keys(), reverse=True):
                    if amount >= bar:
                        bar_amount = amount // bar
                        amount %= bar
                        tip.extend([bars_dictionary[bar]] * bar_amount)
                        total += bar_amount * bar + fees_dictionary[bar]
                if total > bot_amount:
                    await self.highrise.chat("Not enough funds to tip the specified amount.")
                    return
                # Send tip to the user who issued the command
                for bar in tip:
                    await self.highrise.tip_user(user.id, bar)
                await self.highrise.chat(f"You have been tipped {amount_str}.")
            except (IndexError, ValueError):
                await self.highrise.chat("Invalid tip amount. Please specify a valid number.")

# Check the first line after this remove the text and add your username in the quotes where i wrote "username here"

      if message.lower().startswith("!tipall ") and user.username == "username here":
          parts = message.split(" ")
          if len(parts) != 2:
              await self.highrise.send_message(user.id, "Invalid command")
              return
          # Checks if the amount is valid
          try:
              amount = int(parts[1])
          except:
              await self.highrise.chat("Invalid amount")
              return
          # Checks if the bot has the amount
          bot_wallet = await self.highrise.get_wallet()
          bot_amount = bot_wallet.content[0].amount
          if bot_amount < amount:
              await self.highrise.chat("Not enough funds")
              return
          # Get all users in the room
          room_users = await self.highrise.get_room_users()
          # Check if the bot has enough funds to tip all users the specified amount
          total_tip_amount = amount * len(room_users.content)
          if bot_amount < total_tip_amount:
              await self.highrise.chat("Not enough funds to tip everyone")
              return
          # Tip each user in the room the specified amount
          for room_user, pos in room_users.content:
              bars_dictionary = {
                  10000: "gold_bar_10k",
                  5000: "gold_bar_5000",
                  1000: "gold_bar_1k",
                  500: "gold_bar_500",
                  100: "gold_bar_100",
                  50: "gold_bar_50",
                  10: "gold_bar_10",
                  5: "gold_bar_5",
                  1: "gold_bar_1"
              }
              fees_dictionary = {
                  10000: 1000,
                  5000: 500,
                  1000: 100,
                  500: 50,
                  100: 10,
                  50: 5,
                  10: 1,
                  5: 1,
                  1: 1
              }
              # Convert the amount to a string of bars and calculate the fee
              tip = []
              remaining_amount = amount
              for bar in bars_dictionary:
                  if remaining_amount >= bar:
                      bar_amount = remaining_amount // bar
                      remaining_amount = remaining_amount % bar
                      for i in range(bar_amount):
                          tip.append(bars_dictionary[bar])
                          total = bar + fees_dictionary[bar]
              if total > bot_amount:
                  await self.highrise.chat("Not enough funds")
                  return
              for bar in tip:
                  await self.highrise.tip_user(room_user.id, bar)


bot_file_name = "main"
bot_class_name = "Bot"
room_id = "Your room id"
bot_token = "Your bot api token"

my_bot = BotDefinition(
    getattr(import_module(bot_file_name), bot_class_name)(), room_id,
    bot_token)

while True:
  try:
    definitions = [my_bot]
    arun(main(definitions))
  except Exception as e:
    print(f"An exception occourred: {e}")
    time.sleep(2)
