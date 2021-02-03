from sys import exit
from os import system
from os import system, name as os_name
import random
import sys
import time
import os
import subprocess
import csv

# importing choices from csv file
choice_data = csv.DictReader(open("choices.csv", mode = "r"), delimiter = "$")
choice_data_dict = {}
for row in choice_data:
    key = row['Chapter']
    val = row['Choices']
    if key not in choice_data_dict:
        choice_data_dict[key] = []
    choice_data_dict[key].append(val)

# importing chapters (text) from csv file
paragraph_data = csv.DictReader(open("chapters.csv", mode = "r"), delimiter = "$")
paragraph_data_dict = {}
for row in paragraph_data:
    key = row['Chapter']
    val = row['Contents']
    if key not in paragraph_data_dict:
        paragraph_data_dict[key] = []
    paragraph_data_dict[key].append(val)

# resizing terminal window
subprocess.call(["echo","-e","\x1b[8;42;67t"])

#############figure out how to exit max window

#############figure out how to print in color

# defining variables
chapter = 0
paragraph = ""

# defining functions
def clear():
    #if os_name == 'nt':
        _ = system('clear')
    #else:
    #    _ = system('cls')

# defining figlet
def figletD():
    _ = system('figlet -f bloody.flf " Dracula"')

def figletC():
    global chapter
    chapter += 1
    _ = system(f'figlet -f straight.flf " Chapter {chapter}"')

# defining typewriter function to print paragraphs
def typewriter(paragraph):
        char = 0
        sys.stdout.flush()
        for char in paragraph:  
            if char == ".":
                print(f"{char}", end="")
                sys.stdout.flush()
                time.sleep(0.05)
                # real value when finalizing game 0.25
            elif char != ".":
                print(f"{char}", end="")
                sys.stdout.flush()
                time.sleep(random.uniform(0.01, 0.01))
                # real values when finalizing game 0.03, 0.065
            sys.stdout.flush()

# defining typewriter function to print choices
def choices(paragraph):
        char = 0
        sys.stdout.flush()
        for char in paragraph:  
            if char == "?" or char == "'":
                print("\n")
                sys.stdout.flush()
                time.sleep(0.05)
                # real value when finalizing game 0.25
            elif char != ".":
                print(f"{char}", end="")
                sys.stdout.flush()
                time.sleep(random.uniform(0.01, 0.01))
                # real values when finalizing game 0.03, 0.065
            sys.stdout.flush()



def callTypewriter():
        typewriter(str(paragraph_data_dict[paragraph]).strip('[""]').center(70))

def callChoices():
        choices(str(choice_data_dict["c1p1"]).strip('[""]'))


def bad_response(why):
    print(why, ", try again.")
    main_entrance()

# c1p1 prompt
def main():

    print("\n\n")
    callChoices()
    choice = input('\n\n> ')
    boolean_choice = choice.isnumeric()
    if boolean_choice == False:
        bad_response("That's not a valid response")
        main_entrance()
    elif boolean_choice == True:
        how_much = int(choice)
        if how_much == 1:
            print("Before you can knock, the door eerily creaks open.")
            return
        if how_much == 2:
            print("You find nothing of interest.")
            return
        if how_much == 3:
            print("Before you can knock, the door eerily creaks open.")
            return
        elif how_much < 0 or how_much > 3:
            bad_response("That's not a valid response")
            main()

class mmap():
    #scenes = {
    #    'mainEntrance': mainEntrance()
    #}
    pass

class engine():
    pass

class scene(object):
    def __init__(self, intialize, choice1, choice2, choice3, choice4,  badResponse):
        self.initialize = initialize
        self.choice1 = choice1
        self.choice2 = choice2
        self.choice3 = choice3
        self.choice4 = choice4
    pass

class character():
    def charAttributes(HP, item, equipment):
        pass

class items():
    def item():
        pass

    def equipment():
        pass

if __name__ == "__main__":
    clear()
    paragraph = "intro"; callTypewriter()
    time.sleep(1.2)
    print("\n")
    figletD()
    time.sleep(2)
    figletC()
    paragraph = "c1p1"; callTypewriter()
    time.sleep(1)
    main()
