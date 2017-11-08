import discord
from discord.ext import commands
from discord.ext.commands.core import Command

import salem

import time, os, asyncio, json, atexit

class Bot(commands.Bot):
    def __init__(self, command_prefix, formatter=None, description=None, pm_help=False, **options):
        super().__init__(command_prefix, formatter, description, pm_help, **options)
        self.token = os.environ['DISCORD_KEY']

        #commands
        self.add_command(Command('salem', self.salem))

        #salem
        #{guild_id: game_object}
        self.games = dict()

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('-' * len(str(self.user.id)))
        print(self.commands)

    async def salem(self, ctx):
        if ctx.guild not in self.games:
            self.games[ctx.guild] = salem.Game(ctx.guild)

        await self.games[ctx.guild].add_player(salem.Player(ctx.author))

        if len(self.games[ctx.guild].players) >= 2:
            await self.start_game(ctx)

            #debug stuff
            for k, v in self.games.items():
                print(k, v)
                for player in self.games[k].players:
                    print(player.user)

    async def start_game(self, ctx):
        guild = ctx.guild
        salem_category = await guild.create_category('salem')
        #for player in self.something:

bot = Bot(command_prefix='!')
bot.run(bot.token)
