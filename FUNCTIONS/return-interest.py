def interest( princ, rate, time ):
    
    """return simple interest that has to be paid"""
    
    simple_interest = (princ * rate *time)/100
    return simple_interest

value = interest(5000000, 0.8, 5)
print("the interest to be paid is: ", value)
