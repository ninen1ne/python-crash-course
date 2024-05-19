# 13/5/2024
from pathlib import Path


def count_words(path):
    """read contents in path file and count the approximate number of words."""

    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # When errors occurs in your program you can tell except part to do nothing by using "pass".
        # pass - tell python to do nothing.
        print(f'Sorry, the file {path} does not exist.')
    else:
        # Count the approximate number of words in a file.
        words = contents.split()
        num_word = len(words)
        print(f'the file {path} has about {num_word} words.')

filenames = ['alice.txt', 'romeo_juliet.txt', 'yolle_adventure.txt', 'learning_python.txt']

for filename in filenames:
    path = Path(filename)
    count_words(path)
