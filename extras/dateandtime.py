import datetime
# from copt import inputs
# def time_diff(*args,**kwargs):
#     while True:
#         start_time_inp = (input("Enter the startime xx:xx : "))
#         end_time_inp = (input("Enter the endtime xx:xx : "))
#         try:
#             date_time_obj = datetime.datetime.strptime(start_time_inp, '%H:%M')
#             end_time_obj = datetime.datetime.strptime(end_time_inp, '%H:%M')
#             if date_time_obj == date_time_obj and end_time_obj==end_time_obj:
#                 print('Start Time :', date_time_obj.time())
#                 print('End Time :', end_time_obj.time())
#                 res = end_time_obj-date_time_obj
#                 print('minutes :',res.total_seconds()/60)
#                 print('hours :',res.total_seconds()/60**2)
#                 break
#             else:
#                 print('wrong')
#         except ValueError:
#             print('value is not valid')

# time_diff()

"""All errors solved First i have an issue of time difference Calculation"""
from datetime import timedelta
from datetime import datetime

def time_diff(fn,*args,**kwargs):
    while True:
        start_time_inp = (input("Enter the startime xx:xx : "))
        end_time_inp = (input("Enter the endtime xx:xx : "))
        try:
            date_time_obj = datetime.strptime(start_time_inp, '%H:%M')
            end_time_obj = datetime.strptime(end_time_inp, '%H:%M')
            tdelta = end_time_obj-date_time_obj
            if tdelta.days < 0:
                tdelta = timedelta(days=0,
                                    seconds=tdelta.seconds,
                                    microseconds=tdelta.microseconds)
                print(f'{tdelta} Hours')
                break
            else:
                tdelta = end_time_obj-date_time_obj
                print(f'{tdelta} Hours')
                
                break
        except ValueError:
            print('value is not valid')
# time_diff()

