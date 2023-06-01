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
            if item == "KnihaMinecraftu":
                return min(base_prob + 0.4, 1.0)
            if item == "UcebniceCestiny":
                return min(base_prob + 0.1, 1.0)           
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

warrior = Player("Válečník", 90, 145)
rogue = Player("Zloděj", 60, 60)
mage = Player("Kouzelník", 90, 50)
necromancer = Player("Nekromancer", 100, 100)
Hajek = Player("HajekUltimateKorbaForm", 180, 16)
PetaKozak = Player("Nejmocnejsi hrdina pythnu", 1000, 10000)
Bubileg = Player("AjtakBubileg", 75, 120)
Paladin = Player("Rytíř HTML", 80, 100)
China = Player("Činský náčelník", 80, 150 )

goblin = Enemy("Goblin", 20, 5, 0.7)
Prezident = Enemy("Prezident Světa", 50, 2, 0.7)
Majitel = Enemy("Majitel peněz", 20, 30, 0.7)
Wyvern = Enemy("Wyzern", 75, 5, 0.6)
Expredseda = Enemy("Pan Patočka", 80, 5, 0.7)
skibidi = Enemy("Matěj haruda", 500, 2, 0.7)
Ai = Enemy("CHATGPT", 1, 1, 0.7)
mistopredseda = Enemy("Bican", 100, 10, 0.7)
Php = Enemy("Avarage PHP developer", 5, 5, 0.7)
meliodas = Enemy("Meliodas fullcounter", 20, 100, 0.7)
Pavel = Enemy("Skoro bez hlavý Pája J.", 50, 5, 0.7)
zombie = Enemy("Zombík", 15, 15, 0.7)
goku= Enemy("Goku", 200, 70, 0.7)
Ender = Enemy("Enderman", 45, 5, 0.7)
Blaf = Enemy("Pan Polák blafuje?", 45, 5, 0.7)
adambim = Enemy("AdamBím", 35, 8, 0.7)
BigCh = Enemy("Big chongus Jiřík", 45, 10, 0.7)
PanPohl = Enemy("PanPohl", 85, 3, 0.7)
skeleton = Enemy("Kostra", 30, 8, 0.6)
troll = Enemy("Troll", 40, 10, 0.5)
Dan = Enemy("Kolega Šfarný", 50, 8, 0.7)
dragon = BossEnemy("Drak", 75, 15, 0.3, "Magický meč")
Zappfire = BossEnemy("Vojtahotař", 75, 15, 0.3, "KnihaMinecraftu")
teacher = BossEnemy("Učitelka češtiny", 50, 9, 0.3,"UcebniceCestiny")
nemesis = Enemy("Pan Škoda", 120, 20, 0.1)

def get_random_enemy(difficulty):
    if difficulty == EASY:
        return random.choice([goblin, skeleton,adambim,zombie,Pavel,Blaf,BigCh,Ender,Php,Ai,Prezident,Majitel])
    elif difficulty == MEDIUM:
        return random.choice([goblin, skeleton, troll,adambim,PanPohl,zombie,Pavel,Blaf,BigCh,Dan,Expredseda,Wyvern])
    elif difficulty == HARD:
        return random.choice([dragon,Zappfire,PanPohl,teacher,Pavel,goku,meliodas,mistopredseda,skibidi])
    elif difficulty == NIGHTMARE:
        return nemesis

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

EASY = 1
MEDIUM = 2
HARD = 3
NIGHTMARE = 4

def choose_difficulty():
    while True:
        print_and_wait("Vyberte obtížnost:")
        print("1) Snadná")
        print("2) Střední")
        print("3) Těžká")
        print("4) Noční můra")
        choice = input("Vaše volba: ")
        if choice == "1":
            return EASY
        elif choice == "2":
            return MEDIUM
        elif choice == "3":
            return HARD
        elif choice == "4":
            return NIGHTMARE
        else:
            print("Neplatná volba, zadejte prosím 1, 2, 3 nebo 4.")

difficulty = choose_difficulty()

while True:
    print_and_wait("Vyberte si svého hrdinu:")
    print("1) Válečník")
    print("2) Zloděj")
    print("3) Kouzelník")
    print("4) Nekromancer")
    print("5) Hajek")
    print("6) PetaKozak")
    print("7) Bubileg")
    print("8) Rytíř HTML")
    print("9) Činský náčelník")
    choice = input("Vaše volba: ")
    if choice == "1":
        player = warrior
        break
    elif choice == "2":
        player = rogue
        break
    elif choice == "3":
        player = mage
        break
    elif choice == "4":
        player = necromancer
        break
    elif choice == "5":
        player = Hajek
        break
    elif choice == "6":
        player = PetaKozak
        break
    elif choice == "7":
        player = Bubileg
        break
    elif choice == "8":
        player = Paladin
        break
    elif choice == "9":
        player = China
        break       
    else:
        print("Neplatná volba, zadejte prosím 1, 2, 3, 4, 5, 6, 7, 8 nebo 9.")

print_and_wait(f"Vítejte, {player.name}! Vydejte se do podzemí a hledejte poklad!")

while True:
    enemy = get_random_enemy(difficulty)
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