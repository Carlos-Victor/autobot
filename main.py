from discord import Intents, utils, AllowedMentions
from discord.ext import commands
from decouple import config

token = config("DISCORD_TOKEN", cast=str)

intents = Intents.default()
intents.members = True
intents.presences = True
intents.guilds = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")


@bot.event
async def on_voice_state_update(member, before, after):
    if member.bot:
        return

    if before.channel is None and after.channel is not None:
        guild = member.guild
        members_channels = [
            member for channel in guild.voice_channels for member in channel.members
        ]
        actual_members = [
            member_channel for member_channel in members_channels if not member_channel.bot
        ]

        if len(actual_members) != 1:
            return

        general_channel = utils.get(guild.text_channels, name="geral")
        await general_channel.send(
            f"{member.mention} Chegou e está Chamando Todos os Autobots\n@everyone",
            allowed_mentions=AllowedMentions(everyone=True),
        )


bot.run(token)
