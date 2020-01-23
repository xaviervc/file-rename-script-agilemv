import os
 
rootDir = '.'

for dirName, subdirList, fileList in os.walk(rootDir):

    print(f'Found directory: {dirName}')

    check_for_chars(dirName)

    for fname in fileList:
        print(f'\t{fname}')


def replace_chars(fileName):
    for i in fileName:
        if i == '\"':
            fileName = fileName.replace('\"', ' in')
        elif i == '*':
            fileName = fileName.replace('*', ' ')
        elif i == ':':
            fileName = fileName.replace(':', ' ')
        elif i == '<':
            fileName = fileName.replace('<', ' ')
        elif i == '>':
            fileName = fileName.replace('>', ' ')
        elif i == '?':
            fileName = fileName.replace('?', ' ')
        elif i == '/':
            fileName = fileName.replace('/', ' ')
        elif i == '\\':
            fileName = fileName.replace('\\', ' ')
        elif i == '|':
            fileName = fileName.replace('|', ' ')
    return fileName

def check_for_chars(fullpath):
    if '\"' in fullpath or '*' in fullpath or ':' in fullpath or '<' in fullpath or '>' in fullpath or '?' in fullpath or '/' in fullpath or '\\' in fullpath or '|' in fullpath:
        return replace_chars(fullpath)