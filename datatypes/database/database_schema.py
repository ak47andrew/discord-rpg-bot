from datatypes.database.db_serrialisable import JsonSerializable
from discord.ext import commands


class Character(JsonSerializable):
    a: commands.Bot
