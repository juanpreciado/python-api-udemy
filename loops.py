myVariable = 'hello'

for character in myVariable:
    print(character)

myList = [1,2,3,4,5]

for number in myList:
    print(number ** 2)

userWantsNumber = True
while userWantsNumber == True:
    print(10)
    userInput = input("SHould we print again ? (y/n)")
    if userInput == 'n':
        userWantsNumber = False