import json
import csv

#read superheroes json
with open('superheroes.json', 'r') as f:
    superheroes = json.load(f)


#save data for each member into a csv row


with open('members.csv', 'w') as f:
    writer = csv.writer(f)
    #header
    header = ['name', 'age', 'secretIdentity', 'powers', 'squadName' 'homeTown', 'formed', 'secretBase', 'active']
    writer.writerow(header)
    writer.writerow(['col1', 'col2'])
    writer.writerow(['val1', 'val2'])
    writer.writerow(['val1', 'val2'])
    writer.writerow(['val1', 'val2'])

    # looop thru each member
members = superheroes['members']
for member in members:
	row = [member
	]