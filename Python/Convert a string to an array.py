#https://www.codewars.com/kata/57e76bc428d6fbc2d500036d
def string_to_array(s):
    return list(s.split()) if s != '' else ['']


print(string_to_array(""))

