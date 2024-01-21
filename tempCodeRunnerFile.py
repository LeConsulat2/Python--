try:
    print(name)
except NameError:    
    print("That is not a name")
    55/0
except ZeroDivisionError:
    print("Dividing by 0?, find a new career pathway please")