#https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python

def find_short(s):
    list_l = []
    s = s.split(" ")
    for element in s:
         list_l.append(len(element))
        
    list_l.sort()
    l = list_l[0]
    
  
    return l



find_short("bitcoin take over the world maybe who knows perhaps")