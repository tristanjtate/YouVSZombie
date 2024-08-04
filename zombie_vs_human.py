import random as r

class Zombie:
#   creating a zombie to have basic health and strength for each instance, health is determined by strength
    def __init__(self, strength):
        self.strength = strength
        self.health = (strength * 10)
        self.max_health = 200
        self.isDecapitated = False
        if self.health == 0:
            self.isDecapitated = True



    def __repr__(self):
      # printing a zombie will tell you it's strength and how much health it has
        return (f"This Zombie has a {self.strength} strength level and currently has {self.health} health!")


# this is a basic zombie attack
# checks if zombie is already dead...like dead dead
# basic attack will be strength * 3
# will subtract basic attack from human.health
# if human has defend as true then damage is reduce via defend method
    def zombie_attack(self, human, defend = False):
        if self.isDecapitated == False:
            basic_attack = self.strength * 3
            if defend == True:
                damage = human.defend(basic_attack)
                human.health -= damage
                human.health = max(human.health, 0)
                
                if human.health == 0:
                    print(f"{human.name} tried to defend, but just slapped by a Zombie. {human.name} is pretty much dead..or now a Zombie.", end='')
                else:
                    print(f"{human.name} defended, but got slashed by a Zombie. Nice blocking. This hit did {damage} damage.")
                    print(f'{human.name} has {human.health} health now.')
                    
          
            else:
                human.health -= basic_attack
                human.health = max(human.health, 0)
                if human.health == 0:
                    print(f"{human.name} just got SMACKED by this Zombie. They might as well be friends, because {human.name} is now a Zombie too or about to become one real....soon.")
                else:   
                    print(f"{human.name} needs to block, but didn't....they got SMACKED. Don't let it happen again. This hit did {basic_attack} damage.")
                    print(f'{human.name} has {human.health} health now.')
        else: 
            print('Nah, Zombie is decapitated...')


    # checks if zombie is already dead...like dead dead
    # this zombie bite does more damage : strength * 4
    # takes away from human health
    # if human has defend as true then damage is reduce via defend method
    def zombie_bite(self, human, defend = False):
        if self.isDecapitated == False:
            bite = self.strength * 4
            if defend == True:
                damage = human.defend(bite)
                human.health -= damage
                human.health = max(human.health, 0)
                
                if human.health == 0:
                    print(f"{human.name} tried to defend, but just got bit by this Zombie. They might as well be friends, because {human.name} is now a Zombie too or about to become one real....soon.", end='')
                else:
                    print(f"{human.name} defended, but got a nasty bite from this Zombie. Don't let it happen again. This bite did {damage} damage.")
                    print(f'{human.name} has {human.health} health now.')
                    
            else:
                human.health -= bite
                human.health = max(human.health, 0)
                if human.health == 0:
                    print(f"{human.name} just got bit by this Zombie. They might as well be friends, because {human.name} is now a Zombie too or about to become one real....soon.")
                else:
                    print(f"{human.name} needs to block, but didn't....they got a nasty bite from this Zombie. Don't let it happen again. This bite did {bite} damage.")
                    print(f'{human.name} has {human.health} health now.')
                
        else: 
            print('Nah, Zombie is decapitated')
            
            
    # defend will be dependent on strength
    def defend(self, damage):
        damage_after_defend = damage - self.strength
        return damage_after_defend

      



