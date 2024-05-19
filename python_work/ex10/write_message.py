file_path = 'programming.txt'

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

with open(file_path, 'w') as file:
    file.write(contents)