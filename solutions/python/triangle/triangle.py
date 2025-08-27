def is_triangle(sides):
    a, b, c = sides
    return (
        a + b > c 
        and a + c > b
        and b + c > a
    )

def equilateral(sides):
    a, b, c = sides
    return (
        is_triangle(sides)
        and a == b == c
    )


def isosceles(sides):
    a, b, c = sides
    return (
        is_triangle(sides)
        #and not equilateral(sides)
        and (a == b or a == c or b == c)
    )


def scalene(sides):
    a, b, c = sides
    return (
        is_triangle(sides)
        and a != b and b != c and c != a
    )
