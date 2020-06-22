import unittest


# class MySoftware(unittest.TestCase):

#     def inputs(machineID=None,workTime=None,Date=None,start_time_inp=None,end_time_inp=None):

#         validmachineID = False
#         while not validmachineID:
#             machineID = (input('Enter the Machine Id '))
#             if machineID.isalnum() and len(machineID)>5:
#                 validmachineID = True
#             else:
#                 print('Your machine id is not valid')
#         print('your machine id : ',machineID)

#         if Date is None:
#             Date = datetime.now().strftime("%Y-%m-%d")
#             print(f'Machine and Date {machineID} : {Date}')

#         while True:
#             start_time_inp = (input("Enter the startime xx:xx : "))
#             end_time_inp = (input("Enter the endtime xx:xx : "))
#             try:
#                 date_time_obj = datetime.strptime(start_time_inp, '%H:%M')
#                 end_time_obj = datetime.strptime(end_time_inp, '%H:%M')
#                 workTime = end_time_obj-date_time_obj
#                 if workTime.days < 0:
#                     workTime = timedelta(days=0,
#                                         seconds=workTime.seconds,
#                                         microseconds=workTime.microseconds)
                    
#                     print(f'system Total working Hours {workTime} ')
#                     print(type(workTime))
                    
#                     # workTime = workTime
#                     break
#                 else:
#                     workTime = end_time_obj-date_time_obj
#                     print(f'system Total working Hours {workTime} ')
#                     workTime = (f'{workTime}')
#                     # workTime = tdelta                 
#                     break
#             except ValueError:
#                 print('value is not valid')
                
#         return (machineID,workTime,Date,start_time_inp,end_time_inp)


    # def catch(fn):
    #     def inner(*args,**kwargs):
    #         g = fn(*args,kwargs)
    #         rows=[]
    #         rows = g
    #         # name of csv file  
    #         filename = "worktime_records.csv"
    #         header_util(filename)
    #         with open(filename, 'a+') as csvfile:
    #             csvwriter = csv.writer(csvfile)  
    #             csvwriter.writerow(rows)
    #             csvfile.close()
    
    # def header_util(f_name):
    #     with open(f_name) as f:
    #         column_headers = next(f).strip('\n').split(',')
    #         print('Data stored to server')
    #     return f_name


    # def searching(*args,**kwargs):
    #     filename = "worktime_records.csv"
    #     dob = input('Input to check the Status Format (YYYY-MM-DD): ')
    #     date_time_obj = datetime.strptime(dob,'%Y-%m-%d')

    #     with open(filename, newline='') as myfile:
    #         column_headers = next(myfile).strip('\n').split(',')
    #         print(column_headers)
    #         reader = csv.reader(myfile)
    #         for row in reader:
    #             if dob in row:
    #                 print(row)
    #         return row


    # def duplicate_solver():
    #     filename = 'worktime_records.csv'
    #     inFile = open(filename,'r')
    #     outFile = open('2.csv','w')
    #     listLines = []
    #     for line in inFile:
    #         for x in inFile:
    #             if line in x:
    #                 continue 
    #             else:
    #                 outFile.write(line)
    #                 listLines.append(line)
    #                 break
    #     outFile.close()
    #     inFile.close()

if __name__ == '__main__':
    unittest.main()
