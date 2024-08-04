# Zombie Survival Game

## Overview
This Python script is a simple text-based game where players control a human character to survive against attacking zombies. The game features basic combat mechanics, health management, and inventory usage.

## Game Classes

### Zombie
The `Zombie` class represents a zombie with specific attributes and methods:
- **Attributes**:
  - `strength`: Determines the zombie's attack power.
  - `health`: Calculated as `strength * 10`.
  - `max_health`: The maximum health a zombie can have (200).
  - `isDecapitated`: Indicates if the zombie is decapitated (True if health is 0).
- **Methods**:
  - `__init__(self, strength)`: Initializes the zombie with a given strength.
  - `__repr__(self)`: Returns a string representation of the zombie's strength and health.
  - `zombie_attack(self, human, defend=False)`: Performs a basic attack on a human, with optional defense.
  - `zombie_bite(self, human, defend=False)`: Performs a stronger bite attack on a human, with optional defense.
  - `defend(self, damage)`: Calculates the reduced damage when the zombie defends.

### Human
The `Human` class represents a human character with specific attributes and methods:
- **Attributes**:
  - `name`: The name of the human.
  - `strength`: Determines the human's attack power and defense capability.
  - `health`: Calculated as `strength * 10`.
  - `max_health`: The maximum health a human can have (200).
  - `inventory`: A list of items the human has collected.
  - `food_values`: A dictionary mapping food items to their health values.
- **Methods**:
  - `__init__(self, name, strength)`: Initializes the human with a given name and strength.
  - `__repr__(self)`: Returns a string representation of the human's name, strength, and health.
  - `human_attack(self, zombie, defend=False)`: Performs a basic attack on a zombie, with optional defense.
  - `defend(self, damage)`: Calculates the reduced damage when the human defends.
  - `search4_food(self)`: Searches for food items and adds them to the inventory.
  - `use_item(self, item)`: Uses an item from the inventory to modify health.

## Game Functions

- `random_character()`: Returns a randomly selected name for a human character.
- `generate_random_strength()`: Generates a random strength value between 1 and 20.
- `add_new_zombie(zombie_list)`: Adds a new zombie with random strength to the list of zombies.
- `new_game()`: Starts a new game with a random human and a list containing one zombie.
- `main()`: The main function to run the game.

## How to Play

1. **Starting the Game**: Run the script to start the game. A new human character with a random name and strength will be created, along with an initial zombie.
2. **Game Options**:
   - **0**: View game facts.
   - **1**: Attack the zombie.
   - **2**: Defend against the zombie.
   - **3**: Search for food.
   - **4**: Check inventory.
   - **5**: Use an item from the inventory.
   - **6**: Add a new zombie.
   - **7**: Start a new game.
   - **8**: Quit the game.
3. **Combat**: Engage in combat by attacking or defending against zombies. Use items to heal or improve your chances of survival.
4. **Inventory Management**: Collect and use items to maintain your health and improve your chances against zombies.

## Example Usage

To start the game, simply run the script:

```bash
python zombie_game.py
