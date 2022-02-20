while True:
    validOptions = ["P", "Directory", "Banners", "Channel Letters", "Vinyl", "Exit"]
    for item in validOptions:
        item = item.lower()
        
    print(validOptions)
    userInput = input("Please select a sign product: ")
    if(userInput.lower() in validOptions):
        if(userInput == "exit"):
            print("...returning to previous menu...")
            break
        elif(userInput == "p"):
            print("These are metal parkig signs")
        elif(userInput == "directory"):
            print("you'll find these at building entrances.")

    else:
        print("you didnt make a good selection. Try again...")
