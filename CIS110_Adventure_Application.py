print("Hello user, you are about to embark on an imaginary journey.")
print("I will ask you some questions. When you type your answer, press enter.")
mainName = input("\nWhat is the name of your character?")
while len(mainName) == 0:
    mainName = input("Please enter a name: ")
sigName = input("\nWhat is the name of your characters significant other?")
while len(sigName) == 0:
    sigName = input("Please enter a name: ")
flowerType = input("\nWhat is your favorite flower?")
while len(flowerType) == 0:
    flowerType = input("Please enter your favorite flower: ")
chocolateType = input("\nWhat is your favorite chocolate?")
while len(chocolateType) == 0:
    chocolateType = input("Please enter your favorite chocolate: ")
favRestaurant = input("\nWhat is your favorite restaurant?")
while len(favRestaurant) == 0:
    favRestaurant = input("Please enter your favorite restaurant: ")