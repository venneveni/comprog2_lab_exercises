try:
    f = open("message.txt","x")
    print("File is created successfully!")
except FileExistsError:
    print("File is already created")


while True:
    print("\nSimple Messaging App")
    print("\n 1. Send Message\n 2. View all message\n 3. Exit")
    try:
        choice = int(input("Enter choice(1-3):  "))
        
        if choice == 1:
            message = (input("Write a message: ")) + "\n"
            
            with open("message.txt","a") as f:
                f.write((message))
                print("Sent!")
            
        elif choice == 2:
            with open("message.txt") as f:
                print(f.read())
        else:
            print("Exiting program")
            break
    except ValueError:
        print("\nError input, please try again")
