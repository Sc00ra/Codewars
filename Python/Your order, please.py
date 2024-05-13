#https://www.codewars.com/kata/55c45be3b2079eccff00010f

def order(sentence):
    result = ['']*len(sentence.split(" "))
    final = ''
    if sentence != "":
        sentence = sentence.split(" ")
    for element in sentence:
        for letter in element:
            if letter in ["1",'2','3','4','5','6','7','8','9']:
                result[int(letter)-1] = element
    for element in result:
        final += f"{element} "
    return final[0:-1]



print(order("is2 Thi1s T4est 3a"))