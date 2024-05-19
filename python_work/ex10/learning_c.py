filename = 'learning_python.txt'

with open(filename) as f:
    lines = f.readlines()

for line in lines:
    line = line.rstrip()
    # replace word 'Python' woth 'C'.
    print(line.replace('Python', 'C'))
