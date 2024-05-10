#https://www.codewars.com/kata/5842df8ccbd22792a4000245
def expanded_form(num):
    return ''.join(str(num)[i] + '0'*(len(str(num))-1-i) + ' + ' for i in range(len(str(num))) if str(num)[i] != '0' )[0:-3]


print(expanded_form(70304))
