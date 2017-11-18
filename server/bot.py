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
        self.add_command(Command('cleanup', self.cleanup))

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
        guild = ctx.guild
        author = ctx.author

        if guild not in self.games:
            self.games[guild] = salem.Game(guild)

        if not self.games[guild].state:
            await self.games[guild].add_player(salem.Player(author))

            if len(self.games[guild].players) >= 1:
                await self.start_game(ctx)
                await self.games[guild].start_game()

                #debug stuff
                for k, v in self.games.items():
                    print(k, v)
                    for player in self.games[k].players:
                        print(player.user)

        else: await ctx.send("Fuck you koki, a game has started.")

    async def start_game(self, ctx):
        guild = ctx.guild
        game = self.games[guild]

        salem_category = await guild.create_category('salem')

        for player in game.players:
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False),
                guild.get_member(player.user.id): discord.PermissionOverwrite(read_messages=True)
            }

            await guild.create_text_channel('general', overwrites=overwrites, category=salem_category)
        await game.start_game()

    async def cleanup(self, ctx):
        guild = ctx.guild
        channels = guild.by_category()

        for item in channels:
            try:
                if item[0].name == 'salem':
                    for channel in item[1]:
                        await channel.delete()

                    await item[0].delete()

            except (AttributeError, TypeError) as e:
                pass

        try: del self.games[guild]
        except: await ctx.send("You tried to clean nothing! (You must be very smart!)")

bot = Bot(command_prefix='!')
bot.run(bot.token)
