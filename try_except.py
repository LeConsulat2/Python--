name = "Jonathan"

try:
    print(name)
except NameError:    
    print("You didnt put the name")
    55/0
except ZeroDivisionError:
    print("Dividing by 0?, find a new career pathway please")


def upper(word):
    if len(word) == 0:
        raise KeyError("The word has to have one letter, come on")
    return word.upper()

print(upper(""))

