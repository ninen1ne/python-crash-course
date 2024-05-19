# 14/5/2024
def read_contents(path):
    """Read contents of .txt file."""
    try:
        with open(path) as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f'This "{path}" does not exist in this current working directory.')


filenames = ['cat.txt', 'dog.txt']

# For loop list of filenames to call func read_contents.
for filename in filenames:
    read_contents(filename)


