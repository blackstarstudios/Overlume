# Main Libraries
import os, random, math

# Major game states
run = True
menu = True
play = False
rules = False
save = False
load = False
pause = False
options = False
credits = False

# Minor game states
key = False
fight = False 
#battle = False
standing = True
buy = False
#shop = False
speak = False
boss = False
inventory = False

class Player:
    
    def __init__(self, name, HPMAX, ATK):
        self.name = name
        self.HPMAX = HPMAX
        self.HP = self.HPMAX
        #self.MPMAX = 50
        #self.MP = self.MPMAXs
        #self.SPMAX = 100
        #self.SP = self.SPMAX
        #self.XPMAX = 100
        #self.XP = self.XPMAX
        self.ATK = ATK
        self.pot = 0
        self.elix = 0
        self.lums = 0
        self.x = 0
        self.y = 0
        
    def characterCreation(self):
        tname = input("What is your name? > ")
        return Player(tname, 100, 5)

    def heal(self, amount):
        if self.HP + amount < self.HPMAX:
            self.HP += amount
        else:
            self.HP = self.HP
        print(self.name + "'s HP refilled to " + str(self.HP) + "!")

    def healthBars(self):
        
        # display
        bars = 20
        remaining_health_symbol, remaining_mana_symbol, remaining_stam_symbol, remaining_exp_symbol = "█"
        lost_health_symbol, lost_mana_symbol, lost_stam_symbol, lost_exp_symbol = "_"
        
        # colors
        color_green = "\033[92m"
        color_darkgreen = "\033[32m"
        color_yellow = "\33[33m"
        color_red = "\033[91m"
        color_darkred = "\033[31m"
        color_purple = "\033[95m"
        color_darkpurple = "\033[35m"
        color_blue = "\33[34m"
        color_brightblue = "\033[94m"
        color_default = "\033[0m"
        health_color = color_red
        mana_color = color_brightblue
        stam_color = color_green
        exp_color = color_darkpurple
        
        while True:
            # bar update
            remaining_health_bars = round(self.HP / self.HPMAX * bars)
            lost_health_bars = bars - remaining_health_bars
            remaining_mana_bars = round(self.MP / self.MPMAX * bars)
            lost_mana_bars = bars - remaining_mana_bars
            remaining_stam_bars = round(self.SP / self.SPMAX * bars)
            lost_stam_bars = bars - remaining_stam_bars
            remaining_exp_bars = round(self.XP * self.XPMAX * bars)
            lost_exp_bars = bars - remaining_exp_bars
            
        
            # printing stats
            print(f"HEALTH: {self.HP} / {self.HPMAX}")
            print(f"|{health_color}{remaining_health_bars * remaining_health_symbol}"
                  f"{lost_health_bars * lost_health_symbol}{color_default}|")
            print(f"MANA: {self.MP} / {self.MPMAX}")
            print(f"|{mana_color}{remaining_mana_bars * remaining_mana_symbol}"
                  f"{lost_mana_bars * lost_mana_symbol}{color_default}|")
            print(f"STAMINA: {self.SP} / {self.SPMAX}")
            print(f"|{stam_color}{remaining_stam_bars * remaining_stam_symbol}"
                  f"{lost_stam_bars * lost_stam_symbol}{color_default}|")
            print(f"XP: {self.XP} / {self.XPMAX}")
            print(f"|{exp_color}{remaining_exp_bars * remaining_exp_symbol}"
                  f"{lost_exp_bars * lost_exp_symbol}{color_default}|")
        
            # health color update
            if self.HP < 0.5 * self.HPMAX:
                #health_color = color_red
            # else:
                health_color = color_darkred

            if self.MP < 0.5 * self.MPMAX:
                mana_color = color_blue

            if self.SP < 0.5 * self.SPMAX:
                stam_color = color_darkgreen

            if self.XP > 0.5 * self.XPMAX:
                exp_color = color_purple

            '''

            # stat update
            self.HP -= 1
            self.MP -= 1
            self.SP -= 1
            self.XP -= 1
        
            self.HP = max(self.HP, 0)
            self.MP = max(self.MP, 0)
            self.SP = max(self.SP, 0)
            self.XP = max(self.XP, 0)
            '''
        
            # input
            input()

e_list = ["Goblin", "Orc", "Slime"]

mobs = {
    "Goblin": {
        "hp": 15,
        "at": 3,
        "go": 8
    },
    "Orc": {
        "hp": 35,
        "at": 5,
        "go": 18
    },
    "Slime": {
        "hp": 30,
        "at": 2,
        "go": 12
    },
    "Dragon": {
        "hp": 100,
        "at": 8,
        "go": 100
    }
}

#stats
max_health = 100
current_health = 100
max_mana = 50
current_mana = 50

# display
bars = 20
remaining_health_symbol = "█"
lost_health_symbol = "_"

