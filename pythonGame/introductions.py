import dungeon

def intro_text():
    options = ["1. Dungeon"]
    print("Welcome to a python text adventure game")
    print("Please choose your adventure:")
    for option in options:
        print(option)
    user_selection = input()
    if user_selection == "1":
        dungeon.first_selection()
        