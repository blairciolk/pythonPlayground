import time

def first_selection():
    print("You have chosen the Dungeon adventure")
    print("Please enter your chosen name for this adventure")
    player_name = input()
    waking_sequence(player_name)
    
def waking_sequence(player_name):
    print('You wake up in a small room.\n')
    time.sleep(2)
    print(f"{player_name}! You\'re up! I was too afraid to wake you but we need help!")
    time.sleep(2)
    print("We're out of coins to pay for the house rent, we need to find coins or we'll be kicked out!") 
    time.sleep(2)
    print(f"Please, {player_name}! You need to hurry! He hasn't given us long!")