# colors
color_green = "\033[92m"
color_yellow = "\33[33m"
color_red = "\033[91m"
color_blue = "\33[34m"
color_default = "\033[0m"
health_color = color_green

while True:
    # bar update
    remaining_health_bars = round(current_health / max_health * bars)
    lost_health_bars = bars - remaining_health_bars
    remaining_mana_bars = round(current_mana / max_mana * bars)
    lost_mana_bars = bars - remaining_mana_bars

    # printing stats
    print(f"HEALTH: {current_health} / {max_health}")
    print(f"|{health_color}{remaining_health_bars * remaining_health_symbol}"
          f"{lost_health_bars * lost_health_symbol}{color_default}|")
    print(f"MANA: {current_mana} / {max_mana}")
    print(f"|{color_blue}{remaining_mana_bars * remaining_health_symbol}"
          f"{lost_mana_bars * lost_health_symbol}{color_default}|")

    # stat update
    current_health -= 1
    current_mana -= 1

    current_health = max(current_health, 0)
    current_mana = max(current_mana, 0)

    # health color update
    if current_health > 0.66 * max_health:
        health_color = color_green
    elif current_health > 0.33 * max_health:
        health_color = color_yellow
    else:
        health_color = color_red

    # input
    input()

        #  x = 0       x = 1       x = 2       x = 3       x = 4       x = 5         x = 6
map = [["plains",   "plains",   "plains",   "plains",   "forest", "mountain",       "cave"],    # y = 0
       ["forest",   "forest",   "forest",   "forest",   "forest",    "hills",   "mountain"],    # y = 1
       ["forest",   "fields",   "bridge",   "plains",    "hills",   "forest",      "hills"],    # y = 2
       ["plains",     "shop",     "town",    "mayor",   "plains",    "hills",   "mountain"],    # y = 3
       ["plains",   "fields",   "fields",   "plains",    "hills", "mountain",   "mountain"]]    # y = 4

y_len = len(map)-1
x_len = len(map[0])-1

biom = {
    "plains": {
        "t": "PLAINS",
        "e": True},
    "forest": {
        "t": "WOODS",
        "e": True},
    "fields": {
        "t": "FIELDS",
        "e": False},
    "bridge": {
        "t": "BRIGE",
        "e": True},
    "town": {
        "t": "TOWN CENTRE",
        "e": False},
    "shop": {
        "t": "SHOP",
        "e": False},
    "mayor": {
        "t": "MAYOR",
        "e": False},
    "cave": {
        "t": "CAVE",
        "e": False},
    "mountain": {
        "t": "MOUNTAIN",
        "e": True},
    "hills": {
        "t": "HILLS",
        "e": True,
    }
}

# Line Space
def space():
    print("")

def bordl():
    space()
    print("Xx=========================xX")
    space()

def seprl():
    print("x==================x")

def undrl():
    print("--------------------")
    space()
    
symbol = "█"

color_red = "\033[91m"
color_purple = "\33[95m"
color_blue1 = "\33[34m"
color_blue2 = "\33[36m"
color_blue3 = "\33[96m"
color_green1 = "\033[92m"
color_green2 = "\033[32m"
color_brown = "\33[33m"
color_yellow = "\33[93m"
color_grey = "\33[37m"
color_default = "\033[0m"
color_list = (color_red, color_purple, color_blue1, color_blue2, color_blue3,
              color_green1, color_green2, color_yellow, color_brown, color_grey, color_default)


def print_variable_name(variable: object) -> None:
    for name, value in globals().items():
        if id(value) == id(variable):
            return name


def show_colors() -> None:
    for color in color_list:
        print(f"{color}{3 * symbol}", end="")

    print(color_default)

    for color in color_list:
        print(f"{color}{3 * symbol} {print_variable_name(color)}")

    input("")

# Terminal clearing
def cls():
    os.system("cls")
#def cls():
    #os.system('cls||clear')

# Game continuation
def cont():
    return input("> ")

# Movement function
def move():
    pass

# Save function
def save():
    list = [
        player.name,
        str(player.HP),
        str(player.HPMAX),
        str(player.MP),
        str(player.MPMAX),
        str(player.SP),
        str(player.SPMAX),
        str(player.ATK),
        str(player.pot),
        str(player.elix),
        str(player.lums),
        str(player.x),
        str(player.y),
        str(player.key)
    ]

    file = open("load.txt", "w")

    for item in list:
        file.write(item + "\n")
    file.close()

# Load function
def load():
    pass

