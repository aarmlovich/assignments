
import csv
import json

# read veggies.csv into a variable

with open('veggies.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = list(reader)


#save "vegetables" as vegetables.json

with open('cookedveggies.json', 'w') as f:
    json.dump(vegetables, f, indent=2)