## high ho cherry o
import random 
kirchBaume = 10 ## tree
korb = 0 ## basket
nummerVonSpiele = 0 ## counting number of rounds for the actual problem
nummerVonGrossSpiele = 0 ## counting number of games for the actual problem
winnenUnterVier = 0 ## counting number of wins that happened with a round count of less than four
failenUeberZwanzig = 0 ## counting number of games that go over 20

grossLaufNummer = False ## init checking for large numbers, disables printing
kleinLaufNummer = False ## init checking for small numbers, enables verbose

## get user input
laufNummer = int(input("how many times do you want to run this? \n (note that values over 10000000 take a very long time and are not reccomended) \n"))

if laufNummer >= 10000000:
    grossLaufNummer = True

if laufNummer <= 1000: ## IMPLEMENT THIS!!
    kleinLaufNummer = True

win = False ## init win

while nummerVonGrossSpiele != laufNummer: ## 1 billion will run for about 11 days lmao
    nummerVonSpiele = 0 ## resetting rounds
    kirchBaume = 10 ## reset the counts!
    korb = 0
    win = False
    while True: ## the for loop only checked whenever the while loop starts again, not when it runs
        einsDurchSieben = random.randint(1,7)
        if kleinLaufNummer == True:
            print(f"your roll is {einsDurchSieben}")

        if kirchBaume < 0: ## killing negative numbers
            kirchBaume = 0

        if kirchBaume <= 0 or korb >= 10:
            if grossLaufNummer == False:
                print("win!")
            win = True
            break

        if korb < 0 or korb > 10 or kirchBaume > 10: 
            print("broke") ## debugging is important
            break

        if einsDurchSieben == 1:
            korb = korb + 1
            kirchBaume = kirchBaume - 1
            if kleinLaufNummer == True:
                print(f"basket: {korb}")
                print(f"tree: {kirchBaume}")

        elif einsDurchSieben == 2:
            if kirchBaume <= 1: ## not allowing - ints for cherry
                #print("win!")
                win = True
                break
            korb = korb + 2
            kirchBaume = kirchBaume - 2
            if kleinLaufNummer == True:
                print(f"basket: {korb}")
                print(f"tree: {kirchBaume}")
            
        elif einsDurchSieben == 3:
            if kirchBaume <= 2: ## not allowing - ints for cherry
                #print("win!")
                win = True
                break
            korb = korb + 3
            kirchBaume = kirchBaume - 3
            if kleinLaufNummer == True:
                print(f"basket: {korb}")
                print(f"tree: {kirchBaume}")

        elif einsDurchSieben == 4:
            if kirchBaume <= 3: ## not allowing - ints for cherry
                #print("win!")
                win = True
                break
            korb = korb + 4
            kirchBaume = kirchBaume - 4
            if kleinLaufNummer == True:
                print(f"basket: {korb}")
                print(f"tree: {kirchBaume}")

        elif einsDurchSieben in (5, 6): ## 5 or 6 is always true according to claude
            if korb > 0:
                korb -= 1
                kirchBaume += 1
            if kleinLaufNummer == True:
                print(f"basket: {korb}")
                print(f"tree: {kirchBaume}")

        elif einsDurchSieben == 7:
            korb = 0
            kirchBaume = 10
            if kleinLaufNummer == True:
                print(f"basket: {korb}")
                print(f"tree: {kirchBaume}")
    
        nummerVonSpiele = nummerVonSpiele + 1 ## increasing the number of rounds

    if win == True and nummerVonSpiele <= 4:
            winnenUnterVier = winnenUnterVier + 1 ## no else loop required

    if nummerVonSpiele >= 20:
        failenUeberZwanzig = failenUeberZwanzig + 1 

    nummerVonGrossSpiele = nummerVonGrossSpiele +1
    if grossLaufNummer == True:
        print(nummerVonGrossSpiele)

print(f"wins under 4 rounds:{winnenUnterVier}")

print(f"fails above 20 rounds:{failenUeberZwanzig}")

## german notes: 
# siehst du das auto dort? - do you see the car? (over there)
# das moechte ich gern haben - i would like to have that
# 
# kennst du diese leute? - do you know these people?
# ja, die kenne ich gut - yes i know these people well 
# aber does not change word order really :D