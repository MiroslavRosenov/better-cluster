# Better Cluster


<a href="https://pypi.org/project/better-cluster/" target="_blank"><img src="https://img.shields.io/pypi/v/better-cluster"></a>
<img src="https://img.shields.io/pypi/pyversions/better-cluster">
<img src="https://img.shields.io/github/last-commit/MiroslavRosenov/better-cluster">
<img src="https://img.shields.io/github/license/MiroslavRosenov/better-cluster">
<a href="https://discord.gg/Rpg7zjFYsh" target="_blank"><img src="https://img.shields.io/discord/875005644594372638?label=discord"></a>

## A high-performance inter-process communication library designed to handle communication between multiple shards

<img src="https://raw.githubusercontent.com/MiroslavRosenov/better-cluster/main/images/banner.png">

#### This library is made to handle multiple discord clients. If you want something simpler or have only one client, check out [better-ipc](https://github.com/MiroslavRosenov/better-ipc)

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
import logging
from discord.ext.cluster import Cluster

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    cluster = Cluster()
    asyncio.run(cluster.start())
```

## Example of a shard
```python
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
