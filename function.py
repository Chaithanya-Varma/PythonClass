def odd_even(num):
    """
    This function named odd_even & returns odd & even with respect tonumber given by user
    INPUT: num
    OUTOUT: odd&even
    created date
    """
    if type(num) == int:
        if num%2 == 0:
            print( "even")
        else:
            print("odd")
    else:
        print("please enter intiger")
        


odd_even(22)