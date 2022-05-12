import requests
import time

print("Starting Basic Sync Experiment")
start_time = time.time()

for number in range(1, 151):
    url = f'https://pokeapi.co/api/v2/pokemon/{number}'
    resp = requests.get(url)
    pokemon = resp.json()
    # print(pokemon['name'])

print("Basic Sync--- %s seconds ---" % (time.time() - start_time))