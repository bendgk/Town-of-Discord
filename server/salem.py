import uuid
import asyncio

class Player:
    def __init__(self, user, name=""):
        self.user = user
        self.name = name
        self.alive = False

class Game:
    def __init__(self, guild):
        self.guild = guild
        self.players = set()
        self.deceased = set()
        self.day = 0
        self.night = False

    async def add_player(self, player):
        self.players.add(player)
        pass

    async def kill(self, player):
        self.alive.remove(player)
        self.deceased.append(player)

    async def new_day(self):
        self.day += 1
        self.night = False

    async def night(self):
        self.night = True
