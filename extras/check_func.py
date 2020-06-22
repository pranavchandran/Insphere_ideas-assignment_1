
# import datetime


# start_time_inp = (input("Enter the startime xx:xx"))
# end_time_inp = (input("Enter the endtime xx:xx"))
# date_time_obj = datetime.datetime.strptime(start_time_inp, '%H:%M')
# print(type(date_time_obj))
# end_time_obj = datetime.datetime.strptime(end_time_inp, '%H:%M')
# res = end_time_obj-date_time_obj
# print('minutes',res.total_seconds()/60)
# print('hours',res.total_seconds()/60**2)

# ***************************************************************
# while True:

#     start_time_inp = (input("Enter the startime xx:xx"))
#     try:

#         date_time_obj = datetime.datetime.strptime(start_time_inp, '%H:%M')
#         date_time_obj.strftime("%i:%M")
#         print(date_time_obj("%i:%M"%p))
        

    #     if date_time_obj == date_time_obj:
    #         print('Time:', date_time_obj.time())
    #         break
    #     else:
    #         print('wrong')
# *********************************************************
    # except ValueError:
    #     print('value is not valid')

        # if date_time_obj == date_time_obj.time():


        #     print('Time:', date_time_obj.time())
        # else:
        #     print('wrong')

# start_time_inp = (input("Enter the startime xx:xx"))
# end_time_inp = (input("Enter the endtime xx:xx"))
# date_time_obj = datetime.datetime.strptime(start_time_inp, '%H:%M')
# end_time_obj = datetime.datetime.strptime(end_time_inp, '%H:%M')
# res = end_time_obj-date_time_obj
# print('minutes',res.total_seconds()/60)
# print('hours',res.total_seconds()/60**2)


from datetime import timedelta
from datetime import datetime

while True:
    start_time_inp = (input("Enter the startime xx:xx : "))
    end_time_inp = (input("Enter the endtime xx:xx : "))
    try:
        date_time_obj = datetime.strptime(start_time_inp, '%H:%M')
        end_time_obj = datetime.strptime(end_time_inp, '%H:%M')
        if tdelta.days < 0:
            tdelta = timedelta(days=0,
                                seconds=tdelta.seconds,
                                microseconds=tdelta.microseconds)
            print(tdelta)
            break
        else:
            tdelta = end_time_obj-date_time_obj
            print(tdelta)
            break
    except ValueError:
        print('value is not valid')


        # if tdelta.days < 0:
        #     tdelta = timedelta(days=0,
        #                         seconds=tdelta.seconds,
        #                         microseconds=tdelta.microseconds)

        # if date_time_obj == date_time_obj and end_time_obj==end_time_obj:
        #     print('Start Time :', date_time_obj.time())
        #     print('End Time :', end_time_obj.time())
        #     res = end_time_obj-date_time_obj
        #     print('Difference :',res)
        #     break

        #         print('minutes :',res.total_seconds()/60)
        #         print('hours :',res.total_seconds()/60**2)
    #             print(tdelta)
    #             break
    #         else:
    #             print('wrong')
    # except ValueError:
    #     print('value is not valid')