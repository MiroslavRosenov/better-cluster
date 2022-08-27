import asyncio
import discord
import logging

from discord.ext.cluster import Shard, ClientPayload
from discord.ext import commands

logging.basicConfig(level=logging.INFO)

logging.getLogger("discord.http").disabled = True
logging.getLogger("discord.client").disabled = True
logging.getLogger("discord.gateway").disabled = True

class MyBot(commands.Bot):
    def __init__(self) -> None:
        intents = discord.Intents.all()

        super().__init__(
            command_prefix="$.",
            intents=intents
        )

        self.shard = Shard(self, shard_id=1)

    async def setup_hook(self) -> None:
        await self.shard.connect()

    @Shard.route(shard_id=1)
    async def get_user_data(self, data: ClientPayload):
        user = self.get_user(data.user_id)
        return user._to_minimal_user_json()

if __name__ == '__main__':
    bot = MyBot()
    asyncio.run(bot.run(...))