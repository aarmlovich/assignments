# Read vegetable.csv
import csv
import json
from pprint import pprint
#read csv
with open('veggies.csv', 'r') as f:
	reader = csv.DictReader(f)
	veggies = list(reader)



#Group by color
veggies_by_color = {}
for veggie in veggies:
    color = veggie['color']
    if color in veggies_by_color:
        veggies_by_color[color].append(veggie)
    else:
       	veggies_by_color[color] = [veggie]


#Print to terminal
pprint(veggies_by_color)

#Output to JSON
with open('veggiesbycolor.json', 'w') as f:
    json.dump(veggies_by_color, f)

