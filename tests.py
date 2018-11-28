import pytest
from itertools import permutations
from main import permutation_processor


def test_default_size_words():
    letters = 'ahsem'
    size = None

    permutation = permutations(letters, size)
    words = permutation_processor(permutation)
    assert 'shame' in words


def test_custom_size_words():
    letters = 'ahsem'
    size = 4
    expected_output = [
        'ahem', 'hams', 'hems', 'same', 'sham', 'seam', 'mash', 'meas', 'mesa',
        'mesh'
    ]
    permutation = permutations(letters, size)
    words = permutation_processor(permutation)
    assert expected_output == words
