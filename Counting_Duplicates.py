#https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
def duplicate_count(text):
    # Your code goes here
    
    x=0
    known = {}
    text = text.lower()
    for element in text:
        known[element] = known.get(element,0) + 1
    for element2 in known.values():
        if element2 > 1:
            x += 1
    
    return x
duplicate_count("Indivisibilities")