highestnum = 0
# initiate highest num as 0 and replace this 0 inside our for loop 
for i in range(0, 4, 1):
    userinput = input("number please...")
    userint = int(userinput)
    print("User entered: " + str(userinput))
    if userint > highestnum:
        highestnum = userint
        print("Updating highest number...")
    else:
        print("This is not the highest number")
        print("the highest number entered is: " + str(highestnum))