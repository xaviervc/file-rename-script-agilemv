import os

def check_chars(dirName):
    if '\"' in dirName or '*' in dirName or ':' in dirName or '<' in dirName or '>' in dirName or '?' in dirName or '/' in dirName or '\\' in dirName or '|' in dirName:
        return True
    else:
        return False

def replace_chars(fullpath):
    
    for i in fullpath:
        if i == '\"':
            fullpath = fullpath.replace('\"', ' in')
        elif i == '*':
            fullpath = fullpath.replace('*', ' ')
        elif i == ':':
            fullpath = fullpath.replace(':', ' ')
        elif i == '<':
            fullpath = fullpath.replace('<', ' ')
        elif i == '>':
            fullpath = fullpath.replace('>', ' ')
        elif i == '?':
            fullpath = fullpath.replace('?', ' ')
        # elif i == '/':
        #     fullpath = fullpath.replace('/', ' ')
        elif i == '\\':
            fullpath = fullpath.replace('\\', ' ')
        elif i == '|':
            fullpath = fullpath.replace('|', 'test')
    return fullpath



rootDir = './test'
for dirName, subdirList, fileList in os.walk(rootDir):
    if check_chars(dirName):
        os.replace(dirName, replace_chars(dirName))

for dirName, subdirList, fileList in os.walk(rootDir):
    for fileName in fileList:
        if check_chars(fileName):
            os.replace(fileName, replace_chars(fileName))