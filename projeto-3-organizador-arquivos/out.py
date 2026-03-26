import os

files = os.listdir()

for file in files:
    if not os.path.isdir(file):
        continue

    extension_dir = os.getcwd() + os.sep + file

    for subfile in os.listdir(file):
        old_filepath = extension_dir + os.sep + subfile
        new_filepath = os.getcwd() + os.sep + subfile
        os.rename(old_filepath, new_filepath)

    os.rmdir(extension_dir)


