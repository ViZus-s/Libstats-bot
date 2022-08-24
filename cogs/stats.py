import disnake
from disnake.ext import commands

from main import GLOBAL_COLOR
from other.links import get_links
from parsers.github import parsing_git, parsing_update
from parsers.pypi import parsing_pypi, parsing_downloads

LIBRARIES = ("disnake", "nextcord", "pycord",
             "discord.py", "interactions.py", "hikari")


class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="stats_1",
        description="Shows info about pypi/github.",)
    async def stats_1(self, inter: disnake.CommandInter, platform: str = commands.Param(choices=['pypi', 'github']), library: str = commands.Param(choices=LIBRARIES)):

        member = inter.author
        await inter.response.defer()

        if platform == 'github':
            get_data = await parsing_git(library)

            stars = get_data["stars"]
            forks = get_data["forks"]
            issues = get_data["issues"]
            watching = get_data['watching']
            pull = get_data["pull requests"]
            lastcom = get_data["last commit"]

            embed1 = disnake.Embed(title=f"GitHub {library.capitalize()} Statistics",
                                   description=f":star: **stars**: `{stars}`\n:cd: **forks**: `{forks}`\n:bangbang: **issues**: `{issues}`\n:eyes: **watching**: `{watching}`\n:satellite: **pull requests [OPEN]**: `{pull}`\n:hourglass: **last commit**: {lastcom}",
                                   color=GLOBAL_COLOR)

            embed1.set_author(name=member, icon_url=member.display_avatar.url)
            await inter.send(embed=embed1)

        elif platform == 'pypi':
            try:
                get_data = await parsing_pypi(library)

                last_version1 = get_data[0]['last_version']
                downloads1 = get_data[0]['downloads']
                last_version2 = get_data[1]['last_version']
                last_version_downloads2 = get_data[1]['last_version_downloads']
                total_downloads2 = get_data[1]['total_downloads']
                set2 = get_data[1]['set']
                downloads_sum2 = get_data[1]['downloads_sum']

                embed2 = disnake.Embed(
                    title=f"PyPi {library.capitalize()} Statistics",
                    description=f":satellite: `pypistats`\n:bulb: **Latest Version**: {last_version1}\n:pencil: **Downloads last day:** {downloads1[0]}\n:pencil: **Downloads last week:** {downloads1[1]}\n:pencil: **Downloads last month:** {downloads1[2]}\n\n:satellite: `api-pepy-tech`\n:bulb: **Latest Version**: {last_version2}\n:bar_chart: **Last version downloads**: {last_version_downloads2}\n:chart_with_upwards_trend: **Total downloads**: {total_downloads2}\n:calendar_spiral: **Downloads on {set2}**: {downloads_sum2}\n",
                    color=GLOBAL_COLOR)

                embed2.set_author(name=member,
                                 icon_url=member.display_avatar.url)
                embed2.set_footer(text="Statistics are updated every day.")

                await inter.send(embed=embed2)

            except Exception as error:

                await inter.send("The pypi command is not working.")

    @commands.slash_command(
        name="stats_2",
        description="Shows monthly library downloads.",)
    async def stats_2(self, inter: disnake.CommandInter, library: str = commands.Param(choices=LIBRARIES)):

        await inter.response.defer()

        get_data = await parsing_downloads(library)

        desc = "\n".join(f"`{date}`: **{stats:,d}**" for date,
                         stats in get_data.items())

        embed = disnake.Embed(
            title=F"{library.capitalize()} month downloads",
            description=desc,
            color=GLOBAL_COLOR)

        embed.set_author(name=inter.author,
                         icon_url=inter.author.display_avatar.url)
        embed.set_footer(text="Statistics are updated every day.")

        await inter.send(embed=embed)

    @commands.slash_command(
        name="links",
        description="Shows all selected library links.",
    )
    async def links(self, inter: disnake.CommandInter, library: str = commands.Param(choices=LIBRARIES)):

        embed = disnake.Embed(
            title=f"{library.capitalize()} links",
            description=get_links(library),
            color=GLOBAL_COLOR)

        embed.set_author(name=inter.author,
                         icon_url=inter.author.display_avatar.url)
        await inter.send(embed=embed)


def setup(bot):
    bot.add_cog(Stats(bot))
