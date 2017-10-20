import discord
from discord.ext import commands
import random
import time, os

description = "An example bot to showcase the discord.ext.commands extension module."

bot = commands.Bot(command_prefix='!', description=description)

deaths = {}
users = {}

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-' * len(bot.user.id))

@bot.command()
async def rawr():
    await bot.say("XD")

@bot.command()
async def kill(name: str, *argv: str):
    author = commands.bot._get_variable('_internal_author')

    if author not in users:
        users[author] = time.time() + 86500

    if users[author] - time.time() >= 86400:
        for i in argv:
            name = name + " " + i

        if name not in deaths:
            deaths[name] = 0

        deaths[name] += 1
        users[author] = time.time()
        await bot.say(name + " has died " + str(deaths[name]) + " time(s)")

    else:
        await bot.say("Don't be a greedy bastard, wait " + time.strftime('%H:%M:%S', time.gmtime(86400 - (time.time() - users[author]))))

bot.run(os.environ['DISCORD_KEY'])

"""
@bot.command()
async def add(left : int, right : int):
    await bot.say(left + right)

@bot.command()
async def roll(dice : str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    await bot.say(random.choice(choices))

@bot.command()
async def repeat(times : int, content='repeating...'):
    for i in range(times):
        await bot.say(content)

@bot.command()
async def joined(member : discord.Member):
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))

@bot.group(pass_context=True)
async def cool(ctx):
    if ctx.invoked_subcommand is None:
        await bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='bot')
async def _bot():
    await bot.say('Yes, the bot is cool.')
"""
