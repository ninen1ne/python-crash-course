# 14/5/2024

filenames = ['cat.txt', 'dog.txt']


def read_contents(filenames):
    """Read contents of .txt file."""
    for filename in filenames:
        try:
            with open(filename) as file:
                contents = file.read()
        except FileNotFoundError:
            # filenames.remove(path)
            pass
        else:
            print(f'Reading file: {filename}')
            print(contents)


read_contents(filenames)








