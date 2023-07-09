def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a + b < c:
        return False
    if b + c < a:
        return False
    if a + c < b:
        return False
    if a == b:
        if b == c:
            return True
    return False

def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a + b < c:
        return False
    if b + c < a:
        return False
    if a + c < b:
        return False
    if equilateral(sides) == False:
        if a == b:
            return True
        if b == c:
            return True
        if c == a:
            return True
    return False



def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a + b < c:
        return False
    if b + c < a:
        return False
    if a + c < b:
        return False
    if equilateral(sides) == False:
        if isosceles(sides) == False:
            return True
    return False
