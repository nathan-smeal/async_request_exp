import aiohttp
import asyncio
import time

start_time = time.time()
import platform
if platform.system()=='Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def get_pokemon(session, url):
    async with session.get(url) as resp:
        pokemon = await resp.json()
        # return pokemon['name']


async def main():

    async with aiohttp.ClientSession() as session:

        tasks = []
        for number in range(1, 151):
            url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            tasks.append(asyncio.ensure_future(get_pokemon(session, url)))

        original_pokemon = await asyncio.gather(*tasks)
        for pokemon in original_pokemon:
            pass
            # print(pokemon)

asyncio.run(main())
print("Advanced Async--- %s seconds ---" % (time.time() - start_time))