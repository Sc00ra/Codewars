#https://www.codewars.com/kata/56541980fa08ab47a0000040

def printer_error(s):
    return str(len("".join(element for element in s if element not in ['a','b','c','d','e','f','g','h','i','j','k','l','m'] ))) + '/' +str(len(s))

print(printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"))

