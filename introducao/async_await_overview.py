import asyncio

async def sum(a, b):
    return a + b

#coro = sum(2, 3)

async def print_sum(a, b):
    result = await sum(a,b)
    print(f"O resultado é igual a {result}")

print_sum(2, 3)

#EVENT LOOP
event_loop = asyncio.new_event_loop()
event_loop.run_until_complete(print_sum(2, 3))