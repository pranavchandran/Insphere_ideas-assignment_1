# create a search form by date 
import csv
import pprint
from datetime import datetime


def searching(*args,**kwargs):
    filename = "worktime_records.csv"
    dob = input('Search by date in this Format (YYYY-MM-DD): ')
    date_time_obj = datetime.strptime(dob,'%Y-%m-%d')

    with open(filename, newline='') as myfile:
        column_headers = next(myfile).strip('\n').split(',')
        print(column_headers)
        reader = csv.reader(myfile)
        for row in reader:
            if dob in row:
                print(row)
        return row
# searching()







        # print(dob)
    #     # row_date, row_month, row_year = row[6].split("/")
    #     if row_month == month:
    #         print(row) # or whatever you want to print..
