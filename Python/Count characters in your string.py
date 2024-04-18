#https://www.codewars.com/kata/52efefcbcdf57161d4000091

def count(s):
    result = {}
    for element in s:
        if element not in result.keys():
            result[f"{element}"] = s.count(element)
    return result

print(count("aba"))