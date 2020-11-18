#!/usr/bin/env python3

# imports always go at the top of your code
import requests



def main():
    pokeapi = requests.get("https://pokeapi.co/api/v2/pokemon/111").json()

    print(type(pokeapi))


    icon = pokeapi['sprites']['front_default']
    gamesin = len(pokeapi['game_indices'])

    print(icon)
    print(gamesin)

    for x in range(0,len(pokeapi['moves'])+1):
        for move in pokeapi['moves'][x]:
            #print(pokeapi['moves'][x])
            print(move)


main()
