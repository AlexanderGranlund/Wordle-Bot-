import random

def get_words():
    with open('words.txt', 'r') as file:
        all_words = file.readlines()
        all_stripped_words = []
        for i in all_words:
            stripped = i.rstrip()
            all_stripped_words.append(stripped)
        return all_stripped_words

def word_list_converter():
    word_list = get_words()
    for k in range(len(word_list)):
        word_list[k] = word_list[k].lower()
    return word_list

def game_start_parameters(length_of_words):
    game_word_list = []
    word_list = word_list_converter()
    for i in word_list:
        if len(i) == length_of_words:
            game_word_list.append(i)
    guess_count = 0
    picked_word = random.choice(game_word_list)
    parameters_dict = {"length_of_words":length_of_words, "guess_count":guess_count,"game_word_list":game_word_list, "picked_word":picked_word}
    return parameters_dict

def bot_parameters(parameters_dict):
    bot_word_list = parameters_dict["game_word_list"].copy()
    return bot_word_list

def guess_validater(guess, parameters_dict):
    if len(guess) == parameters_dict["length_of_words"]:
        if guess in parameters_dict["game_word_list"]:
            parameters_dict["guess_count"] += 1
            return True
        else:
            return False
    else:
        return False


def guess_match_checker(parameters_dict, guess):
    guess_results = []
    for i in range(len(guess)):
        if guess[i] == parameters_dict["picked_word"][i]:
            guess_results.append(2)
        if guess[i] != parameters_dict["picked_word"][i] and guess[i] in parameters_dict["picked_word"]:
            guess_results.append(1)  
        if guess[i] not in parameters_dict["picked_word"]:
            guess_results.append(0) 
    if (1 not in guess_results) and 0 not in guess_results:
        return True  
    else:
        return guess_results

