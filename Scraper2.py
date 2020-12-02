import csv 

data = []
with open('Scarperwed.csv' , 'r') as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        data.append(row)
headers = data[0]
planetdata = data[1:]
for datapoint in planetdata:
    datapoint[2] = datapoint[2].lower()
planetdata.sort(key= lambda planetdata : planetdata[2]) 
with open('SortedList.csv' , 'a+') as f:
    csvwriter = csv.writer(f) 
    csvwriter.writerow(headers)
    csvwriter.writerows(planetdata)
