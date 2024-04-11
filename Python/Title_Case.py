#https://www.codewars.com/kata/5202ef17a402dd033c000009

def title_case(title, minor_words=''):
    title = title.lower().split()
    minor_words = minor_words.lower().split()
    string = ''
    if title == '':
        return string
    for i in range(0,len(title)):
        if i == 0:
            title[i] = title[i].title()
        if title[i] not in minor_words:
            title[i] = title[i].title()
        string = string + " " + title[i]
    string = string[1:]
    return string

