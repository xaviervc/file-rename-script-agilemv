
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