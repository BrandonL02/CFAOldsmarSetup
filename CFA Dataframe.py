
import pandas as pd

import time

from selenium import webdriver

from selenium.webdriver.common.by import By


#Access Hotschedules with credentials and navigate pages

username = '2445922'

password = 'Monkey2002'

url = "https://www.hotschedules.com/hs/login.jsp"

driver = webdriver.Chrome(executable_path=r'C:/Users/Brand\Desktop/chromedriver.exe')

driver.get(url)

driver.find_element(By.NAME,'username').send_keys(username)

driver.find_element(By.NAME,'password').send_keys(password)

driver.find_elements(By.ID,"loginBtn")[0].click()

time.sleep(2) #Wait for login

driver.find_element(By.CLASS_NAME,"go-to-other-pages-buttons").click()

driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[2]/div[@class='schedule-item-container']/div[@class='schedule-item']").click()

Info = driver.find_element(By.CLASS_NAME, "schedule-table")

Data = Info.get_attribute('innerHTML')


All_shifts = []



time.sleep(2) #Let page load

emp = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[2]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][1]")

#Get employee hours from HS table & Save to All_shifts list

R1_Columns = 1

while R1_Columns != 54:
   for A in range (2,8):
        if (R1_Columns == 1):
            Row_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[2]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][" + str (R1_Columns) + "]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift']["  + str (A) + "]")
        elif (R1_Columns % 2 == 0):
            Row_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[2]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][" + str (R1_Columns) + "]/div[@class='days-row']/div[@class='schedule-table-cell scheduled-shift']["  + str (A) + "]")
        elif (R1_Columns != 53):
            Row_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[2]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][" + str (R1_Columns) + "]/div[@class='days-row grayed']/div[@class='schedule-table-cell scheduled-shift']["  + str (A) + "]")                                 
        else:
            Row_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[2]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][" + str (R1_Columns) + "]/div[@class='days-row grayed border-bottom']/div[@class='schedule-table-cell scheduled-shift']["  + str (A) + "]")
        R1_shifts = (Row_data.text)
        R1_shifts = R1_shifts.replace("FOH General\n", "")
        All_shifts.append(R1_shifts)
   R1_Columns += 1


full_schedule = {}


days = dict({'Monday' : 'x', 'Tuesday' : 'x' , 'Wednesday' : 'x' , 'Thursday' : 'x' , 'Friday' : 'x' , 'Saturday' : 'x'})

#Get employee names from HS

for x in range (1,54):
   x = str (x)
   emp = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[2]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][" + x + "]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
   employee_id = emp.text
   full_schedule.update({employee_id : days})

#Create dataframe to display employee names and hours

df = pd.DataFrame(full_schedule).T


#Replace letter x in dataframe with all the scheduled shifts

A = 0
B = 1
staff = 0

for p in range (0,53):
    nav = 0
    y = 1 
    for t in df.iloc[A:B]:
        df.iloc[A:B, nav:y] = All_shifts[staff]
        if nav == 6:
            nav == 0
            y == 1
            staff += 1
        else:
            nav += 1
            y += 1
            staff +=1
    A += 1
    B += 1


#Display full dataframe

pd.set_option('display.max_columns', None)
print(df) 


driver.close()

