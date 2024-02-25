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

    favChocolate = input(f"\nWhat is your favorite chocolate: ")
    while (len(favChocolate) == 0):
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

    goGetFlowers = input(f"\nDoes {mainName} go to store to get {favChocolate} and {favFlower}? Type yes or no: ")
    while goGetFlowers.lower() != "yes" and goOnDate.lower() != "no"
        goGetFlowers = input(f"Type yes or no: ")

    if goGetFlowers == "yes":
        print(f"\n{mainName} goes out to get {favChocolate} and {favFlower} for {sigName}.")
        print(f"When {mainName} returns, {sigName} is so surprised and thrilled to recieve the gifts.")
        print(f"{sigName} tells {mainName} how much they love each other and asks to go to {favRestaurant}.")
    else:
        print(f"\n{mainName} goes to {favRestaurant} with friends.")
        print(f"{mainName} starts to feel resentment for not spending time with {sigName}.")
        print(f"As feelings of guilt torments {mainName}'s mind, he starts to question his decision.")

    goOnDate = input(f"\nShould {mainName} take {sigName} to {favRestaurant} for a date? Type yes or no: ")
    while goOnDate.lower() != "yes" and goOnDate.lower() != "no":
        goOnDate = input(f"Type yes or no: ")
    
    if goOnDate == "yes":
        print(f"\n{mainName} takes {sigName} on a date to their favorite restaurant {favRestaurant}.")
        print(f"They have a lovely time together, as they are talking, they can feel their connection growing.")
        print(f"{mainName} and {sigName} order the largest plate of pasta to share.")
    else:
        print(f"\n{mainName} would rather not spend time with {sigName} at this point.")
        print(f"{mainName} feels his connection with {sigName} isn't as strong as it used to be when they first started dating.")
        print(f"{mainName} really starts to feel the guilt because he wants to love {sigName} but can't seem to find the feelings anymore.")
        print(f"{mainName} starts eating pounds of {favChocolate} to help cope with his feelings of guilt.")
    
    if goGetFlowers == "yes" and goOnDate == "yes":
        print(f"\n{mainName} has {favFlower} arranged at {favRestaurant} for {sigName}.")
        print(f"She is happy and thrilled with {mainName}'s effort to make this day special.")
        print(f"Later, when they are finished with dinner. {mainName} reaches into his pocket.")
        print(f"{mainName} pulls out a ring and says 'Marry me {sigName} I'm so in love with you.'")
        print(f"{sigName} is so shocked she can't do anything but nod her head yes.")
        print(f"{mainName} and {sigName} now live a happy life together where they started a family together.")
    elif goGetFlowers == "no" and goOnDate == "no":
        print(f"\nAfter returning home from spending time with friends. {mainName} finds another car sitting in the driveway.")
        print(f"{mainName} walks inside to find {sigName} cheating on him with the guy friend she told him not to worry about.")
        print(f"Infuriated by the situation, {mainName} kicks {sigName} and her new boyfriend out of the house.")
        print(f"{mainName} eats another pound of {favChocolate} as waves of emotions crash through his brain.")
        print(f"Now {mainName} really wishes he treated {sigName} better as he still loves her.")
        print(f"{mainName} now lives a life filled with sorrow and regret as he is having trouble dating others.")
    else:
        print(f"\n{mainName} enjoyed his day, made time for both {sigName} and friends.")
        print(f"{mainName} returns home with {sigName} where they settle in for the night.")
        print(f"Before they go to bed, they watch a movie together.")
    print(f"\nThe End")

    keepPlaying = input(f"\nDo want to play again? Type yes or no: ")
    while keepPlaying.lower() != "yes" and keepPlaying.lower() != "no":
        keepPlaying = input(f"Type yes or no: ")
