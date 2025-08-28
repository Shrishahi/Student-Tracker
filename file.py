import csv
with open('StudentDetails.csv', mode='a', newline='') as file:
        fieldnames = ['id', 'name', 'age']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
