from highrise import BaseBot, User, Position, AnchorPosition
from highrise.__main__ import *
import highrise, random, asyncio, json
from emotes import Emotes, Dance_Floor
from pickuplines import PUL
import time


class MGBot(BaseBot):
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
            await self.highrise.teleport(self.highrise.my_id, self.bot_pos)

        # Ensure the dance_floor task is not already running
        if not self.check_players_task or self.check_players_task.done():
            self.check_players_task = asyncio.create_task(self.dance_floor())

    async def on_chat(self, user: User, message: str) -> None:
        print(f"{user.username} said: {message}")

        # Detect "clap" text or 👏 emoji
        if message.lower() == "clap" or "👏" in message:
            # Clap reaction for the user who sent the message
            await self.highrise.react("clap", user.id)

        # Detect "clap @username" or "👏 @username" command
        elif message.lower().startswith("clap") or message.startswith("👏"):
            parts = message.split(" ")
            if len(parts) == 2:  # Ensure the command has a target user
                target_username = parts[1].lstrip("@")  # Remove "@" if present
                target_user = await self.get_target_user_in_room(target_username)
                
                if target_user:
                    await self.highrise.react("clap", target_user.id)
                else:
                    await self.highrise.chat(f"User {target_username} not found in the room.")

        # If user is a moderator or host and sends "clap all" or "👏 all"
        if (user.is_moderator or user.is_host) and (message.lower() == "clap all" or message == "👏 all"):
            # Clap for all users in the room
            room_users = await self.highrise.get_users_in_room()
            for room_user in room_users:
                await self.highrise.react("clap", room_user.id)
        
        # Additional commands like tipping, setting positions, etc.
        if message.startswith("!wallet") and user.username == "REDEliff", "Ali_wq_":
            wallet = (await self.highrise.get_wallet()).content
            await self.highrise.chat(f"The bot wallet contains {wallet[0].amount} {wallet[0].type}")

        if message.lower().startswith("!tipme ") and user.username == "REDEliff", "Ali_wq_":
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

        if message.lower().startswith("!tipall ") and user.username == "REDEliff", "Ali_wq_":
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
                    
        # Handling dance floor commands, position setting, etc.
        if message.startswith("/pos1"):
            self.pos1 = await self.get_actual_pos(user.id)
            await self.highrise.chat("Position 1 set.")

        elif message.startswith("/pos2"):
            self.pos2 = await self.get_actual_pos(user.id)
            await self.highrise.chat("Position 2 set.")

        elif message.startswith("/check"):
            await self.highrise.chat(f"{self.on_dance_floor}")

        elif message.startswith("/create"):
            if self.pos1 and self.pos2:
                await self.create_dance_floor()
                await self.highrise.chat("Dance floor created.")
                self.pos1 = None
                self.pos2 = None
            else:
                await self.highrise.chat("Please set both Position 1 and Position 2 first.")

        elif message.startswith("/clear-df"):
            self.on_dance_floor = []
            await self.highrise.chat("Dance floor/s removed.")
            self.save_loc_data()

    # Remaining methods for teleportation, dance floor, etc. stay the same.


