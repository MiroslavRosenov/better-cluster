import asyncio
from discord.ext.cluster import Cluster

if __name__ == "__main__":
    cluster = Cluster()
    asyncio.run(cluster.start())