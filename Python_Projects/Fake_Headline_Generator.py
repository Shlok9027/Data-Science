import random

# importing random 

Subjects = [
    "Shreya",
    "Abhishek",
    "Ankita",
    "Prateek",
    "Akancha",
    "Virat",
    "Anushka",
    "Hrithik",
    "Jethalal",
    "Daya",
    "Ricksaw Wala ",
    "Motu from Motu Patlu",
    "Patlu from Motu Patlu",

]


actions = [
    "Lauches",
    "Destroys",
    "Cancels",
    "eats",
    "throws",
    "created",
    "celebrates",
    "needs",
]

places_or_things = [
    "at Red Fort",
    "a plate of samosas",
    "inno village",
    "at Ganga River",
    "a party",
    "a wedding",
    "during IPL match",
    "at moon"

]

while True:
    subject = random.choice(Subjects) 
    action = random.choice(actions) 
    places_or_thing = random.choice(places_or_things)

    headline = f" BREAKING NEWS :: {subject} {action} {places_or_thing} ::"

    print("\n" + headline)

    user_input = input("\nDo You Want To Continue [Yes / No] : ").strip().lower()

    if user_input == "no":
        break
    else:
        continue

print("Thank You For Using Fake News Generator")