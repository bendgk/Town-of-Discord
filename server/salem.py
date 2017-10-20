import uuid
import asyncio

class Player:
    def __init__(self, p_id, name):
        self.id = p_id
        self.name = name
        self.alive = False

class Game:
    def __init__(self):
        self.game_id = uuid.uuid4()
        self.players = []
        self.alive = self.players
        self.deceased = []
        self.player_count = len(self.players)
        self.alive_count = self.player_count
        self.day = 1
        self.night = False

    async def add_player(self):
        pass

    async def kill(self, player):
        self.alive.remove(player)
        self.deceased.append(player)

    async def new_day(self):
        self.day += 1
        self.day()

    async def night(self):
        self.night = True

    async def day(self):
        self.night = False

g = Game()
