import random         #Use import random to chose values randomly in a dice.

print("Welcome to this game of DICE")
print("")
a= input("Your Name:")
print("")
print("Hello!",a,"Here are some rules for this game.")
print("")
print("Rule No. 1 --> You can play till you want.")
print("Rule No. 2 --> Press 'c' and enter to Continue the game.")
print("Rule No. 3 --> Press 'e' and enter to Exit the game.")
print("At the end you can see your score")
print("")
n= input("Write 'play' to start: ")
print("")
print("Let's Play")
print("")

i= 0

while (n!= "e" and n == "c") or n == "play":
    c= random.randint(1,6)               # randint function gives number randomly from the given range including ending value.
    d= int(input("Your Choice from 1 To 6:"))
    print("Computer Choice is:",c)
    if c == d:
        print("You Won")
        i+= 1                            # increasing the score on each win.
        n= input("Do you want to continue?: ")
    else:
        print("You Lose")
        n= input("Do you want to continue?: ")
print("")
print("Your Score is:",i)