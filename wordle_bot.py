from wordle_game import game_start_parameters, guess_match_checker, guess_validater, word_list_converter
import random
import time

def first_stage(parameters_dict):
    potential_choices_backup = []
    already_used = "abcdefghijklmnopqrstyvwxyzåäö"
    potential_choices = word_frequency(parameters_dict["game_word_list"], already_used)
    for n in parameters_dict["game_word_list"]:
        if is_unique(n) == True:
            potential_choices_backup.append(n)
    for n in potential_choices_backup: 
        if contains_vocals(n) == False:
            potential_choices_backup.remove(n)
    if potential_choices != []:
        bot_guess = random.choice(potential_choices) 
    elif potential_choices_backup != []:    
        bot_guess = random.choice(potential_choices_backup)    
    else:
         bot_guess = random.choice(parameters_dict["game_word_list"])
    return bot_guess



def smart_bot_guess(parameters_dict, guess):
    if not "bot_word_list" in parameters_dict:
        parameters_dict["bot_word_list"] = set(parameters_dict["game_word_list"])
    bot_word_list = parameters_dict["bot_word_list"]
    already_used = "abcdefghijklmnopqrstyvwxyzåäö"
    guess_results = guess_match_checker(parameters_dict, guess)
    removed_words = [] 
    potiential_choices_unique_characters = ""
    potential_choices_backup = []
    for i in range(len(guess_results)): 
        if guess_results[i] == 0:
            for k in bot_word_list: 
                if guess[i] in k:    
                    removed_words.append(k)        
        if guess_results[i] == 1:
            for k in bot_word_list:
                if guess[i] not in k:
                    removed_words.append(k) 
                if guess[i] == k[i]:
                    removed_words.append(k)
        if guess_results[i] == 2:
            for k in bot_word_list: 
                if guess[i] != k[i]:
                    removed_words.append(k) 
    for n in removed_words:  
        if n in bot_word_list:
            bot_word_list.remove(n)
    potential_choices = word_frequency(bot_word_list, already_used)
    if len(potential_choices) > 3:
        word_value_dict = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0, "k":0, "l":0, "m":0, "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0, "å":0, "ä":0, "ö":0}
        for n in potential_choices:
            for i in n:
                word_value_dict[i] = word_value_dict[i] + 1
        for k in word_value_dict:
            if word_value_dict[k] == 1:
                potiential_choices_unique_characters += k
        potential_choices = word_frequency(parameters_dict["game_word_list"], potiential_choices_unique_characters)
    for n in bot_word_list: 
        if is_unique(n) == True:
            potential_choices_backup.append(n)
    for n in potential_choices_backup: 
        if contains_vocals(n) == False:
            potential_choices_backup.remove(n)
    if potential_choices != []:   
        bot_guess = random.choice(potential_choices)
    elif potential_choices_backup != []:
        bot_guess = random.choice(potential_choices_backup)
    else:
         bot_guess = random.choice(list(bot_word_list))
    return bot_guess

def is_unique(word):
    for i in range(len(word)): 
        for j in range(i + 1,len(word)): 
            if(word[i] == word[j]):
                return False
    return True

def contains_vocals(word):
    vocals = ["A","a","E","e","I","i","O","o","U","u","Y","y","Å","å","Ä","ä","Ö","ö"]
    contained_vocals = []
    count = 0 
    for k in word:
        if k in contained_vocals:
            count -= 1
        if k in vocals:
            count += 1
            contained_vocals.append(k)
    if len(word) < 6:
        if count > 1:
            return True
    if len(word) > 5:
        if count > 2:
            return True
    return False

def word_frequency(word_list, already_used):
    potential_choices = []
    highscore = 0
    word_value_dict = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0, "k":0, "l":0, "m":0, "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0, "å":0, "ä":0, "ö":0}
    game_word_list_dict = {}
    for n in word_list:
        for q in n:
            if q in already_used:
                word_value_dict[q] = word_value_dict[q] + 1
    #print(word_value_dict)
    for k in word_list:
        game_word_list_dict[k] = 0
        used_characters = ""
        for q in k:
            if q not in used_characters:
                game_word_list_dict[k] = game_word_list_dict[k] + word_value_dict[q]
                used_characters += q
        if game_word_list_dict[k] == highscore:
            potential_choices.append(k)
        elif game_word_list_dict[k] > highscore:
            highscore = game_word_list_dict[k]
            potential_choices = [k]
    return potential_choices

