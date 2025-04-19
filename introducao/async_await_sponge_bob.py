# chapar pão
# fritar hamburguer
# montar sanduiche
#fazer milkshake

from time import sleep
import asyncio

class AsyncSpongeBob:
    async def cook_bread(self):
        await asyncio.sleep(3)

    async def cook_hamburger(self):
        await asyncio.sleep(10)

    async def monunt_sandwich(self):
        await asyncio.sleep(3)

    async def make_milkshake(self):
        await asyncio.sleep(5)

    async def make_sandwich(self):
        await asyncio.gather(
            self.cook_bread(),
            self.cook_hamburger(),
        )
        event_loop = asyncio.get_running_loop()
        event_loop.create_task(self.monunt_sandwich())

    async def cook(self):
        await asyncio.gather(self.make_sandwich(),self.make_milkshake())

async_spongebob = AsyncSpongeBob()
asyncio.run(async_spongebob.cook())
print("Pronto")