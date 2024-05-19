# 14/5/2024

filename = 'romeo_juliet.txt'

def count_common_word(filename, word):
    try:
        with open(filename, encoding='utf-8') as file:
            contents = file.read()
    except FileNotFoundError:
        pass
    else:
        word_count = contents.lower().count(word)
        msg = f"'{word}' appears in {filename} about {word_count} times."
        print(msg)


count_common_word(filename, 'the ')
