import asyncio
import logging
from discord.ext.cluster import Cluster

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    cluster = Cluster()
    asyncio.run(cluster.start())