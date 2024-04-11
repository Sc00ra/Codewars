#https://www.codewars.com/kata/52c4dd683bfd3b434c000292
def is_interesting(number, awesome_phrases):
    str_number = str(number)
    increment = '1234567890'
    decrese = '9876543210'
    if number == 98 or number == 99:
        return 1

    if number < 100:
        return 0
    if number in awesome_phrases:
        return 2

    if len(list(set(str_number))) == 1:
        return 2

    if str_number in increment or str_number in decrese:
        return 2

    if str_number == str_number[::-1]:
        return 2
    if str_number[1:] == "0" * (len(str_number)-1):
        return 2

    next1 = number + 1
    next2 = number + 2

    if next1 in awesome_phrases or next2 in awesome_phrases:
        return 1
    if str(next1) in increment or str(next1) in decrese or str(next2) in increment or str(next2) in decrese:
        return 1
    if len(list(set(str(next1)))) == 1 or len(list(set(str(next2)))) == 1:
        return 1
    if str(next1) == str(next1)[::-1] or str(next2) == str(next2)[::-1]:
        return 1
    if str(next1)[1:] == "0" * (len(str(next1))-1) or str(next2)[1:] == "0" * (len(str(next2))-1):
        return 1

    return 0
    


print(is_interesting(98, [1337, 256]))
     
