#https://www.codewars.com/kata/55cbd4ba903825f7970000f5
def get_grade(s1, s2, s3):
    return 'A' if (s1+s2+s3)/3 >=90 else "B" if (s1+s2+s3)/3 >=80 else 'C' if (s1+s2+s3)/3 >=70 else 'D' if (s1+s2+s3)/3 >=60 else 'F'
    