from highrise import BaseBot, User, Position, AnchorPosition
from highrise.__main__ import *
import highrise, random, asyncio, json
from emotes import Emotes, Dance_Floor
from pickuplines import PUL
import time


class bot(BaseBot):
    def __init__(self):
        super().__init__()

        self.check_players_task = None

        self.emotesdf = Dance_Floor

        self.emote_tasks = {}

        self.dancer = []
        self.on_dance_floor = []
        self.pos1 = None
        self.pos2 = None

        self.bot_pos = None

    async def on_start(self, session_metadata):

        print("Bot started")

        self.load_loc_data()

        if self.bot_pos:
            await self.highrise.walk_to(Position(16.5 , 0.0 , 12.5 , "FrontRight"))

        asyncio.create_task(self.dance_floor())

    async def on_chat(self, user: User, message: str) -> None:

            print(f"{user.username} said: {message}")
            if message.startswith("!wallet") and user.username == "RayMG":
                  wallet = (await self.highrise.get_wallet()).content
                  await self.highrise.chat(f"The bot wallet contains {wallet[0].amount} {wallet[0].type}")
            if message.lower().startswith("!tipme ") and user.username=="iced_yu":
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


            if message.lower().startswith("!tipall ") and user.username == "RayMG":
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
            elif message.startswith("!df 1"):
                self.pos1 = await self.get_actual_pos(user.id)
                await self.highrise.chat(f"🎵Position 1: [{self.pos1}]")

            elif message.startswith("!df 2"):

                self.pos2 = await self.get_actual_pos(user.id)
                await self.highrise.chat(f"🎵Position 1 : [{self.pos2}]")

            elif message.startswith("!check"):

                await self.highrise.chat(f"🎵All Position: [{self.on_dance_floor}]")

            elif message.startswith("!create"):

                if self.pos1 and self.pos2:
                    await self.create_dance_floor()
                    await self.highrise.chat("✅️Dancefloor created.")
                    self.pos1 = None
                    self.pos2 = None
                else:
                    await self.highrise.chat("❌️Set up the dancefloor first: !dancefloor 1 | !dancefloor 2")



            elif message.startswith("!delete"):

                self.on_dance_floor = []
                await self.highrise.chat("❌️Dancefloor removed.")
                self.save_loc_data()


    async def get_actual_pos(self, user_id):

        room_users = await self.highrise.get_room_users()

        for user, position in room_users.content:
            if user.id == user_id:
                return position



    async def teleport_target_user_to_loc(self, target_username, loc):

        try:
            if target_username:
                target = await self.get_target_user_in_room(target_username)

                if target:

                    if loc:
                        await self.highrise.teleport(target.id, loc)
                        await self.highrise.chat(f"@{target.username} has been successfuly teleported.")
                    else:
                        await self.highrise.chat(f"Target location is not set.")

                else:
                    await self.highrise.chat(f"Username {target_username} is invalid.")
        except Exception as e:
            print(f"teleport_target_user: {e}")

    async def get_target_user_in_room(self, target_username):

        room_users = await self.highrise.get_room_users()
        target_user = next((user for user, _ in room_users.content if user.username == target_username), None)
        return target_user

    async def get_users_in_room(self):

        try:
            room_users = await self.highrise.get_room_users()

            if room_users.content:
                for user in room_users.content:
                    get_user = [user for user, _ in room_users.content]
                    return get_user
            else:
                return []
        except Exception as e:
            print(f"{e}")

    async def get_user_ids_in_room(self):

        try:
            room_users = await self.highrise.get_room_users()

            if room_users.content:
                user_ids = [user.id for user, _ in room_users.content]
                return user_ids
            else:
                return []
        except Exception as e:
            print(f"{e}")

    async def get_emote(self, target) -> None:

        try:
            emote_info = self.emotes.get(target)
            return emote_info
        except ValueError:
            pass

    async def get_emote_df(self, target) -> None:

        try:
            emote_info = self.emotesdf.get(target)
            return emote_info
        except ValueError:
            pass


    async def on_emote(self, user: User, emote_id: str, receiver: User | None) -> None:
        print(f"{user.username} emoted: {emote_id}")

    async def on_user_move(self, user: User, destination: Position | AnchorPosition) -> None:

        try:
            if user:
                user_pos = destination

                # Check if user is in any dance floor area
                if self.on_dance_floor:

                    if isinstance(destination, Position):

                        for dance_floor_info in self.on_dance_floor:

                            if (
                                dance_floor_info[0] <= user_pos.x <= dance_floor_info[1] and
                                dance_floor_info[2] <= user_pos.y <= dance_floor_info[3] and
                                dance_floor_info[4] <= user_pos.z <= dance_floor_info[5]
                            ):

                                if user.id not in self.dancer:
                                    self.dancer.append(user.id)

                                return

                    # If not in any dance floor area
                    if user.id in self.dancer:
                        self.dancer.remove(user.id)
        except Exception as e:
            print(f"on_user_move error: {e}")

    async def create_dance_floor(self):

        # Assuming pos1 and pos2 are set as Position objects
        min_x = min(self.pos1.x, self.pos2.x)
        max_x = max(self.pos1.x, self.pos2.x)
        min_y = min(self.pos1.y, self.pos2.y)
        max_y = max(self.pos1.y, self.pos2.y)
        min_z = min(self.pos1.z, self.pos2.z)
        max_z = max(self.pos1.z, self.pos2.z)

        # Store the square area as a tuple and add it to on_dance_floor list
        dance_floor_pos = (min_x, max_x, min_y, max_y, min_z, max_z)
        self.on_dance_floor.append(dance_floor_pos)
        self.save_loc_data()


    def save_loc_data(self):

        loc_data = {

            'bot_position': {'x': self.bot_pos.x, 'y': self.bot_pos.y, 'z': self.bot_pos.z} if self.bot_pos else None,
            'dance_floor': self.on_dance_floor if self.on_dance_floor else None
        }

        with open('loc_data.json', 'w') as file:
            json.dump(loc_data, file)

    def load_loc_data(self):

        try:
            with open('loc_data.json', 'r') as file:
                loc_data = json.load(file)
                self.bot_pos = Position(**loc_data.get('bot_position')) if loc_data.get('bot_position') is not None else None
                self.on_dance_floor = loc_data.get('dance_floor') if loc_data.get('dance_floor') is not None else []
        except FileNotFoundError:
            pass




    async def dance_floor(self):

        while True:

            try:

                if self.on_dance_floor and self.dancer:

                    ran = random.randint(1, 73)
                    emote_text, emote_time = await self.get_emote_df(ran)
                    emote_time -= 10

                    emote_tasks = [self.highrise.send_emote(emote_text, user_id) for user_id in self.dancer]

                    await asyncio.gather(*emote_tasks)
                    await asyncio.sleep(emote_time)

                await asyncio.sleep(15)

            except Exception as e:
                print(f"{e}")



    async def on_user_join(self, user: User, Position):
        print(f"{user.username} joined the room")

    async def on_user_leave(self, user: User):

        try:
            if user.id in self.dancer:
                self.dancer.remove(user.id)
        except Exception as e:
            print(f"{e}")
