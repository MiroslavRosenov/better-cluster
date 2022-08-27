# Better Cluster

## A high-performance inter-process communication library designed to handle communication between multiple bots/web applications

<img src="https://raw.githubusercontent.com/MiroslavRosenov/better-cluster/main/images/banner.png">

#### This library is made to handle mulltiple discord clients. If you want something simpler or have only one client, check out [better-ipc](https://github.com/MiroslavRosenov/better-ipc)

# Installation
> ### Stable version
#### For Linux
```shell
python3 -m pip install -U better-cluster
```
#### For Windows
```shell
py -m pip install -U better-cluster
```

> ### Development version
#### For Linux
```shell
python3 -m pip install -U git+https://github.com/MiroslavRosenov/better-cluster
```
#### For Windows
```shell
py -m pip install -U git+https://github.com/MiroslavRosenov/better-cluster
```


# Support

You can join the support server [here](https://discord.gg/Rpg7zjFYsh)

# Examples

## Example of a cluster
```python
import asyncio
from discord.ext.cluster import Cluster

if __name__ == "__main__":
    cluster = Cluster()
    asyncio.run(cluster.start())
```

## Example of a shard
```python
import asyncio
import discord

from discord.ext.cluster import Shard, ClientPayload
from discord.ext import commands

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
```


## Example of web client
```python
from quart import Quart
from discord.ext import cluster

app = Quart(__name__)
ipc = cluster.Client()

@app.route('/')
async def main():
    return await ipc.request("get_user_data", 1, user_id=383946213629624322)

if __name__ == '__main__':
    app.run(port=8000, debug=True)
```
