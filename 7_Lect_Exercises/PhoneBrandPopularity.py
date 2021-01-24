# Program to demonstrate dictionaries: Popularity of phone choice.

phones = {}

while True:
    phone_name = input("Enter phone name / q to quit: ")
    
    if phone_name.lower() == "q":
        print("Thank you. program done.\n")
        break

    if phone_name in phones:
        phones[phone_name] = phones[phone_name] + 1
    else:
        phones[phone_name] = 1


for p in phones.keys():
    print(f"{p} {phones[p]}")

print(f"Most popular phone: {max(phones, key=phones.get)} with {max(phones.values())}")