class Human:
  #  creating a human for each instance : name and strength, health and max health is determined by strength
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength
        self.health = strength * 10
        self.max_health = 200
        self.inventory = []
        self.food_values = {
            'apple': 5,
            'granola bar': 10,
            'tuna': 15,
            'stale bread': 2,
            'soda': 5,
            'beef jerky': 8,
            "pork n' beans": 12,
            'crackers': 4,
            'expired chocolate': -10
        }
        

    def __repr__(self):
    #   printing human instance will give you the name, strength level and health
        return f"This human named {self.name} has a strength level of {self.strength} and has {self.health} health!"


    # basic human attack = strength * 3
    # checks if human is alive/health above 0
    # basic attack will take away health from zombie health
    # zombie health then uses max func to determine if health is above 0, and if not to auto select it
    def human_attack(self, zombie, defend = False):
        if self.health > 0:
            basic_attack = self.strength * 3
            if defend == True:
                damage = zombie.defend(basic_attack)
                zombie.health -= damage
                zombie.health = max(zombie.health, 0)
                if zombie.health == 0:
                    zombie.isDecapitated = True
                    print(f"This Zombie thought he could block, but that didn't work out. This zombie just had it's head chopped off! ")
                    print(f"{self.name} did {damage} damage. NICE.")
                else:
                    print(f"Zombie is still alive or..undead...still moving...he or she... blocked some of the {basic_attack} attack damage!")
                    print(f"{self.name} did a total of {damage} damage. Zombie has {zombie.health} health left.")
            elif defend == False:
                zombie.health -= basic_attack
                zombie.health = max(zombie.health, 0)
                if zombie.health > 0 or zombie.isDecapitated == False:
                    print(f"This Zombie can't block. {self.name} did {basic_attack} damage..")
                    print(f"Lame Zombie has {zombie.health} health now.")
                else:
                    zombie.isDecapitated == True
                    print(f"{self.name} just sliced the Zombie's head clean off with {basic_attack} damage!")
        else:   
            print(f'Yeah, no. {self.name} is dead or turning into a zombie. Sorry!')

     # defend will be dependent on strength
    def defend(self, damage):
        damage_after_defend = damage - self.strength
        return damage_after_defend
    
    
    # foodlist matches human class dictionary
    # random mod imported to pick a choice from food list
    # added to inventory once found
    def search4_food(self):
        foodList = ['apple', 'granola bar', 'tuna', 'stale bread', 'soda', 'beef jerky', "pork n' beans", 'crackers', 'expired chocolate']
        found_food = r.choice(foodList)
        print(f"{self.name} begins searching around for something to eat and heal up...")
        print("Searching...")
        print("Searching...still")
        print(f"{self.name} found {found_food}. This will be added to their inventory.")
        self.inventory.append(found_food)
        return found_food
        
        
    # checks if item is in inventory and human dictionary
    # adds value of item to human health(or subtracts)
    # removes item from inventory
    def use_item(self, item):
        if item in self.food_values and item in self.inventory:
            item_value = self.food_values[item]
            print(f"{self.name} wants to use the {item} to heal up.")
            self.health += item_value
            self.inventory.remove(item)
            if item_value < 0:
                print(f"{self.name} just consumed something bad! {item} took away {item_value} health!")
                print(f'Their health is now {self.health}. DO NOT eat that again.')
            else:  
                self.health = min(self.health, self.max_health)
                print(f"{self.name} consumed {item} and gained {item_value} health. ")
                print(f"Their health is now {self.health}!")
        else:
            print(f"{self.name} needs to stop playing around. They don't have {item} in their inventory!")
            
  
# functions outside classes but necessary for:
# picking a random character
# generating random strength
# adding a new zombie to a list of zombies and checking if they are dead
# starting a new game with a new generation for character, zombie and strengths and reset zombie list

def random_character():
    random_names = ['Chainsaw Chaz', 'Bite-Sized Betty', 'Splatter Sam', 'Machete Mike', 'Slashy Stacey', 'Bullet Becky', 'Decap Dave', 'No BS Steve']
    return r.choice(random_names)

def generate_random_strength():
    return r.randint(1,20)

