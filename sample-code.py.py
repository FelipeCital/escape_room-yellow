# -*- coding: utf-8 -*-
"""all_together.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UKVzmbghXzJIMaThoMSw_E9yYnFjcAsn
"""

# define rooms and items

#doors declaration
door_a = {
    "name": "door_a",
    "type": "door",
}

door_b = {
    "name": "door_b",
    "type": "door",
}

door_c = {
    "name": "door_c",
    "type": "door",
}

#Juliette: added password to the "door_d"
door_d = {
    "name": "door_d",
    "type": "door",
    "password": "77"
}

#Berna added "door_e"
door_e = {
    "name": "door_e",
    "type": "door",
}

#keys declaration:

key_a = {
    "name": "key for door a",
    "type": "key",
    "target": door_a,
}

key_b = {
    "name": "key for door b",
    "type": "key",
    "target": door_b,
}

key_c = {
    "name": "key for door c",
    "type": "key",
    "target": door_c,
}

key_d = {
    "name": "key for door d",
    "type": "key",
    "target": door_d,
}

#Berna added " key_e"
key_e = {
    "name": "key for door e",
    "type": "key",
    "target": door_e,
}

#items declaration:
couch = {
    "name": "couch",
    "type": "furniture",
}

piano = {
    "name": "piano",
    "type": "furniture",
}

queen_bed = {
    "name": "queen_bed",
    "type": "furniture",
}

double_bed = {
    "name": "double_bed",
    "type": "furniture",
}

dresser = {
    "name": "dresser",
    "type": "furniture",
}

dinning_table = {
    "name": "dinning_table",
    "type": "furniture",
}

#Berna added new item "standing_lamp", "suit_case", and "bomb"
standing_lamp = {
    "name": "standing_lamp",
    "type": "furniture",
}

suitcase = {
    "name":"suitcase",
    "type": "furniture",
}

bomb = {
    "name": "bomb",
    "type": "bomb"
}

# FELIPE items declaration: blue potion, red potion, chest, ancient chest.
blue_potion = {
    "name": "blue_potion",
    "type": "potion",
    "description": "A blue potion with a mysterious label.",
}

red_potion = {
    "name": "red_potion",
    "type": "potion",
    "description": "A red potion with a comforting aroma.",
}

chest = {
    "name": "chest",
    "type": "furniture",
    "description": "A chest with two potions inside.",
    "contains": [blue_potion, red_potion],
}

ancient_chest = {
    "name": "ancient_chest",
    "type": "furniture",
}

#rooms declaration:
game_room = {
    "name": "game_room",
    "type": "room",
}

bedroom_1 = {
    "name": "bedroom_1",
    "type": "room",
}
bedroom_2 = {
    "name": "bedroom_2",
    "type": "room",
}

livingroom = {
    "name": "livingroom",
    "type": "room",
}
outside = {
    "name": "outside",
    "type": "room",
}
#Berna added "cliff" as new room
cliff = {
    "name": "cliff",
    "type": "room",
}

all_rooms = [game_room, outside, bedroom_1, bedroom_2, livingroom]

all_doors = [door_a, door_b, door_c, door_d, door_e]

all_keys =[key_a, key_b, key_c, key_d, key_e]
# FELIPE Added chest and ancient_chest to all_items
all_items = [couch, piano, queen_bed, double_bed, dresser, dinning_table,chest , ancient_chest, standing_lamp, suitcase]


# define which items/rooms are related

object_relations = {
    #FELIPE Added chest to game_room:
    "game_room": [couch, chest, piano, door_a],
    #FELIPE Added ancient_chest to bedroom_1:
    "bedroom_1": [ancient_chest, queen_bed, door_b, door_a, door_c],
    "bedroom_2": [double_bed, dresser, suitcase, door_b],
    "livingroom": [dinning_table, standing_lamp, door_c, door_d, door_e],
    "outside": [door_d],
     #Berna added cliff
    "cliff": [door_e],
    "door_a": [game_room, bedroom_1],
    "door_b": [bedroom_1, bedroom_2],
    "door_c": [bedroom_1, livingroom],
    "door_d": [livingroom, outside],
    #Berna added door_e
    "door_e": [livingroom, cliff],
    "key_a": [door_a],
    "key_b": [door_b],
    "key_c": [door_c],
    "key_d": [door_d],
    #Berna added key_e
    "key_e": [door_e],
    "piano": [key_a],
    "queen_bed": [key_b],
    "double_bed": [key_c],
    "dresser": [key_d],
    "couch": [],
    "dinning_table": [],
    # Berna added items standing_lamp and suitcase
    "standing_lamp": [key_e],
    "suitcase": [bomb],
# FELIPE Added chest and anciente chest
    "chest": [game_room],
    "ancient_chest":[blue_potion, red_potion],
}





