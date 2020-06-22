from datetime import datetime

# def parse_date(value, *, default=None):
#     date_format='%m/%d/%Y'
#     try:
#         return datetime.strptime(value, date_format).date()
#     except ValueError:
#         return default

# *************************************************************
# def parse_time(value, *, default=None):
#     time_format='%H:%M'
#     try:
#         return datetime.strptime(value, '%H:%M')
#     except ValueError:
#         return default

# print(parse_time('12:00'))
# *************************************************************

# catch another function return
# def catch(fn):
#     def inner(*args,**kwargs):
#         g = fn(*args,kwargs)
#         print(g)
#     return inner

# **********************************************

# def csv_parser(fname, *, delimiter=',', quotechar='"', include_header=True):
#     with open(fname)as f:
#         reader = csv.reader(f, delimiter=delimiter, quotechar=quotechar)
#         if include_header:
#             next(f)
#         yield from reader

# csv_parser('2.csv')

# 
# **************************************************************
# make some beauty to saved data
# import csv

# txt_file = r"worktime_records.csv"
# csv_file = r"2.csv"

# with open(txt_file, "r") as in_text:
#     in_reader = csv.reader(in_text, delimiter = '\t')
#     with open(csv_file, "w") as out_csv:
#         out_writer = csv.writer(out_csv)
#         for row in in_reader:
#             out_writer.writerow(row)

# ******************************************************************
