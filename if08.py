def main(number):
    """
    Return the days of the week, return the days of the week according to the numbers 1 to 7.
    Use the elif statments.
    1: "Monday"
    2: "Tuesday"
    3: "Wednesday"
    4: "Thursday"
    5: "Friday"
    6: "Saturday"
    7: "Sunday"
    Args:
        number: Number of the day.
    Returns:
        str: return answer.
    """
    if number == 1:
        print('monday')
    elif number==2:
        print('tuesday')
    elif number == 3:
        print('wednesday')
    elif number == 4:
        print('thursday')
    elif number ==5:
        print('friday')
    elif number == 6:
        print('saturday')
    elif number==7:
        print('sunday')
    return
    
v = main(5)
print(v)