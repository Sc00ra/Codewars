#https://www.codewars.com/kata/5168bb5dfe9a00b126000018

def solution(string):
    string_reversed = ''
    for i in range(1,len(string)+1):
        string_reversed += string[-i]
    return string_reversed


print(solution('world'))