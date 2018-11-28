import enchant
from itertools import permutations

language = enchant.Dict("en_US")

def get_permutation(letter_list, length=None):
    permutation = permutations(letter_list, length)
    words = permutation_processor(permutation)
    display_words(words)

def permutation_processor(permutation):
    words = []
    for i in list(permutation):
        joined_word = "".join(i)
        word = check_words(joined_word)
        if word != None:
            words.append(word)

    return words

def check_words(word):
    if (language.check(word)):
        return word

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

def display_words(words):
    if len(words):
        print("Here are the results. Bingo!")
        for word in words:
            print(word)
        
        return
    
    print("Oops! No words found. You just broke the English language 😟")

def main():
    letters = get_letters()
    size = get_size(letters)
    get_permutation(letters, size)

if __name__ == "__main__":
    main()
