import enchant
from itertools import permutations

language = enchant.Dict("en_US")

def get_permutation(letter_list, length=None):
    permutation = permutations(letter_list, length)
    print("Here are the results. Bingo!")
    permutation_processor(permutation)

def permutation_processor(permutation):
    for i in list(permutation):
        joined_word = "".join(i)
        check_words(joined_word)

def check_words(word):
    if (language.check(word)):
        print(word)

def get_letters():
    beautiful_letters = input("Gimme those letters without space. Press return when finished. \n")
    trimmed_beautiful_letters = beautiful_letters.strip()
    splitted_letters = list(trimmed_beautiful_letters)

    return splitted_letters

def get_size(splitted_letters):
    beautiful_size = input("What length of word do you need? (Optional) \n")
    if beautiful_size:
        try:
            beautiful_size = int(beautiful_size)
        except ValueError:
            print("Not a valid number 😟")
    else:
        beautiful_size = len(splitted_letters)

    return beautiful_size

def main():
    letters = get_letters()
    size = get_size(letters)
    get_permutation(letters, size)

if __name__ == "__main__":
    main()
