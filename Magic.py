import random

random_number = random.randint(1, 10)
print(random_number)

name = "Mike"

question = "Will today be a good day?"

if name == "":
    print("Question: " + question)
else:
  print(name + " asks: " + question)

if question == "":
  print("Magic 8-Ball cannot provide an answer without given a question")

answer = ""

if random_number == 1:
    answer = "I'd say yes."
elif random_number == 2:
    answer = "Perhaps."
elif random_number == 3:
    answer = "Undoubtetly"
elif random_number == 4:
    answer = "Can't find answer, have another go."
elif random_number == 5:
    answer = "Try again another time."
elif random_number == 6:
    answer = "Maybe its bet to not say."
elif random_number == 7:
    answer = "Probably a no."
elif random_number == 8:
    answer = "Looking like a yes."
elif random_number == 9:
    answer = "Mot looking good at all."
elif random_number == 10:
    answer = "Unfortunately it looks like no."
else: 
    answer = "Error"

print("Magic 8-Ball says: " + answer)

print("Magic 8-Ball says: Would you like to ask another?")
  
