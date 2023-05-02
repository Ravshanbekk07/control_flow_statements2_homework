def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a<b and a>c:
        print (a)
    elif b<a and b>c:
        print(b) 
    elif c<a and c>b:
        print (c)
    return

v = main(5,4,1)
print(v)