from wordle_game import game_start_parameters, guess_match_checker, guess_validater, word_list_converter
import random

def first_stage(parameters_dict):
    potential_choices = []
    for n in parameters_dict["game_word_list"]:
        if is_unique(n) == True:
            potential_choices.append(n)
    if potential_choices == []:        
        bot_guess = random.choice(parameters_dict["game_word_list"])
    else:
        bot_guess = random.choice(potential_choices)
    return bot_guess

removed_words = [] 

def smart_bot_guess(parameters_dict, bot_word_list, guess):
    if parameters_dict["guess_count"] == 1:
        removed_words.clear()
    guess_results = guess_match_checker(parameters_dict, guess)
    potential_choices = []
    for n in removed_words:
        if n in bot_word_list: 
            bot_word_list.remove(n)
    print(len(bot_word_list))
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
                if guess[i] not in k[i]:
                    removed_words.append(k) 
    for n in removed_words:
        if n in bot_word_list: 
            bot_word_list.remove(n)
    print(len(bot_word_list)) 
    for n in bot_word_list:
        if is_unique(n) == True:
            potential_choices.append(n)
    if potential_choices == []:        
        bot_guess = random.choice(bot_word_list)
    else:
        bot_guess = random.choice(potential_choices)
    return bot_guess

def is_unique(word):
    for i in range(len(word)):
        for j in range(i + 1,len(word)):
            if(word[i] == word[j]):
                return False
    return True