# Battle function
def battle():
    global fight, play, run, player

    if not boss:
        enemy = random.choice(e_list)
    else:
        enemy = "Dragon"

    hp = mobs[enemy]["hp"]
    hpmax = hp
    atk = mobs[enemy]["at"]
    g = mobs[enemy]["go"]

    while fight:
        cls()
        bordl()
        print("Defeat the " + enemy + "!")
        seprl()
        print(enemy + "'s HP: " + str(hp) + "/" + str(hpmax))
        print(player.name + "'s HP: " + str(player.HP) + "/" + str(player.HPMAX))
        print("POTIONS: " + str(player.pot))
        print("ELIXIR: " + str(player.elix))
        seprl()
        print("1 - ATTACK")
        if player.pot > 0:
            print("2 - USE POTION (30HP)")
        if player.elix > 0:
            print("3 - USE ELIXIR (50HP)")
        bordl()

        choice = input("# ")

        if choice == "1":
            hp -= player.ATK
            print(player.name + " dealt " + str(player.ATK) + " damage to the " + enemy + ".")
            if hp > 0:
                player.HP -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + player.name + ".")
            input("> ")

        elif choice == "2":
            if player.pot > 0:
                player.pot -= 1
                player.heal(30)
                player.HP -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + player.name + ".")
            else:
                print("No potions!")
            input("> ")

        elif choice == "3":
            if player.elix > 0:
                player.elix -= 1
                player.heal(50)
                player.HP -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + player.name + ".")
            else:
                print("No elixirs!")
            input("> ")

        if player.HP <= 0:
            print(enemy + " defeated " + player.name + "...")
            seprl()
            fight = False
            play = False
            run = False
            print("GAME OVER")
            input("> ")

        if hp <= 0:
            print(player.name + " defeated the " + enemy + "!")
            seprl()
            fight = False
            player.lums += g
            print("You've found " + str(g) + " gold!")
            if random.randint(0, 100) < 30:
                player.pot += 1
                print("You've found a potion!")
            if enemy == "Dragon":
                seprl()
                print("Congratulations, you've finished the game!")
                boss = False
                play = False
                run = False
            input("> ")
            cls()

# Shop function
def shop():
    global buy, player

    while buy:
        cls()
        bordl()
        print("Welcome to the shop!")
        seprl()
        print("GOLD: " + str(player.lums))
        print("POTIONS: " + str(player.pot))
        print("ELIXIRS: " + str(player.elix))
        print("ATK: " + str(player.ATK))
        seprl()
        print("1 - BUY POTION (30HP) - 5 GOLD")
        print("2 - BUY ELIXIR (MAXHP) - 8 GOLD")
        print("3 - UPGRADE WEAPON (+2ATK) - 10 GOLD")
        print("4 - LEAVE")
        bordl()

        choice = input("# ")

        if choice == "1":
            if player.lums >= 5:
                player.pot += 1
                player.lums -= 5
                print("You've bought a potion!")
            else:
                print("Not enough gold!")
            input("> ")
        elif choice == "2":
            if player.lums >= 8:
                player.elix += 1
                player.lums -= 8
                print("You've bought an elixir!")
            else:
                print("Not enough gold!")
            input("> ")
        elif choice == "3":
            if player.lums >= 10:
                player.ATK += 2
                player.lums -= 10
                print("You've upgraded your weapon!")
            else:
                print("Not enough gold!")
            input("> ")
        elif choice == "4":
            buy = False

# Inventory function
def inventory():
    pass

# NPC Interaction function
def mayor():
    global speak, key, player

    while speak:
        cls()
        bordl()
        print("Hello there, " + player.name + "!")
        if player.ATK < 10:
            print("You're not strong enough to face the dragon yet! Keep practicing and come back later!")
            key = False
        else:
            print("You might want to take on the dragon now! Take this key but be careful with the beast!")
            key = True

        seprl()
        print("1 - LEAVE")
        bordl()

        choice = input("# ")

        if choice == "1":
            speak = False

# Dungeon Function
def cave():
    global boss, key, fight

    while boss:
        cls()
        bordl()
        print("Here lies the cave of the dragon. What will you do?")
        seprl()
        if key:
            print("1 - USE KEY")
        print("2 - TURN BACK")
        bordl()

        choice = input("# ")

        if choice == "1":
            if key:
                fight = True
                battle()
        elif choice == "2":
            boss = False

# Choice function
def choice():
    return int(input("> "))

# Choice confirmation
def confirm(opt, rtrn):
    c = input("Are you sure? (y/n) > ")
    if c == "y":
        opt
    elif c =="n":
        rtrn
    else: confirm(opt, rtrn)

# Rules screen
def rules():
    cls()
    bordl()
    print("   RULES")
    space()
    print("1. Have fun!")
    bordl()
    cont()

# Credits screen
def credits():
    cls()
    bordl()
    print("CREDITS")
    space()
    print("By BLACKSTAR.")
    bordl()
    cont()

# Options screen
def options():
    cls()
    bordl()
    print("OPTIONS")
    space()
    print("1. SETTINGS")
    print("2. DISPLAY")
    bordl()
    cont()

