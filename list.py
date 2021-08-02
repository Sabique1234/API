import csv

finaldict = {}

with open('venv/gravity.csv', mode = 'r') as f:
    reader = csv.reader(f)
    dict_from_csv = {rows[0]:rows[1] for rows in reader}
print(dict_from_csv)

""" with open("format.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(reader)
    csvwriter.writerows(dict_from_csv)"""