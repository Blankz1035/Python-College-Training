# Program to demonstrate the use of functions

# Functions
def happybirthday(name: str) -> str:
    """Function to say happy birthday using the name provided.

    Args:
        name (str): [Name of the person whos birthday it is.]

    Returns:
        None. Print out results within function.
    """

    print("Happy Birthday to You..")
    print("Happy Birthday to You..")
    print("Happy Birthday dear, ", name)
    print("Happy Birthday to You..")

name = input("Whose birthday is it?: ")

happybirthday(name)


