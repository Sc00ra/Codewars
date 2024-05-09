#https://www.codewars.com/kata/545cedaa9943f7fe7b000048
def is_pangram(s):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    used  = []

    for element in s.lower():
        if element in alphabet and element not in used:
            used.append(element)
    if len(used) == len(alphabet):
        return True
    else: 
        return False