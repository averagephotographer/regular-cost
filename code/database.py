# database interactions
import csv

# fn. retrieving data from .csv
    # input: shop name
    # output: none
csv_file = "example_input.csv"
fields = []
rows = []

with open(csv_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)
    
    print("Total no. of rows: %d"%(csvreader.line_num))

# print('Field names are:' + ', '.join(field for field in fields))

print(f"{fields=}")
print(f"{rows=}")

# fn. adding new shops
    # input: name, cost
    # output: none

# fn. updating entries (prices, names, ?)
    # input: name, (optional new name), (optional new cost)
    # output: new information, allowing user to confirm the new data is correct

