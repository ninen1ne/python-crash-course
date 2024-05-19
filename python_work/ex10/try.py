from pathlib import Path


path = Path('alice.txt')

try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f'Sorry, the file {path} does not exist.')
else:
    # Count the approximate number of words in a file.
    words = contents.split()
    num_word = len(words)
    print(f'the file {path} has about {num_word} words.')
    