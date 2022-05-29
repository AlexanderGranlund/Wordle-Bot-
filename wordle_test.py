letters = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0, "k":0, "l":0, "m":0, "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0, "å":0, "ä":0, "ö":0}
words = ["detta", "är", "en", "test", "av", "algoritm","lagoritm"]
point_per_word = {}

for k in words:
    for n in k:
        letters[n] = letters[n] + 1

highscore = 0
topwords = []
for k in words:
    point_per_word[k] = 0
    used_characters = ""
    for n in k:
        if n not in used_characters:
            point_per_word[k] = point_per_word[k] + letters[n]
            used_characters += n
    if point_per_word[k] == highscore:
        topwords.append(k)
    elif point_per_word[k] > highscore:
        highscore = point_per_word[k]
        topwords = [k]; 
print(topwords)

