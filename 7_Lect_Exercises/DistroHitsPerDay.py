# Program to demonstrate use of dictionaries.  Capturing web stie 

# Write a program which uses a loop to input the names and hits per day of a number of Linux
# distributions and insert them into a dictionary as key-value pairs (the name is the key and the hits
# per day is the value).

# After the values have been added to the dictionary, the program should sort it in alphabetical order
# and display its contents, and then determine and display the distribution with the maximum hits per
# day.
# Hint:
# Given a dictionary called data_dict
# the maximum value is max(data_dict.values())
# and the key associated with the maximum value is
# max(data_dict,key=data_dict.get)

print()
print("Enter 10 best days for web hits and distributions. \n")

web_hits = {}

while True:

    distribution = input("\nEnter distribution name: ")
    hits =  int(input("Enter number of hits for distribution: "))

    if distribution and hits:
        # if both variables contain data, then proceed
        web_hits[distribution] = hits

    else:
        print("Data not entered correctly.")

    if len(web_hits) == 10:
        break

# After data has been entered, now we want to proceed with output.

# Sort contents of the dictionary
print(f"\nNumber of hits entere: {len(web_hits)}\n")
print("Top 10 distributions")

for hit in sorted(web_hits.keys()):
    print(f"{hit}   :   {web_hits[hit]}")

print(f"Most popular distribution: {max(web_hits, key=web_hits.get)} with {max(web_hits.values())}")