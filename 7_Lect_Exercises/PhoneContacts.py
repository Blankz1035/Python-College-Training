# Program to demonstrate the use of a dictionary with phone contacts.


# create dict
contacts = {}

while True:
    choice = input("\nPrint Add Edit Delete Quit")

    if choice.lower()[0] == "p":
        if len(contacts) == 0:
            print("No contacts to display")
        else:
            print("Numbers in contacts:")
            for name in contacts.keys():
                print(name, "\t", contacts[name])

    elif choice.lower()[0] == "a":
        new_name = input("Enter a new name: ")

        if new_name in contacts:
            print("Contact already exists.")
        else:
            new_number = int("Enter contacts number: ")
            contacts[new_name] = new_number

    elif choice.lower()[0] == "e":
        name = input("Enter name to edit: ")
        if name in contacts:
            new_number = int("Enter new number: ")
            contacts[name]= new_number

    elif choice.lower()[0] == "d":
        name = input("Enter name to delete: ")
        # look before we leap concept:
        if name in contacts:
            del contacts[name]
        else:
            print("Contact not available: ", name)

    elif choice.lower()[0] == "q":
        break
    else:
        print("Invalid Option..")