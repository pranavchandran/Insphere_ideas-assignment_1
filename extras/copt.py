import datetime
import time
from dateandtime import time_diff

def inputs(machineID=None,workTime=None,Date=None,starttime=None,endtime=None):

    validmachineID = False
    while not validmachineID:
        machineID = (input('Enter the Machine Id '))
        if machineID.isalnum() and len(machineID)>5:
            validmachineID = True
        else:
            print('Your machine id is not valid')
    print('your machine id : ',machineID)

    if Date is None:
        Date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f'Machine and Date {machineID} : {Date}')

        def time_diff(inputs):
            return starttime,endtime,workTime

    

    

inputs()
time_diff(inputs)



