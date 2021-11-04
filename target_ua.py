
"""
my project for target game
"""
from typing import List
import random
def generate_grid() -> List[List[str]]:
    """
    generates a grid randomly from 5 letters
    """
    letters_1 = []
    letters = ['а','б','в','г','ґ','д','е',\
    'є','ж','з','и','і','ї','й','к','л','м',\
    'н','о','п','р','с','т','у','ф','х','ц','ч','щ','ь','ю','я']
    while len(letters_1) < 5:
        let = random.choice(letters)
        if let not in letters_1:
            letters_1.append(let)
    return letters_1

def get_words(file1: str, letters) -> List[str]:
    """
    gets words from dictionary from letters
    >>> get_words("base.lst", "щ")
    []
    """
    with open(file1, "r", encoding="utf-8") as file:
        list_of_words = []
        for line in file:
            line = line.strip()
            ind = line.find(" ")
            word=line[:ind]
            letter = line[ind:]
            letter = letter.lstrip()
            if len(word) > 5 or len(word) < 1:
                continue
            for i in letters:
                if i == word[0]:
                    break
            else:
                continue
            if "noninfl" in letter or "intj" in letter:
                continue
            if letter.startswith("adv") or letter.startswith("/adv"):
                list_of_words.append((word, "adverb"))
                continue
            if letter.startswith("adj") or letter.startswith("/adj"):
                list_of_words.append((word, "adjective"))
                continue
            if "/n" in letter or "noun" in letter:
                list_of_words.append((word, "noun"))
                continue
            if "/v" in letter:
                list_of_words.append((word, "verb"))
                continue
    return list_of_words
            
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
def get_user_words():
    """
    Reads the words entered by user
    """
    return input().lower().split()

def language_part_gen():
    """
    Generates a random part of language
    """
    language = ['verb', 'noun', 'adjective', 'adverb']
    return random.choice(language)
