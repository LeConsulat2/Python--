direction = input("Which direction? ")

match direction:
    case "north":
        print("Up")
    case "south":
        print("Down")
    case "East":
        print("Right")
    case "West":
        print("Left")
    case _:
        print("Not a valid direction")    