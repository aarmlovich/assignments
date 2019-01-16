import csv
import json
#read csv
with open('veggies.csv', 'r') as f:
	reader = csv.DictReader(f)
	veggies = list(reader)


# filter whitelist names


green_veggies = []
whitelist = ['green']
for veggie in veggies:
	if veggie['color'] in whitelist:
		veggies.append(veggie)


# write to JSON
with open('greenvegetables.json', 'w') as f:
	json.dump(green_veggies, f, indent=2)
