def main(a,b):
    """
    Return zero if the numbers are equal, return the larger one if they are not equal.
    Args:
        a: First number.
        b: Second number.
    Returns:
        int: return answer.
    """
    if a == b:
        print(0)
    if a!=b:
        if a>b:
            print(a)
        else:
            print(b)
        print()
    return 


v = main(3,6)
print(v)