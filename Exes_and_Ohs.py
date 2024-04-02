#https://www.codewars.com/kata/55908aad6620c066bc00002a
def xo(s):
    x=0
    o=0
    for element in s:
        if(element == 'x' or element == 'X'):
            x+=1
        if(element == 'o' or element == 'O'):
            o+=1
    if(x==o):
        return True
    return False


