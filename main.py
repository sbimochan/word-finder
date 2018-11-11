import enchant
from itertools import permutations

language = enchant.Dict("en_US")

def possible_permutations(letter_list, beautiful_size):
    perm = permutations(letter_list)
    for i in list(perm):
        joined_word = "".join(i)
        required_substraction = len(joined_word) - beautiful_size
        if required_substraction > 0:
            required_word = joined_word[:-required_substraction]

            check_words(required_word)
        else:
            check_words(joined_word)

def check_words(word):
    if (language.check(word)):
        print(word)

def ask_input():
    beautiful_letters = input("Gimme the letters separated by space please. Press return when finished. \n")
    trimmed_beautiful_letters = beautiful_letters.strip()
    splitted_letters = trimmed_beautiful_letters.split(" ")
    for i in list(splitted_letters):
        if len(i) > 1:
            raise TypeError("Please enter single word separated by a space. Please try again 😇")

    beautiful_size = input("What length of word do you need? (Optional) \n")
    if beautiful_size:
        try:
            beautiful_size = int(beautiful_size)
        except ValueError:
            print("Not a valid number")
    else:
        beautiful_size = len(splitted_letters)

    print("Here are the results. Bingo!")
    possible_permutations(splitted_letters, beautiful_size)


def main():
    ask_input()

if __name__ == "__main__":
    main()
