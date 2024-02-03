password_correct = True

if password_correct:
    print ("Here is your money")
else:
    print ("You are a thief")    

# separate code
winner = 10

if winner > 10:
  print("winner is greater than 10")
elif winner  < 10:
  print("winner is less than 10")
else:
  print("winner is 10")
# separate code

from random import randint
user_choice = int(input("Choose number."))

pc_choice = randint(1, 50)

if user_choice == pc_choice:
    print("You won!")
elif user_choice > pc_choice:
    print("Need to be lower computer chose", pc_choice)
elif user_choice < pc_choice:
    print("Need to be higher computer chose", pc_choice)
    
# separate code

from random import randint

pc_choice = randint(1, 50)

while True:
    user_choice = int(input("Choose a number: "))

    if user_choice == pc_choice:
        print("You won!")
        break
    elif user_choice > pc_choice:
        print("Need to be lower")
    elif user_choice < pc_choice:
        print("Need to be higher")
        
# separate code
distance = 0

while distance < 20:
    print("I am running:", distance, "km")
    distance = distance + 1
    
# separate code
days_of_week = ["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"]

print(days_of_week[2])

days_of_week.reverse()

print(days_of_week)
# separate code (for loops)
websites = (
  "facebook.com",
  "youtube.com"
)

for each in websites:
  print("go to ", each)
#separate
websites = (
    "facebook.com",
    "https://youtube.com",
    "instagram.com"
)

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    print(website)

#separate
from requests import get

websites = (
  "facebook.com",
  "https://youtube.com",
  "instagram.com"
)

results = {
  
}

for website in websites:
  if not website.startswith("https://"):
      website = f"https://{website}"
  response = get(website)
  if response.status_code == 200:
   results[website] = "ok"
  else:
   results[website] = "Failed"

print(results)


