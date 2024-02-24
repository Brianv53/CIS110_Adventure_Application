print(f"Hello, you are about to embark on an adventure about someone and their friends.")
print(f"Before we begin, there are a few questions you need to answer. ")
print(f"When you type your anwser, press enter. ")
input(f"\nPress enter to begin...")

keepPlaying = "yes"
while keepPlaying.lower() == "yes":

    mainName = input(f"\nWhat is your characters name: ")
    while (len(mainName) == 0):
        mainName = input(f"Please enter a name: ")

    sigName = input(f"\nWhat is your character's significant others name: ")
    while (len(sigName) == 0):
        sigName = input(f"Please enter a name: ")

    favRestaurant = input("Please enter your favorite restaurant: ")    while (len(favChocolate) == 0):
        favChocolate = input(f"Please enter your favorite chocolate: ")

    favFlower = input(f"\nWhat is your favorite flower: ")
    while (len(favFlower) == 0):
        favFlower = input(f"Please enter your favorite flower: ")

    favRestaurant = input(f"\nWhat is your favorite restaurant: ")
    while (len(favRestaurant) == 0):
        favRestaurant = input(f"Please enter a restaurant: ")
    
    print(f"\nWhile at home, {mainName} wants to get {favChocolate} and an arrangement of {favFlower} for {sigName}.")
    print(f"\nHowever, {mainName} also wants to spend time with friends.")
    print(f"\n{mainName} really loves {sigName} and wants to spend Valentine's Day together.")
    print(f"\nBut {mainName} hasn't seen friends in years and was invited to {favRestaurant} with them.")

    goOnDate = input(f"\nDoes {mainName} go to store to get {favChocolate} and {favFlower}? Type yes or no: ")
    while goOnDate.lower() != "yes" and goOnDate.lower() != "no"
        goOnDate = input(f"Type yes or no: ")

    if goOnDate == "yes":
        print(f"\n{mainName} goes out to get {favChocolate} and {favFlower} for {sigName}.")
        print(f"When {mainName} returns, {sigName} is so surprised and thrilled to recieve the gifts.")
        print(f"")
