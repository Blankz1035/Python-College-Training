# Program to demonstrate dictionaries for csv file.

def get_data():

    with open("8_Lect_Exercises/trolleywatch.csv") as csv_in:

    # remove first line
        csv_in.readline()

        data = csv_in.readlines()

    # Hospital,Region,Trolley,Ward,Patients
        bitsFreq = {}
        hospitals = {}

        for line in data:

            d, h, r, t, w, p = line.split(",")

            if d not in bitsFreq.keys():
                bitsFreq[d] = int(p)
            else:
                bitsFreq[d] =  bitsFreq[d] + int(p)

            if h not in hospitals.keys():
                hospitals[h] = int(p)
            else:
                hospitals[h] =  hospitals[h] + int(p)


    return bitsFreq, hospitals


abc, xyz = get_data()


print(abc)
print(xyz)




