import random
import time

class Pokemon:
    def __init__(self, name, level, health, attack, defense):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack
        self.defense = defense

def initialize_pokemon(pokemon, name, level, health, attack, defense):
    pokemon.name = name
    pokemon.level = level
    pokemon.health = health
    pokemon.attack = attack
    pokemon.defense = defense

def display_pokemon(pokemon):
    print(f"Name: {pokemon.name}")
    print(f"Level: {pokemon.level}")
    print(f"Health: {pokemon.health}")
    print(f"Attack: {pokemon.attack}")
    print(f"Defense: {pokemon.defense}")
    print()

def battle(pokemon1, pokemon2):
    # Simulate a simple battle
    damage = pokemon1.attack - pokemon2.defense
    damage = max(0, damage)  # No negative damage

    # Inflict damage on the opponent
    pokemon2.health -= damage

    # Display battle information
    print(f"{pokemon1.name} attacked {pokemon2.name} and dealt {damage} damage!")
    print(f"{pokemon2.name}'s health: {pokemon2.health}")
    time.sleep(1)  # Introduce a delay for better visualization

    # Check if the opponent is defeated
    if pokemon2.health <= 0:
        print(f"{pokemon2.name} fainted!")
        time.sleep(1)  # Introduce a delay for better visualization

