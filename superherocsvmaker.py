import json

#read superheroes json
with open('superheroes.json', 'r') as f:
	superheroes = json.load(f)


#save data for each member into a csv row
import csv

with open('superheroes.csv', 'w') as f:
	writer = csv.writer(f)
	#write headers
	header = ['name', 'age', 'secretIdentity', 'powers', 'squadName' 'homeTown', 'formed', 'secretBase', 'active']
	writer.writerow(header)

	# loop over members
	members = superheroes['members']
	for member in members:
		#define variables
		name = member['name']
		age = member['age']
		secretIdentity = member['secretIdentity']
		powers = member['powers']
		squadName = superheroes['squadName']
		homeTown = superheroes['homeTown']
		formed = superheroes['formed']
		secretBase = superheroes['secretBase']
		active = superheroes['active']
#write data to csv
		row = [name, age, secretIdentity, powers, squadName, homeTown, formed, secretBase, active]

		writer.writerow(row)

