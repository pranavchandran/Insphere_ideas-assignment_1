import time
from datetime import timedelta
from datetime import datetime

def parse_date(value, *, default=None):
    date_format='%m/%d/%Y'
    try:
        return datetime.strptime(value, date_format).date()
    except ValueError:
        return default

def inputs(machineID=None,workTime=None,Date=None,start_time_inp=None,end_time_inp=None):

    validmachineID = False
    while not validmachineID:
        machineID = (input('Enter the Machine Id '))
        if machineID.isalnum() and len(machineID)>5:
            validmachineID = True
        else:
            print('Your machine id is not valid')
    print('your machine id : ',machineID)

    if Date is None:
        Date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f'Machine and Date {machineID} : {Date}')

    while True:
        start_time_inp = (input("Enter the startime xx:xx : "))
        end_time_inp = (input("Enter the endtime xx:xx : "))
        try:
            date_time_obj = datetime.strptime(start_time_inp, '%H:%M')
            end_time_obj = datetime.strptime(end_time_inp, '%H:%M')
            workTime = end_time_obj-date_time_obj
            if workTime.days < 0:
                workTime = timedelta(days=0,
                                    seconds=workTime.seconds,
                                    microseconds=workTime.microseconds)
                
                print(f'system Total working Hours {workTime} ')
                print(type(workTime))
                
                # workTime = workTime
                break
            else:
                workTime = end_time_obj-date_time_obj
                print(f'system Total working Hours {workTime} ')
                workTime = (f'{workTime}')
                # workTime = tdelta                 
                break
        except ValueError:
            print('value is not valid')
    return (machineID,workTime,Date,start_time_inp,end_time_inp)
print(inputs())




