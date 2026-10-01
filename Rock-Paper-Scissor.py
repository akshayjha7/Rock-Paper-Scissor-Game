import random

list=["Rock","Paper","Scissor"]

print("Select anyone from the list of",list)

user=input("Enter your choice: ")
comp=random.choice(list)

print(f"user choice: {user} , computer choice: {comp}")

if user==comp:
    print("Both choices are same,Match Tie!")
elif user=="Rock":
    if comp=="Paper":
        print("Paper covers Rock,Computer Wins!")
    else:
        print("Rock smashes Scissor,You Wins!")
elif user=="Paper":
    if comp=="Scissor":
        print("Scissor cuts Paper,Computer Wins!")
    else:
        print("Paper covers Rock,You Wins!")
elif user=="Scissor":
    if comp=="Rock":
        print("Rock smashes Scissor,Computer Wins!")
    else:
        print("Scissor cuts Paper,You Wins!")
else:
    print("Invalid Input!,Try Again")