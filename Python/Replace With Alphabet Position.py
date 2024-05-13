#https://www.codewars.com/kata/546f922b54af40e1e90001da

def alphabet_position(text):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    positions = ''
    for element in text.lower():
        if element in alphabet:
            positions += f"{alphabet.index(element)+1} "
    return positions[0:-1]

print(alphabet_position("The sunset sets at twelve o' clock."))