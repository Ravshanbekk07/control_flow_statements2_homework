def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a>b:
        print (a)
        if a>c:
            print(a)
    elif b>c:
        print (b)
    elif b>a:
        print (b)
    else:
        print(c)
    
    return
v =  main(1,4,2)
print(v)
