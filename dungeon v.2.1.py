import random
import time
import os

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def print_and_wait(text):
    clear_terminal()
    print(text)
    time.sleep(1)
    input("Stiskněte Enter pro pokračování...")

print_and_wait("Vítejte v Dungeon Quest! Vaším úkolem je najít poklad ukrytý v podzemním labyrintu.")
print_and_wait("Vyberete si svého hrdinu a vydejte se na cestu!")

class Player:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
        self.inventory = []

    def attack(self, enemy):
        damage = random.randint(1, self.strength)
        enemy.health -= damage
        print(f"{self.name} zasadil {enemy.name} úder za {damage} zdraví. {enemy.name} má nyní {enemy.health} zdraví.")

    def get_defeat_prob(self, enemy):
        base_prob = enemy.defeat_prob
        for item in self.inventory:
            if item == "Magický meč":
                return min(base_prob + 0.2, 1.0)
        return base_prob

class Enemy:
    def __init__(self, name, health, strength, defeat_prob):
        self.name = name
        self.health = health
        self.strength = strength
        self.defeat_prob = defeat_prob

    def attack(self, player):
        damage = random.randint(1, self.strength)
        player.health -= damage
        print(f"{self.name} zasadil {player.name} úder za {damage} zdraví. {player.name} má nyní {player.health} zdraví.")

class BossEnemy(Enemy):
    def __init__(self, name, health, strength, defeat_prob, reward):
        super().__init__(name, health, strength, defeat_prob)
        self.reward = reward

warrior = Player("Válečník", 65, 10)
rogue = Player("Zloděj", 60, 15)
mage = Player("Kouzelník", 40, 50)
necromancer = Player("Nekromancer", 100, 100)

goblin = Enemy("Goblin", 20, 5, 0.7)
skeleton = Enemy("Kostra", 30, 8, 0.6)
troll = Enemy("Troll", 40, 10, 0.5)
dragon = BossEnemy("Drak", 75, 15, 0.3, "Magický meč")

def get_random_enemy():
    return random.choice([goblin, skeleton, troll, dragon])

def get_random_item():
    items = ["Sword", "Shield", "Potion", "Scroll"]
    return random.choice(items)

def show_inventory(player):
    if len(player.inventory) == 0:
        print_and_wait("Váš inventář je prázdný.")
    else:
        print_and_wait(f"{player.name}, máte v inventáři následující předměty:")
        for item in player.inventory:
            print_and_wait(item)

while True:
    print_and_wait("Vyberte si svého hrdinu:")
    print("1) Válečník")
    print("2) Zloděj")
    print("3) Kouzelník")
    print("4) Nekromancer")
    choice = input("Vaše volba: ")
    if choice == "1":
        player = warrior
        break
    elif choice == "2":
        player = rogue
        break
    elif choice == "3":
        player = mage
    elif choice == "4":
        player = necromancer    
        break
    else:
        print("Neplatná volba, zadejte prosím 1, 2 nebo 3.")

print_and_wait(f"Vítejte, {player.name}! Vydejte se do podzemí a hledejte poklad!")

while True:
    enemy = get_random_enemy()
    print_and_wait(f"Našel jste {enemy.name}!")
    while player.health > 0 and enemy.health > 0:
        player.attack(enemy)
        if enemy.health <= 0:
            defeat_chance = random.random()
            if defeat_chance <= player.get_defeat_prob(enemy):
                print_and_wait(f"Podařilo se vám porazit {enemy.name}!")
                if isinstance(enemy, BossEnemy):
                    player.inventory.append(enemy.reward)
                    print_and_wait(f"Získali jste {enemy.reward}!")
                    print_and_wait("Gratulujeme! Našli jste poklad. Hra končí.")
                    quit()
                else:
                    if random.random() < 0.5:
                        item = get_random_item()
                        player.inventory.append(item)
                        print_and_wait(f"Získali jste {item}!")
                    break
            else:
                print_and_wait(f"Nepodařilo se vám porazit {enemy.name}! Utíkáte s posledními silami.")
                break
        enemy.attack(player)
        if player.health <= 0:
            print_and_wait("Bohužel jste zemřeli. Hra končí.")
            quit()
    print_and_wait("Hledání pokračuje...")
    if len(player.inventory) > 0 and random.random() < 0.75:
        print_and_wait("Našli jste krabici s pokladem!")
        show_inventory(player)
        print_and_wait("Gratulujeme! Našli jste poklad. Hra končí.")
        quit()
    elif len(player.inventory) > 0 and random.random() < 0.1:
        print_and_wait("Našli jste skrytou místnost!")
        print_and_wait("Zde se nachází lektvar, který vám obnoví veškeré zdraví.")
        player.health = 100
        show_inventory(player)
        player.health = 100
        show_inventory(player)
