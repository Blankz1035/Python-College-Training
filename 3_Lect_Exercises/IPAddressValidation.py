# Program to validate IP Address input from user.

count = 0
num = int(input("Enter number: "))
ip_address = ""

while (True):

    # Number is valid.
    if 0 <= num <= 255:
        # Check if empty = If empty then 
        if not ip_address:
            ip_address = str(num)
            count += 1
        else:
            ip_address = ip_address + "." + str(num)
            count += 1
    # Number is not valid.
    else:
        print("Incorrect number entered.")

    # Control after 4 numbers entered.
    if count == 4:
        break

    num = int(input("Enter number: "))

print(ip_address)