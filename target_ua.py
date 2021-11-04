"""
my project for target game
"""
from typing import List
import random
def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    letters_1 = []
    letters = ['а','б','в','г','ґ','д','е',\
    'є','ж','з','и','і','ї','й','к','л','м',\
    'н','о','п','р','с','т','у','ф','х','ц','ч','щ','ь','ю','я']
    while True:
        let = random.choice(letters)
        if let not in letters_1:
            letters_1.append(let)
        if len(letters_1) == 5:
            return letters_1
print(generate_grid())


def get_words(file1: str, letters) -> List[str]:
    """
    gets words from dictionary from letters
    >>> get_words("base.lst", "щ")
    []
    """
    if len(letters) != 5:
        return []
    with open(file1, "r", encoding="utf-8") as file:
        list1 = []
        for line in file:
            line = line.strip()
            line =line.strip().split(" ")
            if len(list(line)[0]) <6 or line[0][0] not in letters:
                try:
                    if (("n" and "i") in line[1]) or (("n" and "j") in line[1]):
                        continue
                    if ("/adj" in line) or ("adj" in line):
                        list1.append((line[0], "adjective"))
                    line[1] = list(line[1])
                    if "n" in line[1]:
                        list1.append((line[0], "noun"))
                    if "v" in line[1]:
                        list1.append((line[0],"verb"))
                    if ("a" and "d" and "v") in line[1]:
                        list1.append((line[0], "adverb"))
                except IndexError:
                    continue
    return list1
def check_user_words(user_words, language_part, letters, dict_of_words) -> List[str]:
    """
    gets list of user words and checks if it is among dictionary words
    with appropriate part of language

    >>> check_user_words(["ага", 'абат'], "noun", ["і","с","л","п","а"] , (('абаз', 'noun'),\
('абайя', 'noun'), ('абак', 'noun'), ('абат', 'noun'), ('абая', 'noun')))
    (['абат'], ['абаз', 'абайя', 'абак', 'абая'])
    """
    letters =len(letters)
    dict1 = []
    user_right =[]
    user_loose = []
    for i,_ in enumerate(dict_of_words):
        dict1.append(dict_of_words[i][0])
    for i, _ in enumerate(user_words):
        word = user_words[i]
        if word in dict1:
            if (word, language_part) in dict_of_words:
                user_right.append(word)
    for i, _ in enumerate(dict1):
        if dict1[i] not in user_right:
            user_loose.append(dict1[i])
    return user_right, user_loose
print(get_words("base.lst", ['ф', 'у', 'щ', 'б', 'л']))
print(check_user_words(['бабин', 'битий', 'бичий', 'білий', 'бісів', 'богів', 'божий', 'босий', 'булий', 'булів', 'бурий', 'ласий', 'лисий', 'литий', 'лихий', 'лівий', 'любий', 'лютий', 'усний', 'утлий', 'щирий', 'щучий', 'щучин'], "adjective", ['ф', 'у', 'щ', 'б', 'л'], get_words("base.lst", ['ф', 'у', 'щ', 'б', 'л'])))
