#https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d
def solution(text, ending):
    return ending in text[len(text)-len(ending):]