# Start menu screen
def start():
    global play, menu, load

    cls()
    bordl()
    print(" WELCOME TO LUMORE!")
    space()
    print("    1. NEW GAME")
    print("    2. LOAD GAME")
    print("    3. RULES")
    print("    4. CREDITS")
    print("    0. QUIT GAME")
    bordl()
    opt = choice()

    if opt == 1:
        print()
        cont()

    elif opt == 2:
        load()
    
    elif opt == 3:
        rules()
    
    elif opt == 4:
        credits()
    
    elif opt == 0:
        exit()

# Pause menu screen
def pause():
    print("PAUSE MENU")
    print(" ")
    print("1. UNPAUSE")
    print("2. LOAD")
    print("3. OPTIONS")
    print("0. QUIT")

    if choice() == 1:
        game()
    elif choice() == 2:
        load()
    elif choice() == 3:
        options()
    elif choice() == 0:
        exit()

# Menus function

def menu():
    if pause != True:
        start()
    else:
        pause()

# Main game loop function
def game():
    print(" *GAME START* ")

# Main game loop function
def main():
    while run:
        while menu:
            print("1, NEW GAME")
            print("2, LOAD GAME")
            print("3, RULES")
            print("4, QUIT GAME")

            if rules:
                print("I'm the creator of this game and these are the rules.")
                rules = False
                choice = ""
                input("> ")
            else:
                choice = input("# ")

            if choice == "1":
                cls()
                player = Player.characterCreation()
                menu = False
                play = True
            elif choice == "2":
                try:
                    f = open("load.txt", "r")
                    load_list = f.readlines()
                    if len(load_list) == 9:
                        player.name = load_list[0][:-1]
                        player.HP = int(load_list[1][:-1])
                        player.ATK = int(load_list[2][:-1])
                        player.pot = int(load_list[3][:-1])
                        player.elix = int(load_list[4][:-1])
                        player.gold = int(load_list[5][:-1])
                        player.x = int(load_list[6][:-1])
                        player.y = int(load_list[7][:-1])
                        player.key = bool(load_list[8][:-1])
                        cls()
                        print("Welcome back, " + player.name + "!")
                        input("> ")
                        menu = False
                        play = True
                    else:
                        print("Corrupt save file!")
                        input("> ")
                except OSError:
                    print("No loadable save file!")
                    input("> ")
            elif choice == "3":
                rules = True
            elif choice == "4":
                quit()

        while play:
            save()  # autosave
            cls()

            if not standing:
                if biom[map[player.y][player.x]]["e"]:
                    if random.randint(0, 100) < 30:
                        fight = True
                        battle()

            if play:
                bordl()
                print("LOCATION: " + biom[map[player.y][player.x]]["t"])
                seprl()
                print("NAME: " + player.name)
                player.healthBars()
                print("ATK: " + str(player.ATK))
                print("POTIONS: " + str(player.pot))
                print("ELIXIRS: " + str(player.elix))
                print("GOLD: " + str(player.lums))
                print("COORD:", player.x, player.y)
                seprl()
                print("0 - SAVE AND QUIT")
                if player.y > 0:
                    print("1 - NORTH")
                if player.x < x_len:
                    print("2 - EAST")
                if player.y < y_len:
                    print("3 - SOUTH")
                if player.x > 0:
                    print("4 - WEST")
                if player.pot > 0:
                    print("5 - USE POTION (30HP)")
                if player.elix > 0:
                    print("6 - USE ELIXIR (50HP)")
                if map[player.y][player.x] == "shop" or map[player.y][player.x] == "mayor" or map[player.y][player.x] == "cave":
                    print("7 - ENTER")
                bordl()

                dest = input("# ")

                if dest == "0":
                    play = False
                    menu = True
                    save()
                elif dest == "1":
                    if player.y > 0:
                        player.y -= 1
                        standing = False
                elif dest == "2":
                    if player.x < x_len:
                        player.x += 1
                        standing = False
                elif dest == "3":
                    if player.y < y_len:
                        player.y += 1
                        standing = False
                elif dest == "4":
                    if player.x > 0:
                        player.x -= 1
                        standing = False
                elif dest == "5":
                    if pot > 0:
                        pot -= 1
                        player.heal(30)
                    else:
                        print("No potions!")
                    input("> ")
                    standing = True
                elif dest == "6":
                    if player.elix > 0:
                        player.elix -= 1
                        player.heal(50)
                    else:
                        print("No elixirs!")
                    input("> ")
                    standing = True
                elif dest == "7":
                    if map[player.y][player.x] == "shop":
                        buy = True
                        shop()
                    if map[player.y][player.x] == "mayor":
                        speak = True
                        mayor()
                    if map[player.y][player.x] == "cave":
                        boss = True
                        cave()
                else:
                    standing = True

# Game initialization
main()