# define game state. Do not directly change this dict.
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This
# way you can replay the game multiple times.

INIT_GAME_STATE = {
    "current_room": game_room,
    "keys_collected": [],
    "target_room": outside,
    # FELIPE Added inventory (to keep the potions with the user)
    "inventory": [],
}

def linebreak():
    """
    Print a line break
    """
    print("\n\n")

def start_game():
    """
    Start the game
    """
    print("You wake up on a couch and find yourself in a strange house with no windows which you have never been to before. You don't remember why you are here and what had happened before. You feel some unknown danger is approaching and you must get out of the house, NOW!")
    play_room(game_state["current_room"])

# FELIPE Added second life (to reborn on the bedroom_1)
def second_life():
    play_room(game_state["current_room"])

def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either
    explore (list all items in this room) or examine an item found here.
    """
    game_state["current_room"] = room
    if(game_state["current_room"] == game_state["target_room"]):
        printVictory()
        print("Congrats! You escaped the room!")
    #Berna added TRAP condition
    elif(game_state["current_room"] == cliff):
        print("It was a TRAP!! You fell down from cliff. GAME OVER :(")
        print(
            """
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠉⠻⣿
                ⣿⣿⣿⠁⠀⠈⢿⣿⣿⣿⣿⣇⠀⠀⠀⠻⣿⣿⣿⣿⣿⠟⠋⠁⠀⠀⠀⠀⢀⣿⡇
                ⣿⣿⣿⣄⠀⠀⠀⠙⢿⣿⣿⣿⣆⠀⠀⠀⠹⣿⣿⡿⠁⠀⠀⠀⣀⣤⣴⣾⣿⣿⡇
                ⣿⣿⣿⣿⣦⡀⠀⠀⠀⠹⣿⣿⣿⣦⠀⠀⠀⠘⣿⠁⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⡇
                ⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⣿⣿⠟⠋⠀⠀⠀⠀⠈⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⡇
                ⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⡿⠋⠁⠀⠈⠙⢆⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⡿⠛⠁⠀⠹⣿⣿⣿⣿⣿⣿⣿
                ⣿⠁⠀⠀⠀⠀⠀⠈⣧⠀⠀⠀⠀⠈⠙⠻⠟⠁⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⡇
                ⣿⣄⠀⠀⠀⠀⠀⣰⣿⣿⣶⣤⣀⡀⠀⠀⠀⠀⠀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣷⣤⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            """
        )
        #game_state["current_room"] == bedroom_1
        game_state.update(INIT_GAME_STATE)  # Reset the game state to the initial state
        start_game()

    else:
        print("You are now in " + room["name"])
        intended_action = input("What would you like to do? Type 'explore' or 'examine'?").strip()
        if intended_action == "explore":
            explore_room(room)
            play_room(room)
        elif intended_action == "examine":
            examine_item(input("What would you like to examine?").strip())
        else:
            print("Not sure what you mean. Type 'explore' or 'examine'.")
            play_room(room)
        linebreak()

def explore_room(room):
    """
    Explore a room. List all items belonging to this room.
    """
    items = [i["name"] for i in object_relations[room["name"]]]
    print("You explore the room. This is " + room["name"] + ". You find " + ", ".join(items))

def get_next_room_of_door(door, current_room):
    """
    From object_relations, find the two rooms connected to the given door.
    Return the room that is not the current_room.
    """
    connected_rooms = object_relations[door["name"]]
    for room in connected_rooms:
        if(not current_room == room):
            return room

def printBomb():
    print(
    """
              \|/
            `--+--'
              /|\
             ' | '
           ,--'#`--.
           |#######|
        _.-'#######`-._
     ,-'###############`-.
   ,'#####################`,
  /#########################\
 |###########################|
 |###########################|
  \#########################/
   `.#####################,'
     `._###############_,'
        `--..#####..--'
    """
    )

def printKey():
    print("     ooo,    .---. ")
    print("    o`  o   /    |\________________ ")
    print("   o`   'oooo()  | ________   _   _) ")
    print('   `o   o`  \    |/        | | | | ')
    print("""    `ooo'    `---'         "-" |_|  """)


