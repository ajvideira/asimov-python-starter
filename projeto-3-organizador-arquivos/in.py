import os

ignore_extensions = ['py']

files = os.listdir()

for file in files:
    if os.path.isdir(file):
        continue

    extension = file.split('.')[-1]

    if extension in ignore_extensions:
        continue

    if not os.path.exists(extension):
        os.mkdir(extension)

    old_filepath = os.getcwd() + os.sep + file
    new_filepath = os.getcwd() + os.sep + extension + os.sep + file
    os.rename(old_filepath, new_filepath)


