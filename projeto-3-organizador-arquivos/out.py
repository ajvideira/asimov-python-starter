import os

files = os.listdir()

for file in files:
    if not os.path.isdir(file):
        continue

    extension_dir = os.getcwd() + os.sep + file

    for subfile in os.listdir(file):
        from_path = extension_dir + os.sep + subfile
        to_path = os.getcwd() + os.sep + subfile
        os.rename(from_path, to_path)

    os.rmdir(extension_dir)


