print("Hello! This program will format your text <3 ")

text = input("Please input your text here: ")

print("\nGreat! Now, how do you want to format your text? \n[1]\tUpper Case\n[2]\tLower Case\n[3]\tNone")

while True:
    try:
        choice = int(input("Please enter your choice here: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if choice in [1,2,3]:
        match choice:
            case 1: 
                print(text.upper())
                print("\nThank you for using the program!")
                break
            case 2: 
                print(text.lower())
                print("\nThank you for using the program!")
                break
            case 3:
                print(text)
                print("\nThank you for using the program!")
                break
    else:
        print("Invalid choice! Please try again.")