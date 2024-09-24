import csv

with open("rian.csv") as csvfile:
    read = csv.reader(csvfile)
    for i in read:
        print(i)
        