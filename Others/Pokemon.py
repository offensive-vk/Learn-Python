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

def assign(x: int, y: int) -> int:
    return random.randint(x, y)

def main():

    # Create two Pokemon
    pikachu = Pokemon("", 0, 0, 0, 0)
    charmander = Pokemon("", 0, 0, 0, 0)

    # Initialize Pokemon
    initialize_pokemon(pikachu, "Pikachu", 10, 50, 20, 15)
    # initialize_pokemon(pikachu, "Prime Pikachu", assign(1,10), assign(40,50), assign(10,20), assign(10,15))
    initialize_pokemon(charmander, "Charmander", 10, 45, 18, 12)

    # Display Pokemon information
    print("Initial Pokemon Information:")
    display_pokemon(pikachu)
    display_pokemon(charmander)

    # Simulate a battle between the two Pokemon
    print("Battle Begins!")
    while pikachu.health > 0 and charmander.health > 0:
        # Randomly decide which Pokemon attacks first
        if random.choice([True, False]):
            battle(pikachu, charmander)
            if charmander.health > 0:
                battle(charmander, pikachu)
        else:
            battle(charmander, pikachu)
            if pikachu.health > 0:
                battle(pikachu, charmander)

    # Display the result of the battle
    if pikachu.health <= 0:
        print("Pikachu fainted. Charmander wins!")
    else:
        print("Charmander fainted. Pikachu wins!")

if __name__ == "__main__":
    main()
