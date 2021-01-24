# Program which inputs number of dependents and then determines and displays the corresponding income limit.  

# Variables - Grants available
grant1 = "€39875"
grant2 = "€43810"
grant3 = "€47575"

# Number of dependents
dependents = int(input("Enter the number of dependents: "))

# Conditions
# 1. < 4 39875
# 2. 4 to 7 - 43810
# 3. > 8 - 47575
if dependents:
    if 0 <= dependents < 4:
        print("The income limit is: " , grant1)
    elif 4 <= dependents <= 7:
        print("The income limit is: " , grant2)
    elif dependents > 8:
        print("The income limit is: " , grant3)
    else:
        print("Your input was incorect.")
else:
    print("Input not added.")

