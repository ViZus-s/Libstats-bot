# imports
import disnake
from disnake.ext import commands


class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Nick#tag = {self.bot.user}")
        print(f"My id = {self.bot.user.id}")
    
    @commands.Cog.listener()
    async def on_message(self, message):
        return

def setup(bot):
    bot.add_cog(events(bot))