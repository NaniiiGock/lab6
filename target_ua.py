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
print(get_words("base.lst", ['ф', 'у', 'щ', 'б', 'л']))
