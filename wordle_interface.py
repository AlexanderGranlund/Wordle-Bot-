from wordle_game import game_start_parameters, guess_match_checker, guess_validater, word_list_converter, bot_parameters
from wordle_bot import first_stage, smart_bot_guess

def menu():
    print("\n\n\n\nWelcome to Wordle\n")
    menu_choice = False
    while menu_choice == False:
        select = input("Please select one of the the following:\n\nStart new game : Press 1 + Enter\n\nHelp           : Press 2 + Enter\n\n")
        if select.strip() == "1":
            menu_choice = True
            game_start()
        if select.strip() == "2":
            menu_choice = True
            help()
        else:
            print("Please select one of the two choices!")
            go_back = input("Press Enter to continue:") 
            if go_back == go_back:
                menu() 

def help():
    print("Wordle is a word based game where you get six gusses to find the searched five letter word.\nWhen a new game is started you begin by making your first guess,\nthen you will be told if the letters in your guessed word is apart of the searched word and if they are placed correctly relative the searched word.\n")
    go_back = input("Please press Enter to continue:") 
    if go_back == "":
        menu() 
    else:
        menu()

def game_start():
    length_of_words = length_of_word()
    parameters_dict = game_start_parameters(length_of_words)
    while parameters_dict["guess_count"] < 6:
        if parameters_dict["guess_count"] == 0:
            guess = first_stage(parameters_dict)
            print(guess)
        else:
            bot_word_list = bot_parameters(parameters_dict)
            guess = smart_bot_guess(parameters_dict, bot_word_list, guess)
            print(guess)
        #guess = input("\n\nGive your best guess:\n\n").lower()
        if guess_validater(guess, parameters_dict) == True:
            if guess_match_checker(parameters_dict, guess) == True:
                print("You guessed correctly\n\nYou Win!\n\n\n\n")
                go_back = input("Please press Enter to continue:") 
                if go_back == go_back:
                    menu()
            else: 
                print(guess_match_checker(parameters_dict, guess))
        else:
            print("The Word you guessed isn't in our word list or an uncorrect length")
            print("Try again and guess a " + str(parameters_dict["length_of_words"]) + " letter word\n\n")
            go_back = input("Press Enter to continue:")
    print("\n\n\n\nGame Over!\n\nYou ran out of guesses!\n\nThe correct word was " + str(parameters_dict["picked_word"]))
    go_back = input("Please press Enter to continue:") 
    if go_back == "":
        menu() 
    else:
        menu()    

def length_of_word():
    received_int = False
    while received_int == False:
        try:
            length_of_words = int(input("What length of words do you want to play with?\n\n"))
            received_int = True
        except:
            pass
    return length_of_words 

menu()