def printPotions():
    print("      _____          _____   ")
    print("     '.___,'        '.___,' ")
    print("      (___)          (___) ")
    print("      <   >          <   > ")
    print("       ) (            ) ( ")
    print("      /`-.\          /`-.\ ")
    print("     /     \        /     \ ")
    print("    / _    _\      / _    _\ ")
    print("   :,' `-.' `:    :,' `-.' `: ")
    print("   |   BLUE  |    |   RED   | ")
    print("   :  POTION ;    :  POTION ; ")
    print("    \       /      \       / ")
    print("     `.___.'        `.___.'   ")


def printSpidergus():
    print("                   /\ ")
    print("                  /  \ ")
    print("                 |  _ \                  _")
    print("                 | / \ \                / \ ")
    print("                 |/   \ \              /   \ ")
    print("                 /     \ |        /\  /     \ ")
    print("                /|      \| ~  ~  /  \/       \ ")
    print("        _______/_|_______\(o)(o)/___/\_____   \ ")
    print("       /      /  |       (______)     \    \   \_ ")
    print("      /      /   |         '  '        \    \ ")
    print("     /      /    |                      \    \ ")
    print("    /      /     |                       \    \ ")
    print("   /     _/      |                        \    \ ")
    print("  /             _|                         \    \_ ")
    print("_/                                          \ ")
    print("                                             \ ")
    print("                                              \_ ")

def printVictory():
    print("                        ,////, ")
    print("                        /// 6|")
    print("                        //  _|")
    print("                       _/_,-'")
    print("                 _.-/'/   \   ,/;,")
    print("               ,-' /'  \_   \ / _/")
    print("               `\ /     _/\  ` /")
    print("                 |     /,  `\_/")
    print("                 |     \'")
    print("   /\_        /`      /\ ")
    print("  /' /_``--.__/\  `,. /  \ ")
    print(" |_/`  `-._     `\/  `\   `.")
    print("           `-.__/'     `\   |")
    print("                         `\  \ ")
    print("                          `\ \ ")
    print("                             \_\__")
    print("                              \___)")

def examine_item(item_name):
    """
    Examine an item which can be a door or furniture.
    First make sure the intended item belongs to the current room.
    Then check if the item is a door. Tell player if key hasn't been
    collected yet. Otherwise ask player if they want to go to the next
    room. If the item is not a door, then check if it contains keys.
    Collect the key if found and update the game state. At the end,
    play either the current or the next room depending on the game state
    to keep playing.
    """
    current_room = game_state["current_room"]
    next_room = ""
    output = None

    for item in object_relations[current_room["name"]]:
        if(item["name"] == item_name):
            output = "You examine " + item_name + ". "
