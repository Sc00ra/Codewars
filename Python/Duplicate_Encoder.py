#https://www.codewars.com/kata/54b42f9314d9229fd6000d9c
def duplicate_encode(word):
    final = ''
    for element in word.lower():
        if word.count(element) > 1:
            final = final + ")"
        else:
            final = final + "("

    return final

duplicate_encode("recede")