import requests

import pandas as pd

import time

import re

from bs4 import BeautifulSoup


from selenium import webdriver

from selenium.webdriver.common.by import By

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



#Row 1 



R1_Columns = 1
for A in range (0,7):
    R1_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[2]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][1]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R1_Columns) + "]")
    R1_shifts = (R1_data.text)
    R1_shifts = R1_shifts.replace("FOH General\n", "")
    All_shifts.append(R1_shifts)
    R1_Columns += 1

#print(All_shifts)


full_schedule = {}
days = dict({'Sunday' : 'x' , 'Monday' : 'x', 'Tuesday' : 'x' , 'Wednesday' : 'x' , 'Thursday' : 'x' , 'Friday' : 'x' , 'Saturday' : 'x'})
x = 1
for x in range (1,57):
   emp = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[2]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][" + str(x) + "]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
   employee_id = emp.text
   full_schedule.update({employee_id : days})
   x +=1
   
df = pd.DataFrame(full_schedule).T

print (df.iloc[1:3 , : ])
#print (df)   

driver.close()