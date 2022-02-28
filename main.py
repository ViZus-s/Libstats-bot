# -------------------------- imports
import os
import disnake
from disnake.ext import commands
# -------------------------- global color
glcolor = 0x060a5d
# -------------------------- cogs
cogss = {
    'server',
    'events',
    'dev',
    'slash_cmds',
}
# -------------------------- bot settings
bot = commands.Bot(command_prefix="'",
                intents=disnake.Intents.all(),
                activity=disnake.Game("Collecting information!"),
                test_guilds=[808030843078836254])
bot.remove_command("help")
# -------------------------- set
if __name__ == '__main__':
    for cog in os.listdir("./cogs"):
        if cog.endswith(".py"):
            try:
                cog = f"cogs.{cog.replace('.py', '')}"
                bot.load_extension(cog)

            except Exception as e:
                print(f"{cog} Can not be loaded\n")
                print(f"{e}\n")

            else:
                print("{} has been succesfully Loaded.".format(cog))
    # -------------------------- get token and start bot
    bot.run(os.environ.get("BOT_TOKEN"))