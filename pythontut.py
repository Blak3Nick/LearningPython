from csv import reader
import datetime as dt
with open('potus_visitors_2015.csv') as csv_file:
    csv_reader = reader(csv_file)
    potus = list(csv_reader)
    potus = potus[1:]
    print(potus[2])
    date_format = "%m/%d/%y %H:%M"
    for row in potus:
        date = row[2]
        date = dt.datetime.strptime(date, date_format)
        row[2] = date