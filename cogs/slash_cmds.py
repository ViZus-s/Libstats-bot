# imports
import disnake
from disnake import ApplicationCommandInteraction
from disnake.ext import commands
from main import glcolor
from parsers.gitthub import parsing_git, parsing_update
from parsers.pypi import parsing_pypi

class Slashs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(
        name="stats",
        description="Wanna check statistic? Use this command!",
        )
    async def stats(self, inter: ApplicationCommandInteraction, option: str = commands.Param(choices=['pypi', 'github'])):
        if option == 'github':
            Member = inter.author
            get_data = parsing_git()
            
            stars = get_data["stars"]
            forks = get_data["forks"]
            issues = get_data["issues"]
            pull = get_data["pull requests"]
            lastcom = get_data["last commit"]
            
            embed1 = disnake.Embed(title="GitHub Disnake Statistics",
                            description=f":star: **stars**: `{stars}`\n\n:cd: **forks**: `{forks}`\n\n:bangbang: **issues**: `{issues}`\n\n:satellite: **pull requests**: `{pull}`\n\n:hourglass: **last commit**: `{lastcom}`",
                            color=glcolor)
            
            embed1.set_author(name=inter.author.name, icon_url=Member.avatar.url)
            await inter.send(embed=embed1)
            
        elif option == 'pypi':
            Member = inter.author
            get_data = parsing_pypi()
            embed2 = disnake.Embed(
                title="PyPi Disnake Statistics",
                description=f":bulb: **Latest Version**: `{get_data['last_version']}`\n:bar_chart: **Last version downloads**: `{get_data['last_version_downloads']}`\n:chart_with_upwards_trend: **Total downloads**: `{get_data['total_downloads']}`\n:calendar_spiral: **Downloads on {get_data['set']}**: `{get_data['downloads_sum']}`",
                color=glcolor)
            embed2.set_author(name=inter.author.name, icon_url=Member.avatar.url)
            await inter.send(embed=embed2)

    @commands.slash_command(
        name="help",
        description="Shows bot commands",
        )
    async def help(self, inter: ApplicationCommandInteraction):

        embed2 = disnake.Embed(
        title=":book: | Help",
        description="`/stats` - shows any statistics[github/pypi]\n`/info` - shows bot info",
        color=glcolor)
        await inter.send(embed=embed2, ephemeral=True)

    @commands.slash_command(
        name="info",
        description="Shows the bot info",
        )
    async def info(self, inter: ApplicationCommandInteraction):
        Member = inter.author

        embed = disnake.Embed(
            title="Bot information",
            description=f"<:disnake:922937443039186975> **Disnake version**: `{disnake.__version__}`\n:gear: **Bot version**: `1.0`\n:timer: **Ping**: `{round(self.bot.latency * 1000)} ms`\n:envelope_with_arrow: **Last update**: `{parsing_update()}`\n:open_file_folder: **Bot github**: ||https://github.com/ViZus-s/Disnake-Statistics-Bot||",
            color=glcolor)
            
        embed.set_author(name=inter.author.name, icon_url=Member.avatar.url)
        await inter.send(embed=embed)


def setup(bot):
    bot.add_cog(Slashs(bot))
