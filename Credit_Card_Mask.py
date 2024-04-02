#https://www.codewars.com/kata/5412509bd436bd33920011bc
def maskify(cc):
    final=''
    if len(cc) <= 4 :
        final = cc
    else:
        lenght = len(cc)
        cc_last = cc[lenght-4:lenght]
        cc_without_last = cc[0:lenght-4]
        for element in cc_without_last:
            cc_without_last = cc_without_last.replace(element,'#')
        final = cc_without_last + cc_last
    return final