import os

from disnake.ext import commands
import disnake

GLOBAL_COLOR = 0x2c6bd0

bot = commands.Bot(
    command_prefix="'",
    intents=disnake.Intents.all(),
    activity=disnake.Game("Collecting information!"),
)
bot.remove_command("help")

if __name__ == '__main__':
    try:
        bot.load_extensions("./cogs")
        print("Success! cogs loaded.")
    except Exception as error:
        print("Error!\n", error)

    bot.run(os.environ.get("BOT_TOKEN"))
