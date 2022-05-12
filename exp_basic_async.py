import aiohttp
import asyncio
import time
import platform
if platform.system()=='Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
print("Starting Basic Async Experiment")

start_time = time.time()

async def main():

    async with aiohttp.ClientSession() as session:

        for number in range(1, 151):
            pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            async with session.get(pokemon_url) as resp:
                pokemon = await resp.json()
                # print(pokemon['name'])

asyncio.run(main())
print("Basic Async--- %s seconds ---" % (time.time() - start_time))