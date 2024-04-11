#https://www.codewars.com/kata/52fba66badcd10859f00097e
def disemvowel(string_):
    return string_.translate(str.maketrans({'a':'','A':"",'e':'','E':'','I':"",'i':'','O':'','o':'','U':'','u':''}))  