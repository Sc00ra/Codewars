#codewars.com/kata/5556282156230d0e5e000089

def dna_to_rna(dna):
    return dna.translate(str.maketrans({"T":"U"}))  