def add_new_zombie(zombie_list):
    new_zombie_strength = generate_random_strength()
    new_zombie = Zombie(new_zombie_strength)
    zombie_list.append(new_zombie)
    print_options = [
    "The newly risen corpse staggered onto the scene, its fresh wounds still oozing as it searched for its first victim.",
    "With a fresh, lifeless gaze, the newly turned zombie lurched forward, its movements still stiff from recent reanimation.",
    "A freshly turned zombie emerged from the darkness, its body twitching with the remnants of life it once had.",
    "The newly animated zombie crawled from its shallow grave, its eyes glowing with an unnatural hunger.",
    "A recently infected zombie shuffled into view, its body still showing the signs of its former human self."
    ]

    print(r.choice(print_options))
    
    
def new_game():
    human_name = random_character()
    human_strength = generate_random_strength()
    human = Human(human_name, human_strength)
    
    zombie_list = []
    add_new_zombie(zombie_list)
    
    return human, zombie_list

def main ():
    
    
    print('''
          
$$\     $$\                         $$\    $$\  $$$$$$\        $$$$$$$$\                       $$\       $$\           
\$$\   $$  |                        $$ |   $$ |$$  __$$\       \____$$  |                      $$ |      \__|          
 \$$\ $$  /$$$$$$\  $$\   $$\       $$ |   $$ |$$ /  \__|          $$  /$$$$$$\  $$$$$$\$$$$\  $$$$$$$\  $$\  $$$$$$\  
  \$$$$  /$$  __$$\ $$ |  $$ |      \$$\  $$  |\$$$$$$\           $$  /$$  __$$\ $$  _$$  _$$\ $$  __$$\ $$ |$$  __$$\ 
   \$$  / $$ /  $$ |$$ |  $$ |       \$$\$$  /  \____$$\         $$  / $$ /  $$ |$$ / $$ / $$ |$$ |  $$ |$$ |$$$$$$$$ |
    $$ |  $$ |  $$ |$$ |  $$ |        \$$$  /  $$\   $$ |       $$  /  $$ |  $$ |$$ | $$ | $$ |$$ |  $$ |$$ |$$   ____|
    $$ |  \$$$$$$  |\$$$$$$  |         \$  /   \$$$$$$  |      $$$$$$$$\$$$$$$  |$$ | $$ | $$ |$$$$$$$  |$$ |\$$$$$$$\ 
    \__|   \______/  \______/           \_/     \______/       \________\______/ \__| \__| \__|\_______/ \__| \_______|
                                                                                                                       
                                                                                                                       
                                                                                                                       
''')
    # initialize game with starting zombie and starting human
    human, zombie_list = new_game()
    
    
    
    # introduction with the human, giving out name
    print('You are a human...for now.')
    print()
    name_input = input('(What is your name?) ')
    print()
    print(f"Psh. That is a cute name....{name_input}...nah..")
    print()
    print(f"Instead, we will call you '{human.name}'...sounds better than the unicorn fairy name you just gave us.")
    print()
    answer = input("(Anyway, are you ready?) ")
    print()
    print("Who cares. You have no choice. Don't get bitten.")
    print()
    
    
    # explaining strengths and what human is up against
    print(f"You are about to go up against a Zombie that has strength level of {zombie_list[0].strength}.")
    print()
    print('Strength is everything, it essentially defines your attack damage and your defense abilities.')
    print()
    print(f"Oh, and if you are wondering what your current strength is...it's {human.strength}.")
    print()
    response = input('(Uhh hello, you still there?) ')
    
    print('''
  _____               _     _        ___                           _                   
 |__  /___  _ __ ___ | |__ (_) ___  |_ _|_ __   ___ ___  _ __ ___ (_)_ __   __ _       
   / // _ \| '_ ` _ \| '_ \| |/ _ \  | || '_ \ / __/ _ \| '_ ` _ \| | '_ \ / _` |      
  / /| (_) | | | | | | |_) | |  __/  | || | | | (_| (_) | | | | | | | | | | (_| |_ _ _ 
 /____\___/|_| |_| |_|_.__/|_|\___| |___|_| |_|\___\___/|_| |_| |_|_|_| |_|\__, (_|_|_)
                                                                           |___/     
          ''')
    print(f"Again, who cares. Zombie incoming. GOOD LUCK {human.name}! It may or may not be a fair fight.")

    
    while True:
        # options for user
        print()
        print("What are you gonna do??")
        print("------------------")
        print("0. **GAME FACTS**")
        print("1. Attack Zombie")
        print("2. Defend against Zombie")
        print("3. Search for food")
        print("4. Check Inventory")
        print("5. Use an item")
        print("6. Kill another Zombie")
        print('7. NEW GAME...haha you died.')
        print("8. Run away, because you thought you could do it, but you are TOO scared. You are also a classified as a 'QUITTER'!")
        
        choice = input("Enter your choice: ")
        print()
        print()
        
        
        if choice == '0':
            print("** Game Facts **")
            print("1. Humans and Zombies both have strengths that determine their attack and defense capabilities.")
            print("2. Health is an important attribute; humans can heal by finding and consuming food.")
            print("3. Zombies have different types of attacks, and humans can defend against them.")
            print("4. The game includes random elements, like finding food and random strength generation.")
            print("5. Use your resources wisely to survive and defeat the zombies.")

        
        # human attacks zombie, random possibility zombie uses defend
        elif choice == '1':
            # Select the first non-decapitated zombie
            current_zombie = next((z for z in zombie_list if not z.isDecapitated), None)
            if current_zombie:
                bool_list = [True, False]
                possible_zombie_defense = r.choice(bool_list)
                human.human_attack(current_zombie, defend=possible_zombie_defense)
            else:
                print("All zombies are decapitated. Add a new zombie!")
            
        elif choice == '2':
            current_zombie = next((z for z in zombie_list if not z.isDecapitated), None)
            if current_zombie:
                type_of_zombie_attack_with_defend = [lambda: current_zombie.zombie_attack(human, defend=True), lambda:current_zombie.zombie_bite(human, defend=True)]
                type_of_zombie_attack_no_defend = [lambda: current_zombie.zombie_attack(human), lambda: current_zombie.zombie_bite(human)]
                
                defend_choice = input('You really want to defend? (y/n) ').lower()
                if defend_choice == 'y':
                    r.choice(type_of_zombie_attack_with_defend)()
                else:
                    r.choice(type_of_zombie_attack_no_defend)()
            else:
                print("All zombies are decapitated. Add a new zombie!")
                
        elif choice == '3':
            if human.health > 0:
                human.search4_food()
            else:
                print("UH...you are dead. New game? Yeah.")
            
        elif choice == '4':
            if human.health > 0:
                print('This is what you have in your inventory:')
                if len(human.inventory) == 0:
                    print('-----------------------------------------')
                    print("Nothing here. Go search for some stuff!  |")
                    print('-----------------------------------------')
                else:
                    for item in human.inventory:
                        print('---------------|')
                        print(item)
                    print('---------------|')
            else:
                print("You cannot do that...you are dead or....a zombie.")   
                
        elif choice == '5':
            if human.health > 0:
                print('You need to pick 1 item you want to use from your inventory....')
                inv_choice = input("(What do you want to use?)").lower().strip()
                print()
                human.use_item(inv_choice)
            else:
                print("Start a new game and stop being a CHICKEN!")
            
            
        elif choice == '6':
            add_new_zombie(zombie_list)
            
        elif choice == '7':
            print('** STARTING NEW GAME **')
            human, zombie_list = new_game()
            
            
        elif choice == '8':
            quitting_list = [f"'I-I just can't do this, I am too scared.' Whimpered {human.name}.", f"'I-I thought I could handle it, but I can't', {human.name} cried, backing away. 'I am too terrified.' "]
            print(r.choice(quitting_list))
            break
        
        else:
            print(f"{human.name}, you need to select a number. Get it together.")
    
    
    print("Goodbye, until...next time?")
                
                
            
            
    
    
    
    

if __name__ == "__main__":
    main()