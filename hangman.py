import os
import random

#OUTPUT LAYER
#wipes console from previous prints
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

#ASCII graphic definition
def draw_graphic(i):
    if i == 0:
        print("\n\n\n\n\n\n")
    elif i == 7:
        print("\n\n\n\n\n ___")
    elif i == 6:
        print("\n\n\n\n|")
        print("|___")
    elif i == 5:
        print("\n\n|")
        print("|")
        print("|")
        print("|___")
    elif i == 4:
        print(" ______")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|___")
    elif i == 3:
        print(" ______")
        print("|      |")
        print("|")
        print("|")
        print("|")
        print("|___")
    elif i == 2:
        print(" ______")
        print("|      |")
        print("|      O")
        print("|")
        print("|")
        print("|___")
    elif i == 1:
        print(" ______")
        print("|      |")
        print("|      O")
        print("|     /|\\")
        print("|")
        print("|___")
    else:
        print(" ______")
        print("|      |")
        print("|      O")
        print("|     /|\\")
        print("|     / \\")
        print("|___")

#updates ASCII graphic based on selected difficulty and remaining lives
def update_life_graphic(max_lives, current_lives):
    dificulty_graphic_matrix = [[1, 3, 5], [1, 3, 5, 7], [1, 3, 5, 6, 7], [1, 2, 3, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]]

    if max_lives == current_lives:
        draw_graphic(0)
    elif current_lives == -1:
        draw_graphic(8)
    else:
        draw_graphic(dificulty_graphic_matrix[max_lives-3][current_lives])

#updates display of secret password
def update_password_display(word, guessed_letters_list):
    password_char_list = list(word)
    password = ""
    for char in password_char_list:
        if char.lower() in guessed_letters_list:
            password += char + " "
        else:
            password += "_ "
    print(password)

#refreshes whole game display interface
def update_game_display(word, guessed_letters_list, max_lives, current_lives, wrong_guesses_list, case):
    clearConsole() #zmienic na clear_console
    update_password_display(word, guessed_letters_list)
    update_life_graphic(max_lives, current_lives)
    if case == 0:
        print("You have found correct letter in the puzzle word!!!")
    elif case == 1:
        print("You already found that this letter is not in the puzzle word!")
    elif case == 2:
        print("You already have that letter in the puzzle word!")
    elif case == 3:
        print("This letter is not in the puzzle word :(")
    if len(wrong_guesses_list) != 0:
        wrong_letters_display(wrong_guesses_list)

#displays letters which were found by user not to be existing in password
def wrong_letters_display(wrong_guesses_list):
    letters = ""
    #print(f"Wrong checks: {', '.join(wrong_guesses_list)}")
    for letter in wrong_guesses_list:
        letters += "'"+letter + "' "
    print(f"Wrong checks: "+ letters)

def you_win_display():
    print("\nYOU WON!!!\n")


def game_over_display():
    print("\nYOU LOST :(\n")

def leave_game():
    print("Goodbye!")
    exit()

#INPUT LAYER
def ask_user_for_game_input():
    while True:
        user_input = input("Try to guess letter in secret password: ")
        if user_given_valid_game_input(user_input):
            return user_input.lower()
        else:
            continue

#checks if input from user is single letter
def user_given_valid_game_input(inp):
    if inp.isalpha() and len(inp)==1:
        return True
    elif inp.lower() == "quit":
        leave_game()
    else:
        print("You have to type single letter!")
        return False

#asks user for if he wants to play again
def try_again_prompt():
    while True:
        user_input = input("Try again? (y/n): ")
        if user_input.lower() in ["y","n","quit"]:
            return user_input
        else:
            continue

#asks user to select difficulty level
def ask_user_dificulty_input():
    while True:
        difficulty = input("Select dificulty (1-5): ")
        if difficulty.isdigit() and int(difficulty)-1 in range(5):
            return difficulty
        elif difficulty.lower() == "quit":
            leave_game()
        else:
            continue


#LOGIC LAYER
def play(word, lives):
    current_lives = lives
    lowercase_list = list(word.lower())
    guessed_letters_list = []
    wrong_guesses_list = []
    display_case = -1

    #initial gamestate display
    print(lowercase_list)
    update_game_display(word, guessed_letters_list, lives, current_lives, wrong_guesses_list, display_case)
    
    #main game loop
    while len(lowercase_list) != 0 and current_lives >= 0:
        user_input_character = ask_user_for_game_input()

        if user_input_character in lowercase_list:
            guessed_letters_list.append(user_input_character)
            display_case = 0

            while user_input_character in lowercase_list:
                lowercase_list.remove(user_input_character)
        elif user_input_character.upper() in wrong_guesses_list:
            display_case = 1
        elif user_input_character in guessed_letters_list:
            display_case = 2
        else:
            wrong_guesses_list.append(user_input_character.upper())
            current_lives -= 1
            display_case = 3

        update_game_display(word, guessed_letters_list, lives, current_lives, wrong_guesses_list, display_case)

    #win or loose condition check
    if current_lives >= 0:
        you_win_display()
    else:
        game_over_display()
    try_again()

#option to play again
def try_again():
    try_again_answer = try_again_prompt()
    if try_again_answer == "y":
        initialize_game()
    else:
        leave_game()

#selects random word from file
def select_random_word(dificulty):
    file = open("countries-and-capitals.txt", "r")
    word_list = file.read().split("\n")
    file.close()
    while True:
        random_index = random.randint(0, (len(word_list)-1))
        random_word = word_list[random_index]
        if len(random_word) == dificulty+3:
            return random_word
        else:
            continue

#asks user for dificulty 
def initialize_game():
    difficulty = ask_user_dificulty_input()
    lives = 8 - int(difficulty)
    random_word = select_random_word(int(difficulty))
    play(random_word, lives)

def main():
    initialize_game()

main()