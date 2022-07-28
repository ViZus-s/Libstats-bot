all_links = {
    "disnake": 
"""
`Disnake GitHub & PyPi & Website:`
**GitHub:**
https://github.com/DisnakeDev/disnake
**PyPi:**
https://pypi.org/project/disnake
**Website:**
https://disnake.dev

`Disnake Documentation & Guide:`
**Docs:**
https://docs.disnake.dev/en/stable/
**Guide:**
https://guide.disnake.dev

`Disnake Discord:`
**Support server:**
https://discord.gg/disnake
**Russian support server:**
https://discord.gg/RrpKVNuRCc
""",

    "nextcord": 
"""
`Nextcord GitHub & PyPi & Website:`
**GitHub:**
https://github.com/nextcord/nextcord
**PyPi:**
https://pypi.org/project/nextcord
**Website:**
https://nextcord.dev

`Nextcord Documentation:`
**Documentation:**
https://docs.nextcord.dev/en/stable

`Nextcord Discord:`
**Support server:**
https://discord.gg/nextcord

""",

    "pycord":
"""
`Pycord GitHub & PyPi & Website:`
**GitHub:**
https://pycord.dev/github
**PyPi:**
https://pypi.org/project/py-cord
**Website:**
https://pycord.dev

`Pycord Documentation & Guide:`
**Documentation:**
https://docs.pycord.dev/en/master
**Guide:**
https://guide.pycord.dev

`Pycord Discord:`
**Support server:**
https://discord.gg/pycord

`Other links:`
**Subreddit:**
https://www.reddit.com/r/pycord/
**Mod Application:**
https://pycord.dev/apply
**Ban Appeal Form:**
https://pycord.dev/appeal
""",

    "discord.py": 
"""
`Discord.py GitHub & PyPi:`
**GitHub:**
https://github.com/Rapptz/discord.py
**Pypi:**
https://pypi.org/project/discord.py

`Discord.py Documentation:`
**Documentation:**
https://discordpy.readthedocs.io/en/stable

`Discord.py Discord:`
**Support server:**
https://discord.gg/dpy
""",

    "interactions.py":
"""
`Interactions.py GitHub & PyPi & Website:`
**GitHub:**
https://github.com/interactions-py/library
**PyPi:**
https://pypi.org/project/discord-py-interactions
**Website:**
https://interactions.i0.gg or https://interactions-py.carrd.co

`Interactions.py Documentation:`
**Documentation:**
https://interactionspy.readthedocs.io

`Interactions.py Discord:`
**Support server:**
https://discord.gg/interactions

`Other links:`
**Twitter:**
https://twitter.com/interactionspy
**Official How-To/Tutorial Playlist:**
https://www.youtube.com/watch?v=QNCXHq8b1EI&list=PLnI02ssmcTo3qChwe5_tRyILLqrAExZlo
""",

    "hikari":
"""
`Hikari GitHub & PyPi & Website:`
**GitHub:**
https://github.com/hikari-py/hikari
**Pypi:**
https://pypi.org/project/hikari
**Website:**
https://www.hikari-py.dev

`Hikari Documentation:`
**Documentation:**
https://www.hikari-py.dev/hikari/index.html

`Hikari Discord:`
**Support server:**
https://discord.gg/hikari
""",
}

def get_links(library: str) -> str:
    
    return all_links[library]
