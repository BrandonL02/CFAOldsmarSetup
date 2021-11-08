import random
#Pull employee number from CFA_Employees.py
from CFA_Employees import Employee_num
#Returm employee number to name 
from CFA_Employees import Employee_name
#Pull employees ability on positions
from Employee_Ability import employee_ability
#Pull time conversion from Time_conversion.py
from Time_conversion import converted_time
#Prompt user to enter scheduled employee quantity 
employee_count = int(input('How many employees are scheduled between 2 pm and 10:45 pm? '))
#Print scheduled employee quantity
print(employee_count)
#Prompt user to enter employee names and shifts in format: FirstName LastName.StartTime.Endtime 
print("Please enter who is scheduled to work tonight along with their start and end times (in military time) separated by '.'")
#Define Lists
employee_and_shift = []
employee_list = []
start_shift_list = []
end_shift_list = []
shift_length = []
time_2to3 = []
time_3to4 = []
time_4to5 = []
time_5to6 = []
time_6to7 = []
time_7to8 = []
time_8to9 = []
time_9to10 = []
#Create list of scheduled employees and their shifts by repeating as many times as there are sheduled employees
for i in range(0,employee_count):
    scheduled_shift = input()
    employee, start_shift, end_shift = (scheduled_shift.split('.',3))
    #Replace provided employee name with their given number
    if employee in Employee_num:
        employee = Employee_num[employee]    
    employee_list.append (employee)
    #Calculate shift length
    if (int(end_shift) - int(start_shift)) > 0:
        shift_length.append (int(end_shift) - int(start_shift))
    else:
        shift_length.append ((12 - int(start_shift)) + int(end_shift))
    if (int (end_shift) > 14 and int(start_shift) <= 14):  
        time_2to3.append(employee)
    if (int (end_shift) > 15 and int(start_shift) <= 15):  
        time_3to4.append(employee) 
    if (int (end_shift) > 16 and int(start_shift) <= 16):  
        time_4to5.append(employee)
    if (int (end_shift) > 17 and int(start_shift) <= 17):  
        time_5to6.append(employee)
    if (int (end_shift) > 18 and int(start_shift) <= 18):  
        time_6to7.append(employee)
    if (int (end_shift) > 19 and int(start_shift) <= 19):  
        time_7to8.append(employee)
    if (int (end_shift) > 20 and int(start_shift) <= 20):  
        time_8to9.append(employee)
    if (int (end_shift) > 21 and int(start_shift) <= 21):  
        time_9to10.append(employee)       
    start_shift_list.append (start_shift)
    end_shift_list.append (end_shift)
    employee_and_shift.append(scheduled_shift)
#Convert all lists of strings to integers
employee_list = list(map(int,employee_list))    
start_shift_list= list(map(int,start_shift_list))
end_shift_list = list(map(int,end_shift_list))

#Breaks

  #Find who works 2-3 
print(shift_length)
print(time_2to3)
print(time_3to4)

#2-3
print ("2 to 3")
for x in time_2to3:
#Window    
    pos_window2to3 = random.choice(time_2to3)
    if pos_window2to3 in Employee_name:
       window2to3 = Employee_name[pos_window2to3]
    time_2to3.remove(pos_window2to3)
#DT bagging    
    pos_DTbag2to3 = random.choice(time_2to3)
    if pos_DTbag2to3 in Employee_name:
       DTbag2to3 = Employee_name[pos_DTbag2to3]
    time_2to3.remove(pos_DTbag2to3)
#Drinks

#IPad

#Cash


    
print((window2to3) + " on window")
print((DTbag2to3) + "on DT bagging")



    