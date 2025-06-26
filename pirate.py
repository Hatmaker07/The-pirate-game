import random
players = 0
players2 = 0
select = []
idk = []
ttr = 1
something = 0
selected = 0
temp = 0
temp2 = 0
high = 0
loop = 7
loop2 = 7
mode = 0
if ttr == 1:
    print("Tutorial?\n(y/n)")
    ttr = input()
if ttr == "y":
    print("Mode 1: players add tiles and random one is chosen")
    print("Mode 2: random tile is selected\nMode 3: 2 random tiles are selected and 1 is chosen by vote")
    print("To quit program, input q when asked to quit.")
    print("first number represents a letter, 1 = a, 2 = b... 7 = g")
    print("to just play the regular pirate game, use mode 2 and press enter when it asks you to quit\nto get a new number")
    print("to use the choose next square, input c when the program asks you to quit")
print("Select mode")
mode = int(input())
while(loop >= 1):
    something = something + 10
    loop2 = 7
    while(loop2 >= 1):
        something = something + 1
        select.append (something)
        loop2 = loop2 - 1
    loop = loop - 1
    something = something - 7
slength = len(select) - 1
if mode == 1:
    print("How many players?")
    players = int(input())
    players2 = players
    while temp2 != "q":
        while(players2 >= 1):
            print("add selected tile here")
            temp = int(input())
            idk.append(temp)
            players2 = players2 - 1
            temp = random.choice(select)
            idk.append(temp)
        temp = random.choice(idk)
        print(temp)
        idk.clear()
        print("Quit?")
        temp2 = input()
        players2 = players
        while(temp2 == "c"):
            temp2 = int(input())
            select.remove(temp2)
            print("Quit?")
            temp2 = input()
if(mode == 2):
    while temp2 != "q":
        temp = random.choice(select)
        print(temp)
        select.remove(temp)
        print("Quit?")
        temp2 = input()
        while(temp2 == "c"):
            temp2 = int(input())
            select.remove(temp2)
            print("Quit?")
            temp2 = input()
while temp2 != "q":
    if(mode == 3 and temp2 != "c"):
        temp = random.choice(select)
        temp2 = random.choice(select)
        print("1 is ", temp)
        print("2 is ", temp2)
        print("Choose 1 or 2")
        ttr = int(input())
        if ttr == 1:
            print(temp)
            select.remove(temp)
        else:
            print(temp2)
        select.remove(temp2)
    print("Quit?")
    temp2 = input()
    while(temp2 == "c"):
        temp2 = int(input())
        select.remove(temp2)
        print("Quit?")
        temp2 = input()