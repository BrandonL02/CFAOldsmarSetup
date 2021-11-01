#Pull employee number from CFA_Employees.py
from CFA_Employees import Employee_num
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
    start_shift_list.append (start_shift)
    end_shift_list.append (end_shift)
    employee_and_shift.append(scheduled_shift)

#Convert all lists of strings to integers
employee_list = list(map(int,employee_list))    
start_shift_list= list(map(int,start_shift_list))
end_shift_list = list(map(int,end_shift_list))

#Breaks

  #Find who works 2-3 
if int(start_shift) <= 14:
    if int(end_shift) >= 15:
      time_2to3.extend(employee_list) 
    else:
        {}
else:
      {}
     
if int(start_shift) <= 15:
      if int(end_shift) >= 16:
          time_3to4.extend(employee_list)
      else:
          {}
else:
      {}       
if int(start_shift) <= 16:
      if (int(end_shift) >= 17):
          time_4to5.extend(employee_list)
      else:
          []
else:
      {}     
  #elif ((int(start_shift)) <= 17) and ((int(end_shift)) >= 18):
      #time_5to6.append (employee_list)
  #elif ((int(start_shift)) <= 18) and ((int(end_shift)) >= 19):
      #time_6to7.append (employee_list)
  #elif ((int(start_shift)) <= 19) and ((int(end_shift)) >= 20):
     # time_7to8.append (employee_list)
  #elif ((int(start_shift)) <= 20) and ((int(end_shift)) >= 21):
    #  time_8to9.append (employee_list)
  #elif ((int(start_shift)) <= 21) and ((int(end_shift)) >= 22):
   #   time_9to10.append (employee_list)
  #elif ((int(start_shift)) <= 22) and ((int(end_shift)) >= 23): 

#2-2:59 #input military but convert prior to output
print (time_2to3)
print (time_3to4)
print (time_4to5)
print (time_5to6)
print (time_6to7)
print (time_7to8)
print (time_8to9)
print (time_9to10)

    