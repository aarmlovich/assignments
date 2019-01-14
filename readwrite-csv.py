import csv

#write a CSV file

# with open('testwrite.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow(['col1', 'col2'])
#     writer.writerow(['val1', 'val2'])
#     writer.writerow(['val1', 'val2'])
#     writer.writerow(['val1', 'val2'])

#  #read from a csv

#  with open('testwrite.csv', 'r') as f:
#     reader = csv.DictReader(f)
#     rows = list(reader)

# for row in rows:
#     print(row)

vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]

#open a csv file
with open('veggies.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['name', 'color', 'length'])
#loop through veggies
	for vegetable in vegetables:
	#write each veggie to a CSV
		name = vegetable['name']
		color = vegetable['color']
		length_of_veggie = len(name)

		row = [name, color, length_of_veggie]

		writer.writerow(row)



