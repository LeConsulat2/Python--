
age = 10
height = 100

if age >= 8 and height >= 135:
    print("You can ride the ride!")


if age >= 17 or height >= 160:
    print("You can ride the super ride!")
else: print("Go sit down")

if height < 120:
    print("You cannot ride any rides 🤣, shame!")
elif height < 135:
    print("You can ride level 1 rides") 
elif height < 180:
    print("Do whatever you want")
else:
    print("Sorry, you are too tall to ride")

service = 25
employee = "permanent"

if 5 <= service <= 9 and employee == "permanent":
    print("You get an extra holiday")
elif 10 <= service <= 14 and employee == "permanent":
    print("You get an extra 2 weeks of long service leave")
elif 15 <= service <= 20 and employee == "permanent":
    print("You are just lucky still to have your position; just be grateful")
else:
    print("Get ready to be replaced by an AI soon")

