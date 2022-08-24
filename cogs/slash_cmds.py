from sys import version

import disnake
from disnake.ext import commands

from main import GLOBAL_COLOR
from parsers.github import parsing_update

class Slashes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="help",
        description="Shows bot commands.",
    )
    async def help(self, inter: disnake.CommandInter):

        embed2 = disnake.Embed(
            title=":book: | Help",
            description="`/stats_1` - shows any statistics[github/pypi]\n`/stats_2` - shows monthly downloads\n`/info` - shows bot info\n`/links` - shows the links of the selected library",
            color=GLOBAL_COLOR)
        await inter.send(embed=embed2, ephemeral=True)

    @commands.slash_command(
        name="info",
        description="Shows the bot info.",
    )
    async def info(self, inter: disnake.CommandInter):

        embed = disnake.Embed(
            title="Bot information",
            description=f"<:disnake:922937443039186975> **Disnake version**: `{disnake.__version__}`\n<:icon2:983249100558434355> **Python version**: `{version[:6:]}`\n:timer: **Ping**: `{round(self.bot.latency * 1000)} ms`\n:envelope_with_arrow: **Last update**: `{await parsing_update()}`\n:gear: **Lib support**: python libs\n:open_file_folder: **Bot github**: ||https://github.com/ViZus-s/Libstats-bot||",
            color=GLOBAL_COLOR)

        embed.set_author(name=inter.author, icon_url=inter.author.display_avatar.url)
        await inter.send(embed=embed)


def setup(bot):
    bot.add_cog(Slashes(bot))
