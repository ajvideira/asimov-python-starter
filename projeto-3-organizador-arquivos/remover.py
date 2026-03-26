import os

for file in os.listdir():
    extension = file.split('.')[-1]

    if not extension == 'py':
        os.remove(os.getcwd() + os.sep + file)