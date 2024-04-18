#https://www.codewars.com/kata/530e15517bc88ac656000716

def rot13(message):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alphabet_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    result = ''
    for element in message:
        if element in alphabet or element in alphabet_upper:
            if element in alphabet_upper:
                index = alphabet_upper.index(element)
                if index + 13 >= len(alphabet_upper):
                    index = 13 - (len(alphabet) - index)
                else: 
                    index = index + 13
                result += alphabet_upper[index]
            if element in alphabet:
                index = alphabet.index(element)
                if index + 13 >= len(alphabet):
                    index = 13 -(len(alphabet) - index)
                else: 
                    index = index + 13
                result += alphabet[index]
        else:
            result += element
    return result

print(rot13('Test'))