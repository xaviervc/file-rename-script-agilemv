import os
import logging

def check_chars(dirName):
    # Removed '/' in dirName or from the list as it is causing false positives due to the Linux file system
    if '\"' in dirName or '*' in dirName or ':' in dirName or '<' in dirName or '>' in dirName or '?' in dirName or '\\' in dirName or '|' in dirName:
        return True
    else:
        return False

def replace_chars(fullpath):
    # Commented out '/' due to filepath false positive on linux
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
            fullpath = fullpath.replace('|', ' ')
    return fullpath

logging.basicConfig(filename='char_replacement.log', level=logging.DEBUG)

rootDir = './test'
for dirName, subdirList, fileList in os.walk(rootDir):
    if check_chars(dirName):
        logging.info(f'Illegal Character Found at Directory {dirName}')
        replacement_string = replace_chars(dirName)
        logging.info(f'Replaced by {replacement_string}')
        os.replace(dirName, replace_chars(replacement_string))

for dirName, subdirList, fileList in os.walk(rootDir):
    for fileName in fileList:
        if check_chars(fileName):
            logging.info(f'Illegal Character Found at Filename {fileName}')
            replacement_string = replace_chars(dirName + '/' + fileName)
            logging.info(f'Replaced by {replacement_string}')
            os.replace(dirName + '/' + fileName, replacement_string)