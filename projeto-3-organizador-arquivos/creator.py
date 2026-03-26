extensions = ['txt', 'md', 'png', 'jpg', 'mp4', 'sql', 'mov', 'doc']


for extension in extensions:
    for i in range(10):
        with open(f'arquivo-{i}.{extension}', 'w') as file:
            file.write('teste')
            file.close()