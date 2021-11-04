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


def get_words(f: str, letters: List[str]) -> List[str]:
    list1 = []
    letters += "f"
    with open(f, "r", encoding = 'utf-8') as file:
        for line in file:
            line = line.strip()
            line.split("/")
            list1.append((line[0], line[1]))
        for i in range(30):
            print(list1[i])
# print(get_words("base.lst", ["a")