# FELIPE Added a condition for 'chest' incase the user examine it:
            if item["name"] == "chest":
                # Handle the first chest interaction (the one with both potions)
                print("You find a chest with two potions inside: a blue potion and a red potion.")
                choice = input("Do you want to take the potions with you? Type 'yes' or 'no': ").strip()
                if choice == 'yes':
                    game_state["inventory"].extend([blue_potion, red_potion])
                    printPotions()
                    print("After reading the labels, you take the potions with you.")
                    print(" --- Inventory updated: +1 Blue Potion --- ")
                    print(" --- Inventory updated: +1 Red Potion  --- ")
                else:
                    print("You decide not to take the potions with you.")
            elif item["name"] == "ancient_chest":
                # Handle the ancient chest interaction (the one with the creature)
                print("You examine this mysterious chest. Would you like to open this old ancient chest?")
                choice = input("Type 'yes' or 'no': ").strip()
                if choice == 'yes':
                    print(" --- COMBAT --- ")
                    printSpidergus()
                    print("OUCH! You've received a bite from the famous 'Spidergus', a magical creature with a venom that can steal your memories! You start feeling dizzy.")
                    print("-90 HP")
                    if blue_potion not in game_state["inventory"] and red_potion not in game_state["inventory"]:
                        print("Your eyes are feeling heavy, and you decide to sleep until you feel better while your memories are fading away.")
                        print("Maybe there's a magical potion to heal the venom somewhere.")
                        print("...A few moments later...")
                        print("You wake up with a scary feeling of opening that chest again.")
                    else:
                        print("You are in pain and see the potions on your inventory, but the labels fell off and you can't remember which one is for which due to the venom!")
                        potion_choice = input("Which potion do you want to use? Type 'blue potion' or 'red potion': ").strip()
                        if potion_choice == 'blue potion':
                            print(" --- Blue potion used --- ")
                            print("You tried to drink the blue potion, but the side effects are getting worse, you can't even remember your own name!")
                            print("Your eyes are feeling heavy, and you decide to sleep until you feel better while your memories are fading away.")
                            print("...A few moments later...")
                            print("You woke with stamina enough to keep trying your escape.")
                            print("+100 HP")
                            second_life()  # Restart the game on the bedroom_1
                        elif potion_choice == 'red potion':
                            print(" --- Red potion used --- ")
                            print("After drinking the red potion, you start feeling better, scarying the creature away. You find a scroll inside the chest with the number '77' on it.")
                            print("+100 HP")
                        else:
                            print("Invalid potion choice.")
                else:
                    print("You decide not to open the chest, losing the possible treasures inside of it.")
# FELIPE Condition for trap (chest) overs here, below its the normal code for door and normal items.

            elif(item["type"] == "door"):
              have_key = False

              for key in game_state["keys_collected"]:
                    if(key["target"] == item):
                        have_key = True

              if have_key:
                if "password" in item:
                  entered_password = input ("You have the key but the door remains locked... You notice a lock asking for an integer between 00 and 99. What is your answer? ").strip()
                  if entered_password == item["password"]:
                      output += "You entered the correct password!"
                      next_room = get_next_room_of_door(item,current_room)
                  else:
                      output += "Incorrect password.."
                else:
                  output += "You unlock it with the key that you have."
                  next_room = get_next_room_of_door(item,current_room)
              else:
                output += "You are missing the key!"

            elif(item["name"] in object_relations and len(object_relations[item["name"]])>0):
                    item_found = object_relations[item["name"]].pop()
                    # Berna: added type condition for key
                    if item_found["type"] == "key":
                        game_state["keys_collected"].append(item_found)
                        printKey()
                        output += "You find " + item_found["name"] + "."
                    # Berna: added item type bomb condition
                    elif item_found["type"] == "bomb":
                            print(output)
                            printBomb()
                            print("You have triggered the BOMB!")
                            print("It's needed to be disarmed, there is three cables:")
                            print("Yellow, Red, Green")
                            cable = input("Which cable do you want to cut? (Type 'Yellow' or 'Red' or 'Green')")
                            if(cable == "Yellow"):
                                object_relations["suitcase"] = []
                                output = "You did it! Bomb is disarmed, you can continue."
                            else:
                                print("Bomb have exploded!")
                                print(" --- GAME OVER --- ")
                                game_state.update(INIT_GAME_STATE)  # Reset the game state to the initial state
                                start_game()
                                return
                # Berna: moved this message for empty furnitures

                #Rocio: tips for the user:
            elif(item["name"]=="couch"):
                output +="I recommend you to try to find another item in the room."
            # elif(item["name"]=="dinning_table"):
                # output +="I think you have forgotten to examine at least one object in another room."

            else:
                output += "There isn't anything interesting about it."
            print(output)
            break

    if(output is None):
        print("The item you requested is not found in the current room.")

    if next_room:
      if "password" in next_room:
        entered_password = input ("This door is locked. Please enter the password to proceed: ").strip()
        if entered_password == next_room["password"]:
            print("You entered the correct password! The door opens.")
        else:
            print("Incorrect password. The door remains locked.")

      else:
        if input("Do you want to go to the next room? Enter 'yes' or 'no'").strip() == 'yes':
          play_room(next_room)
    else:
        play_room(current_room)



game_state = INIT_GAME_STATE.copy()

start_game()

