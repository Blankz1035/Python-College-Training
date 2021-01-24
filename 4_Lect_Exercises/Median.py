# Program to demonstrate the use of mean, medium and average

firstlist = [1,3,3,6,7,8,9]
secondlist = [1,2,3,4,5,6,8,9]

print(f"Number of values in first list {len(firstlist)} and second list {len(secondlist)} ")


mid_indexFL = int(len(firstlist)/2)
print("First list mid point: ", mid_indexFL)

print()

mid_indexSL = int(len(secondlist)/2)
print("Second list mid point: ", mid_indexSL)
print()

if len(firstlist) % 2 == 1:
    medianfl = firstlist[mid_indexFL]
else:
    medianfl = (firstlist[mid_indexFL -1] + firstlist[mid_indexFL]) / 2

print("Median value for FL: ", medianfl)
print()

if len(secondlist) % 2 == 1:
    mediansl = secondlist[mid_indexSL]
else:
    mediansl = (secondlist[mid_indexSL -1] + secondlist[mid_indexSL]) / 2

    
print("Median value for SL: ", mediansl)
print()
