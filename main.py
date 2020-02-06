#!/usr/bin/env python3
import sys, os, json
# Check to make sure we are running the correct version of Python
assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

# The game and item description files (in the same folder as this script)
game_file = 'game.json'


# Load the contents of the files into the game and items dictionaries. You can largely ignore this
# Sorry it's messy, I'm trying to account for any potential craziness with the file location
def load_files():
    try:
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(os.path.join(__location__, game_file)) as json_file: game = json.load(json_file)
        return (game)
    except:
        print("There was a problem reading either the game or item file.")
        os._exit(1)


def render(game,current):
    c = game[current]
    if c["kind"] == "ROOM":
        print("You are in a " + c["name"])
        print(c["desc"])
    else:
        print("You are at a " + c["name"])
        print(c["desc"])

def get_input():
    d = input("What would you like to do?")
    d = d.upper().strip()
    return d

def update(game,current,choice):
    c = game[current]
    for i in c["exits"]:
        if choice == i["exit"]:
            return i["target"]
    return current
# The main function for the game
def main():
    current = 'WROOM'  # The starting location
    end_game = ['END']  # Any of the end-game locations

    (game) = load_files()

    while True:
        render(game,current)
        choice = get_input()
        if choice == "QUIT":
            break
        current = update(game,current,choice)
    print("Thank you for playing!")
# run the main function
if __name__ == '__main__':
	main()