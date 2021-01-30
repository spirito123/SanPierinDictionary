import csv

f = open('/Users/cdelbasso/Desktop/SPD4FX.csv', 'r')

reader = csv.reader(f)

spd = {}

for row in reader:
    spd[row[0]] = {'Italian':row[1], 'Croatian':row[2], 'English':row[3]}
