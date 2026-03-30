import os

ignore_extensions = ['py']

for file in os.listdir():
    if os.path.isdir(file):
        continue

    extension = file.split('.')[-1]

    if extension in ignore_extensions:
        continue

    if not os.path.exists(extension):
        os.mkdir(extension)

    from_path = os.path.join(os.getcwd(), file)
    to_path = os.path.join(os.getcwd(), extension, file)
    os.rename(from_path, to_path)


