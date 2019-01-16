import csv

#read csv
with open('veggies.csv', 'r') as f:
	reader = csv.DictReader(f)
	veggies = list(reader)


# filter whitelist names


green_veggies = []
whitelist = ['green']
for veggie in veggies:
	if veggie['color'] in whitelist:

		print(veggie)