import enchant
from itertools import permutations
from flask_cors import CORS
from flask import Flask,jsonify,request

app = Flask(__name__)
CORS(app)
language = enchant.Dict("en_US")

@app.errorhandler(Exception)
def handle_error(error):
    message = [str(x) for x in error.args]
    response = {
        'error': {
            'msg': message
        }
    }

    return jsonify(response)

@app.route('/', methods=['GET', 'POST'])
def get_inputs():
    if request.method == 'GET':
        return "Hi! Thank you for hitting me. Please try hitting using POST method with args letters and size."

    data = request.get_json()

    letters = data.get("letters")
    if not letters:
        raise Exception("Letters not provided")
    letters = letters.strip()
    size = data.get("size")

    if len(letters) > 20:
        raise Exception("Too long letters. Pheww...")
    if not size:
        size = len(letters)
    else:
        size = int(size)
    return get_permutation(letters, size)


def get_permutation(letter_list, length=None):
    permutation = permutations(letter_list, length)
    words = permutation_processor(permutation)
    counter = 0
    word_set = set()
    for word in words:
        if word:
            counter += 1
            word_set.add(word)

    if counter != 0:
        return jsonify({
            "msg": "Here are the results. Bingo!",
            "result": list(word_set)
        })
    else:
        return jsonify({
            "msg": "Oops! No words found. You just broke the English language 😟",
            "result":[]
        })
def permutation_processor(permutation):
    for i in permutation:
        joined_word = "".join(i)
        word = check_words(joined_word)
        yield word

def check_words(word):
    if language.check(word):
        return word

# Uncomment if necessary
if __name__ == "__main__":
    app.run()
