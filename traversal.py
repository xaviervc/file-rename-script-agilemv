import os

folders = []
files = []

for entry in os.scandir('/'):
    if entry.is_dir():
        folders.append(entry.path)
    elif entry.is_file():
        files.append(entry.path)

print('Folders:')
print(folders)