import enchant
from itertools import permutations
from flask_cors import CORS
from flask import Flask,jsonify,request

app = Flask(__name__)
CORS(app)
language = enchant.Dict("en_US")

@app.route('/', methods=['GET', 'POST'])
def get_inputs():
    if request.method == 'GET':
        return "Hi! Thank you for hitting me. Please try hitting using POST method with args letters and size."

    letters = request.json['letters'].strip()
    size = request.json['size']
    return get_permutation(letters, int(size))


def get_permutation(letter_list, beautiful_size):
    permutation = permutations(letter_list)
    required_substraction = len(letter_list) - beautiful_size
    return permutation_processor(permutation, required_substraction)

def permutation_processor(permutation, required_substraction):
    word_list = []
    for i in list(permutation):
        joined_word = "".join(i)
        if required_substraction > 0:
            required_word = joined_word[:-required_substraction]
            check_words(required_word, word_list)
        else:
            check_words(joined_word, word_list)
    response = {
        "msg": "Here are the results. Bingo!",
        "result": word_list
    }
    return jsonify(response)

def check_words(word, word_list):
    if (language.check(word)):
        word_list.append(word)

if __name__ == "__main__":
    app.run()
