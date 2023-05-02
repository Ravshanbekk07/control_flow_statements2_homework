def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    x1 = n%10
    number = n//10
    #print(x1)
    x2 = number%10
    number = number//10
    #print(x2)

    x3 = number%10
    number = number//10 
    #print(x3)

    x4  = number%10
    number= number//10
    #print(x4)
    x5 = number%10
    number = number//10
    #print(x5)
    if x1>x2 and x1>x3:
        if x1>x4 and x1>x5:
         print(x1)
    if x2>x1 and x2>x3:
        if x2>x4 and x2>x5:
         print(x2)
    if x3>x1 and x3>x2:
        if x3>x4 and x3>x5:
         print(x3)
    if x4>x2 and x4>x3:
        if x4>x1 and x4>x5:
         print(x4)
    if x5>x2 and x5>x3:
        if x5>x4 and x5>x1:
         print(x5)
         
    
            
    return


v = main(79546)
print(v)
