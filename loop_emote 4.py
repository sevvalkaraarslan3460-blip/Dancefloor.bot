import asyncio
from highrise import BaseBot
from highrise.models import User

emote_list: list[tuple[list[str], str, float]] = [
    (['rest', 'REST', 'Rest'], 'sit-idle-cute', 17.06),
    (['zombie', 'ZOMBIE', 'Zombie'], 'idle_zombie', 28.75),
    (['relaxed', 'RElAXED', 'Relaxed'], 'idle_layingdown2', 20.55),
    (['attentive', 'att', 'Attentive'], 'idle_layingdown', 23.55),
    (['sleepy', 'SlEEPY', 'Sleepy'], 'idle-sleep', 22.62),
    (['pouty', 'POUT', 'Pouty', 'Pouty Face'], 'idle-sad', 24.38),
    (['posh', 'POSH', 'Posh'], 'idle-posh', 21.85),
    (['tired', 'Tired', 'Tired'], 'idle-loop-tired', 21.96),
    (['laploop', 'TapLoop', 'TapLoop'], 'idle-loop-tapdance', 6.26),
    (['shy', 'SHY', 'Shy'], 'idle-loop-shy', 16.47),
    (['bummed', 'BUMMED', 'Bummed'], 'idle-loop-sad', 6.05),
    (['Chill', 'chill', "chillin'", "Chillin'"], 'idle-loop-happy', 18.80),
    (['annoyed', 'annoyed', 'Annoyed'], 'idle-loop-annoyed', 17.06),
    (['aerobics', 'aerobic', 'Aerobics'], 'idle-loop-aerobics', 8.51),
    (['lookup', 'Loopup', 'ponder', 'Ponder'], 'idle-lookup', 22.34),
    (['heropose', 'Hero', 'Heropose', 'hero', 'Hero Pose'], 'idle-hero', 21.88),
    (['relaxing', 'RElAXING', 'Relaxing'], 'idle-floorsleeping2', 16.25),
    (['cozynap', 'nap', 'Nap', 'Cozynap', 'Cozy Nap'], 'idle-floorsleeping', 13.00),
    (['enthused', 'enthus', 'Enthused'], 'idle-enthusiastic', 15.94),
    (['beat', 'feelbeat', 'FeelTheBeat'], 'idle-dance-headbobbing', 25.37),
    (['irritated', 'irritat', 'Irritated'], 'idle-angry', 25.43),
    (['fly', 'Fly', 'I Believe I Can Fly'], 'emote-wings', 13.13),
    (['think', 'Think'], 'emote-think', 3.69),
    (['theatrical', 'theatric', 'Theatrical'], 'emote-theatrical', 8.59),
    (['tapdance', 'tap dance', 'TapDance'], 'emote-tapdance', 11.06),
    (['superrun', 'Superrun', 'Super Run'], 'emote-superrun', 6.27),
    (['super punch', 'superpunch', 'Superpunch', 'Super Punch'], 'emote-superpunch', 3.75),
    (['sumo', 'Sumo', 'Sumo Fight'], 'emote-sumo', 10.87),
    (['thumb suck', 'thumbsuck', 'Thumb suck', 'suckthumb'], 'emote-suckthumb', 4.19),
    (['35', 'splits drop', 'Splits drop', 'splits'], 'emote-splitsdrop', 4.47),
    (['36', 'snowball fight', 'Snowball fight', 'snowball'], 'emote-snowball', 5.23),
    (['37', 'snow angel', 'Snow angel', 'angel'], 'emote-snowangel', 6.22),
    (['39', 'secret handshake', 'Secret handshake', 'handshake'], 'emote-secrethandshake', 3.88),
    (['41', 'rope pull', 'Rope pull', 'rope'], 'emote-ropepull', 8.77),
    (['42', 'roll', 'Roll'], 'emote-roll', 3.56),
    (['43', 'rofl', 'ROFL'], 'emote-rofl', 6.31),
    (['44', 'robot', 'Robot'], 'emote-robot', 7.61),
    (['45', 'rainbow', 'Rainbow'], 'emote-rainbow', 2.81),
    (['46', 'proposing', 'Proposing', 'proposal'], 'emote-proposing', 4.28),
    (['47', 'peekaboo', 'Peekaboo'], 'emote-peekaboo', 3.63),
    (['48', 'peace', 'Peace'], 'emote-peace', 5.76),
    (['49', 'panic', 'Panic'], 'emote-panic', 2.85),
    (['51', 'ninja run', 'Ninja run', 'ninja'], 'emote-ninjarun', 4.75),
    (['52', 'night fever', 'Night fever', 'fever'], 'emote-nightfever', 5.49),
    (['53', 'monster fail', 'Monster fail'], 'emote-monster_fail', 4.63),
    (['54', 'model', 'Model'], 'emote-model', 6.49),
    (['55', 'flirty wave', 'Flirty wave', 'flirty'], 'emote-lust', 4.66),
    (['56', 'level up', 'Level up'], 'emote-levelup', 6.05),
    (['57', 'amused', 'Amused'], 'emote-laughing2', 5.06),
    (['58', 'laugh', 'Laugh'], 'emote-laughing', 2.69),
    (['59', 'kiss', 'Kiss'], 'emote-kiss', 2.39),
    (['60', 'super kick', 'Super kick', 'kick'], 'emote-kicking', 4.87),
    (['61', 'jump', 'Jump'], 'emote-jumpb', 3.58),
    (['62', 'judo chop', 'Judo chop'], 'emote-judochop', 2.43),
    (['63', 'imaginary jetpack', 'Imaginary jetpack', 'jetpack'], 'emote-jetpack', 16.76),
    (['64', 'hug yourself', 'Hug yourself', 'hug'], 'emote-hugyourself', 4.99),
    (['65', 'sweating', 'Sweating'], 'emote-hot', 4.35),
    (['66', 'hero entrance', 'Hero entrance', 'hero'], 'emote-hero', 5.00),
    (['68', 'headball', 'Headball'], 'emote-headball', 10.07),
    (['69', 'harlem shake', 'Harlem shake'], 'emote-harlemshake', 13.56),
    (['70', 'happy', 'Happy'], 'emote-happy', 3.48),
    (['71', 'handstand', 'Handstand'], 'emote-handstand', 4.02),
    (['72', 'greedy', 'Greedy'], 'emote-greedy', 4.64),
    (['73', 'graceful', 'Graceful'], 'emote-graceful', 3.75),
    (['74', 'moonwalk', 'Moonwalk'], 'emote-gordonshuffle', 8.05),
    (['75', 'ghost float', 'Ghost float', 'ghost', 'Ghost'], 'emote-ghost-idle', 18.20),
    (['76', 'gangnam style', 'Gangnam style', 'gangnam'], 'emote-gangnam', 7.28),
    (['77', 'frolic', 'Frolic'], 'emote-frollicking', 3.70),
    (['78', 'faint', 'Faint'], 'emote-fainting', 18.42),
    (['79', 'clumsy', 'Clumsy'], 'emote-fail2', 6.48),
    (['80', 'fall', 'Fall'], 'emote-fail1', 5.62),
    (['81', 'face palm', 'Face palm'], 'emote-exasperatedb', 2.72),
    (['82', 'exasperated', 'Exasperated'], 'emote-exasperated', 2.37),
    (['83', 'elbow bump', 'Elbow bump'], 'emote-elbowbump', 3.80),
    (['84', 'disco', 'Disco'], 'emote-disco', 5.37),
    (["85", "blast off", "Blast Off"], "emote-disappear", 6.2),
    (["86", "faint drop", "Faint Drop"], "emote-deathdrop", 3.76),
    (["87", "collapse", "Collapse"], "emote-death2", 4.86),
    (["88", "revival", "Revival"], "emote-death", 6.62),
    (["89", "dab", "Dab"], "emote-dab", 2.72),
    (["90", "curtsy", "Curtsy"], "emote-curtsy", 2.43),
    (["91", "confusion", "Confusion"], "emote-confused", 8.58),
    (["92", "cold", "Cold"], "emote-cold", 3.66),
    (["93", "charging", "Charging"], "emote-charging", 8.03),
    (["94", "bunny hop", "Bunny Hop"], "emote-bunnyhop", 12.38),
    (["95", "bow", "Bow"], "emote-bow", 3.34),
    (["96", "boo", "Boo"], "emote-boo", 4.5),
    (["97", "home run!", "Home Run!"], "emote-baseball", 7.25),
    (["98", "falling apart", "Falling Apart"], "emote-apart", 4.81),
    (["99", "thumbs up", "Thumbs Up"], "emoji-thumbsup", 2.7),
    (["100", "point", "Point"], "emoji-there", 2.06),
    (["101", "sneeze", "Sneeze"], "emoji-sneeze", 3.0),
    (["102", "smirk", "Smirk"], "emoji-smirking", 4.82),
    (["103", "sick", "Sick"], "emoji-sick", 5.07),
    (["104", "gasp", "Gasp"], "emoji-scared", 3.01),
    (["105", "punch", "Punch"], "emoji-punch", 1.76),
    (["106", "pray", "Pray"], "emoji-pray", 4.5),
    (["107", "stinky", "Stinky"], "emoji-poop", 4.8),
    (["108", "naughty", "Naughty"], "emoji-naughty", 4.28),
    (["109", "mind blown", "Mind Blown"], "emoji-mind-blown", 2.4),
    (["110", "lying", "Lying"], "emoji-lying", 6.31),
    (["111", "levitate", "Levitate"], "emoji-halo", 5.84),
    (["112", "fireball lunge", "Fireball Lunge"], "emoji-hadoken", 2.72),
    (["113", "give up", "Give Up"], "emoji-give-up", 5.41),
    (["114", "tummy ache", "Tummy Ache"], "emoji-gagging", 5.5),
    (["115", "flex", "Flex"], "emoji-flex", 2.1),
    (["116", "stunned", "Stunned"], "emoji-dizzy", 4.05),
    (["117", "cursing emote", "Cursing Emote"], "emoji-cursing", 2.38),
    (["118", "sob", "Sob"], "emoji-crying", 3.7),
    (["119", "clap", "Clap"], "emoji-clapping", 2.16),
    (["120", "raise the roof", "Raise The Roof"], "emoji-celebrate", 3.41),
    (["121", "arrogance", "Arrogance"], "emoji-arrogance", 6.87),
    (["122", "angry", "Angry"], "emoji-angry", 5.76),
    (["123", "vogue hands", "Vogue Hands"], "dance-voguehands", 9.15),
    (["124", "tiktok8", "Savage Dance"], "dance-tiktok8", 10.94),
    (["125", "tiktok2", "Don't Start Now"], "dance-tiktok2", 10.39),
    (["126", "yoga flow", "Yoga Flow"], "dance-spiritual", 15.8),
    (["127", "smoothwalk", "Smoothwalk"], "dance-smoothwalk", 5.69),
    (["128", "ring on it", "Ring on It"], "dance-singleladies", 21.19),
    (["129", "let's go shopping", "Let's Go Shopping"], "dance-shoppingcart", 4.32),
    (["130", "russian dance", "Russian Dance"], "dance-russian", 10.25),
    (["131", "robotic", "Robotic"], "dance-robotic", 17.81),
    (["132", "penny's dance", "Penny's Dance"], "dance-pennywise", 1.21),
    (["133", "orange juice dance", "Orange Juice Dance"], "dance-orangejustice", 6.48),
    (["134", "rock out", "Rock Out"], "dance-metal", 15.08),
    (["135", "karate", "Karate"], "dance-martial-artist", 13.28),
    (["136", "macarena", "Macarena"], "dance-macarena", 12.21),
    (["137", "hands in the air", "Hands in the Air"], "dance-handsup", 22.28),
    (["138", "floss", "Floss"], "dance-floss", 21.33),
    (["139", "duck walk", "Duck Walk"], "dance-duckwalk", 11.75),
    (["140", "breakdance", "Breakdance"], "dance-breakdance", 17.62),
    (["141", "k-pop dance", "K-Pop Dance"], "dance-blackpink", 7.15),
    (["142", "push ups", "Push Ups"], "dance-aerobics", 8.8),
    (["143", "hyped", "Hyped"], "emote-hyped", 7.49),
    (["144", "jinglebell", "Jinglebell"], "dance-jinglebell", 11),
    (["145", "nervous", "Nervous"], "idle-nervous", 21.71),
    (["146", "toilet", "Toilet"], "idle-toilet", 32.17),
    (["147", "attention", "Attention"], "emote-attention", 4.4),
    (["148", "astronaut", "Astronaut"], "emote-astronaut", 13.79),
    (["149", "dance zombie", "Dance Zombie"], "dance-zombie", 12.92),
    (["150", "ghost", "Ghost"], "emoji-ghost", 3.47),
    (["151", "heart eyes", "Heart Eyes"], "emote-hearteyes", 4.03),
    (["152", "swordfight", "Swordfight"], "emote-swordfight", 5.91),
    (["153", "timejump", "TimeJump"], "emote-timejump", 4.01),
    (["154", "snake", "Snake"], "emote-snake", 5.26),
    (["155", "heart fingers", "Heart Fingers"], "emote-heartfingers", 4.0),
    (["156", "heart shape", "Heart Shape"], "emote-heartshape", 6.23),
    (["157", "hug", "Hug"], "emote-hug", 3.5),
    (["158", "laugh", "Laugh"], "emote-lagughing", 1.13),
    (["159", "eyeroll", "Eyeroll"], "emoji-eyeroll", 3.02),
    (["160", "embarrassed", "Embarrassed"], "emote-embarrassed", 7.414283),
    (["161", "float", "Float"], "emote-float", 8.995302),
    (["162", "telekinesis", "Telekinesis"], "emote-telekinesis", 10.492032),
    (["163", "sexy dance", "Sexy Dance"], "dance-sexy", 12.30883),
    (["164", "puppet", "Puppet"], "emote-puppet", 16.325823),
    (["165", "fighter idle", "Fighter Idle"], "idle-fighter", 17.19123),
    (["166", "penguin dance", "Penguin Dance"], "dance-pinguin", 11.58291),
    (["167", "creepy puppet", "Creepy Puppet"], "dance-creepypuppet", 6.416121),
    (["168", "sleigh", "Sleigh"], "emote-sleigh", 11.333165),
    (["169", "maniac", "Maniac"], "emote-maniac", 4.906886),
    (["170", "energy ball", "Energy Ball"], "emote-energyball", 7.575354),
    (["171", "singing", "Singing"], "idle_singing", 10.260182),
    (["172", "frog", "Frog"], "emote-frog", 14.55257),
    (["173", "superpose", "Superpose"], "emote-superpose", 4.530791),
    (["174", "cute", "Cute"], "emote-cute", 6.170464),
    (["175", "tiktok9", "TikTok Dance 9"], "dance-tiktok9", 11.892918),
    (["176", "weird dance", "Weird Dance"], "dance-weird", 21.556237),
    (["177", "tiktok10", "TikTok Dance 10"], "dance-tiktok10", 8.225648),
    (["178", "pose 7", "Pose 7"], "emote-pose7", 4.655283),
    (["179", "pose 8", "Pose 8"], "emote-pose8", 4.808806),
    (["180", "casual dance", "Casual Dance"], "idle-dance-casual", 9.079756),
    (["181", "pose 1", "Pose 1"], "emote-pose1", 2.825795),
    (["182", "pose 3", "Pose 3"], "emote-pose3", 5.10562),
    (["183", "pose 5", "Pose 5"], "emote-pose5", 4.621532),
    (["184", "cutey", "Cutey"], "emote-cutey", 3.26032),
    (["185", "punk guitar", "Punk Guitar"], "emote-punkguitar", 9.365807),
    (["186", "zombie run", "Zombie Run"], "emote-zombierun", 9.182984),
    (["187", "fashionista", "Fashionista"], "emote-fashionista", 5.606485),
    (["188", "gravity", "Gravity"], "emote-gravity", 8.955966),
    (["189", "ice cream dance", "Ice Cream Dance"], "dance-icecream", 14.769573),
    (["190", "wrong dance", "Wrong Dance"], "dance-wrong", 12.422389),
    (["191", "uwu", "UwU"], "idle-uwu", 24.761968),
    (["192", "tiktok dance 4", "TikTok Dance 4"], "idle-dance-tiktok4", 15.500708),
    (["193", "advanced shy", "Advanced Shy"], "emote-shy2", 4.989278),
    (["194", "anime dance", "Anime Dance"], "dance-anime", 8.46671),
    (["195", "kawaii", "Kawaii"], "dance-kawai", 10.290789),
    (["196", "scritchy", "Scritchy"], "idle-wild", 26.422824),
    (["197", "ice skating", "Ice Skating"], "emote-iceskating", 7.299156),
    (["198", "surprise big", "Surprise Big"], "emote-pose6", 5.375124),
    (["199", "celebration step", "Celebration Step"], "emote-celebrationstep", 3.353703),
    (["200", "creepycute", "Creepycute"], "emote-creepycute", 7.902453),
    (["201", "frustrated", "Frustrated"], "emote-frustrated", 5.584622),
    (["202", "pose 10", "Pose 10"], "emote-pose10", 3.989871),
    (["203", "rel", "Rel"], "sit-relaxed", 29.889858),
    (["laidback", "laid", "Laid Back"], "sit-open", 24.025963),
    (["205", "star gazing", "Star Gazing"], "emote-stargaze", 1.127464),
    (["206", "slap", "Slap"], "emote-slap", 2.724945),
    (["207", "boxer", "Boxer"], "emote-boxer", 5.555702),
    (["208", "head blowup", "Head Blowup"], "emote-headblowup", 11.667537),
    (["209", "kawaii gogo", "KawaiiGoGo"], "emote-kawaiigogo", 10),
    (["210", "repose", "Repose"], "emote-repose", 1.118455),
    (["211", "tiktok7", "Tiktok7"], "idle-dance-tiktok7", 12.956484),
    (["212", "shrink", "Shrink"], "emote-shrink", 8.738784),
    (["213", "ditzy pose", "Ditzy Pose"], "emote-pose9", 4.583117),
    (["214", "teleporting", "Teleporting"], "emote-teleporting", 11.7676),
    (["215", "touch", "Touch"], "dance-touch", 11.7),
    (["216", "guitar", "Guitar"], "idle-guitar", 12.229398),
    (["217", "this is for you", "This Is For You"], "emote-gift", 5.8),
    (["218", "push it", "Push It"], "dance-employee", 8),
    (["219", "smooch", "Smooch"], "emote-kissing", 5),
    (["220", "wop dance", "Wop Dance"], "dance-tiktok11", 9.5),
    (["221", "cute salute", "Cute Salute"], "emote-cutesalute", 3),
    (["222", "at attention", "At Attention"], "emote-salute", 3),
]

