test_string = '\" * : < > ? / \\ |'

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

print(check_for_chars(test_string))