user_last_positions = {}

# Check and start emote loop based on user message
async def check_and_start_emote_loop(self: BaseBot, user: User, message: str):
    cleaned_msg = message.strip().lower()

    # Stop the emote loop if user types 'stop'
    if cleaned_msg in ("stop", "/stop", "!stop", "-stop"):
        if user.id in self.user_loops:
            self.user_loops[user.id]["task"].cancel()
            del self.user_loops[user.id]
            await self.highrise.send_whisper(user.id, "Emote loop stopped. (Type any emote name or number to start again)")
        else:
            await self.highrise.send_whisper(user.id, "You don't have an active emote loop.")
        return

    # Find the emote based on message
    selected = next((e for e in emote_list if cleaned_msg in [a.lower() for a in e[0]]), None)
    if selected:
        aliases, emote_id, duration = selected

        # Cancel any existing loop
        if user.id in self.user_loops:
            self.user_loops[user.id]["task"].cancel()
            
        async def emote_loop():
            try:
                while True:
                    if not self.user_loops[user.id]["paused"]:
                        try:
                            await self.highrise.send_emote(emote_id, user.id)
                        except Exception as e:
                            # يحصل أحيانًا Rate-Limit أو Error عند دخول/خروج أحد
                            print(f"[Loop error {user.username}] {e}")
                    await asyncio.sleep(duration)
            except asyncio.CancelledError:
                pass

        # Create and store the task
        task = asyncio.create_task(emote_loop())
        self.user_loops[user.id] = {
            "paused": False,
            "emote_id": emote_id,
            "duration": duration,
            "task": task
        }

        await self.highrise.send_whisper(
            user.id,
            f"You are now in a loop for emote number {aliases[0]}. (To stop, type 'stop')"
        )
# Pause/resume loop when the same user walks/stops
async def handle_user_movement(self: BaseBot, user: User, pos) -> None:
    # تجاهل لو المستخدم ما عنده loop
    if user.id not in self.user_loops:
        return

    # تجاهل تحرك البوت نفسه
    if user.id == self.user.id:
        return

    # احصل على آخر موقع محفوظ
    old_pos = user_last_positions.get(user.id)

    # سجل الموقع الجديد
    user_last_positions[user.id] = (pos.x, pos.y, pos.z)

    # أول مرة نحفظ فقط ومانسوي شي
    if old_pos is None:
        return

    # إذا فعلاً المستخدم تحرك من مكانه القديم
    if old_pos != (pos.x, pos.y, pos.z):
        self.user_loops[user.id]["paused"] = True

        # ننتظر لحين توقفه ثم نرجع نفعّل اللوب
        await asyncio.sleep(2)
        new_pos = user_last_positions.get(user.id)
        if new_pos == (pos.x, pos.y, pos.z):
            self.user_loops[user.id]["paused"] = False