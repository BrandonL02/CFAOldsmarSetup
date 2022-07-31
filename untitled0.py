Row_2 = []
Row_3 = []
Row_4 = []
Row_5 = []
Row_6 = []
Row_7 = []
Row_8 = []
Row_9 = []
Row_10 = []
Row_11 = []
Row_12 = []
Row_13 = []
Row_14 = []
Row_15 = []
Row_16 = []
Row_17 = []
Row_18 = []
Row_19 = []
Row_20 = []
Row_21 = []
Row_22 = []
Row_23 = []
Row_24 = []
Row_25 = []
Row_26 = []
Row_27 = []
Row_28 = []
Row_29 = []
Row_30 = []
Row_31 = []
Row_32 = []
Row_33 = []
Row_34 = []
Row_35 = []
Row_36 = []
Row_37 = []
Row_38 = []
Row_39 = []
Row_40 = []
Row_41 = []
Row_42 = []
Row_43 = []
Row_44 = []
Row_45 = []
Row_46 = []
Row_47 = []
Row_48 = []
Row_49 = []
Row_50 = []
Row_51 = []
Row_52 = []
Row_53 = []
Row_54 = []
Row_55 = []
Row_56 = []

#Row 2 
emp2 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[2]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][2]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp2_name = emp2.text
Row_2.append(emp2_name)

R2_Columns = 1
for A in range (0,7):
    R2_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[2]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][2]/div[@class='days-row']/div[@class='schedule-table-cell scheduled-shift'][" + str (R2_Columns) + "]")
    R2_shifts = (R2_data.text)
    R2_shifts = R2_shifts.replace("FOH General\n", "")
    Row_2.append(R2_shifts)
    R2_Columns += 1   
    
print = (Row_1)
print = (Row_2)    
   
#Row 3 
emp3 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[3]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][3]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp3_name = emp3.text
Row_3.append(emp3_name)

R3_Columns = 1
for A in range (0,7):
    R3_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[3]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][3]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R3_Columns) + "]")
    R3_shifts = (R3_data.text)
    R3_shifts = R3_shifts.replace("FOH General\n", "")
    Row_3.append(R3_shifts)
    R3_Columns += 1  

#Row 4 
emp4 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[4]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][4]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp4_name = emp4.text
Row_4.append(emp4_name)

R4_Columns = 1
for A in range (0,7):
    R4_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[4]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][4]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R4_Columns) + "]")
    R4_shifts = (R4_data.text)
    R4_shifts = R4_shifts.replace("FOH General\n", "")
    Row_4.append(R4_shifts)
    R4_Columns += 1  

#Row 5 
emp5 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[5]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][5]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp5_name = emp5.text
Row_5.append(emp5_name)

R5_Columns = 1
for A in range (0,7):
    R5_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[5]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][5]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R5_Columns) + "]")
    R5_shifts = (R5_data.text)
    R5_shifts = R5_shifts.replace("FOH General\n", "")
    Row_5.append(R5_shifts)
    R5_Columns += 1  

#Row 6 
emp6 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[6]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][6]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp6_name = emp6.text
Row_6.append(emp6_name)

R6_Columns = 1
for A in range (0,7):
    R6_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[6]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][6]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R6_Columns) + "]")
    R6_shifts = (R6_data.text)
    R6_shifts = R6_shifts.replace("FOH General\n", "")
    Row_6.append(R6_shifts)
    R6_Columns += 1  

#Row 7 
emp7 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[7]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][7]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp7_name = emp7.text
Row_7.append(emp7_name)

R7_Columns = 1
for A in range (0,7):
    R7_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[7]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][7]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R7_Columns) + "]")
    R7_shifts = (R7_data.text)
    R7_shifts = R7_shifts.replace("FOH General\n", "")
    Row_7.append(R7_shifts)
    R7_Columns += 1  
    
#Row 8 
emp8 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[8]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][8]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp8_name = emp8.text
Row_8.append(emp8_name)

R8_Columns = 1
for A in range (0,7):
    R8_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[8]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][8]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R8_Columns) + "]")
    R8_shifts = (R8_data.text)
    R8_shifts = R8_shifts.replace("FOH General\n", "")
    Row_8.append(R8_shifts)
    R8_Columns += 1      

#Row 9 
emp9 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[9]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][9]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp9_name = emp9.text
Row_9.append(emp9_name)

R9_Columns = 1
for A in range (0,7):
    R9_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[9]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][9]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R9_Columns) + "]")
    R9_shifts = (R9_data.text)
    R9_shifts = R9_shifts.replace("FOH General\n", "")
    Row_9.append(R9_shifts)
    R9_Columns += 1 
    
#Row 10 
emp10 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[10]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][10]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp10_name = emp10.text
Row_10.append(emp10_name)

R10_Columns = 1
for A in range (0,7):
    R10_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[10]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][10]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R10_Columns) + "]")
    R10_shifts = (R10_data.text)
    R10_shifts = R10_shifts.replace("FOH General\n", "")
    Row_10.append(R10_shifts)
    R10_Columns += 1     
   
#Row 11 
emp11 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[11]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][11]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp11_name = emp11.text
Row_11.append(emp11_name)

R11_Columns = 1
for A in range (0,7):
    R11_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[11]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][11]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R11_Columns) + "]")
    R11_shifts = (R11_data.text)
    R11_shifts = R11_shifts.replace("FOH General\n", "")
    Row_11.append(R11_shifts)
    R11_Columns += 1     

#Row 12 
emp12 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[12]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][12]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp12_name = emp12.text
Row_12.append(emp12_name)

R12_Columns = 1
for A in range (0,7):
    R12_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[12]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][12]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R12_Columns) + "]")
    R12_shifts = (R12_data.text)
    R12_shifts = R12_shifts.replace("FOH General\n", "")
    Row_12.append(R12_shifts)
    R12_Columns += 1 

#Row 13 
emp13 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[13]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][13]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp13_name = emp13.text
Row_13.append(emp13_name)

R13_Columns = 1
for A in range (0,7):
    R13_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[13]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][13]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R13_Columns) + "]")
    R13_shifts = (R13_data.text)
    R13_shifts = R13_shifts.replace("FOH General\n", "")
    Row_13.append(R13_shifts)
    R13_Columns += 1 

#Row 14 
emp14 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[14]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][14]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp14_name = emp14.text
Row_14.append(emp14_name)

R14_Columns = 1
for A in range (0,7):
    R14_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[14]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][14]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R14_Columns) + "]")
    R14_shifts = (R14_data.text)
    R14_shifts = R14_shifts.replace("FOH General\n", "")
    Row_14.append(R14_shifts)
    R14_Columns += 1 

#Row 15 
emp15 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[15]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][15]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp15_name = emp15.text
Row_15.append(emp15_name)

R15_Columns = 1
for A in range (0,7):
    R15_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[15]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][15]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R15_Columns) + "]")
    R15_shifts = (R15_data.text)
    R15_shifts = R15_shifts.replace("FOH General\n", "")
    Row_15.append(R15_shifts)
    R15_Columns += 1 

#Row 16 
emp16 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[16]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][16]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp16_name = emp16.text
Row_16.append(emp16_name)

R16_Columns = 1
for A in range (0,7):
    R16_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[16]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][16]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R16_Columns) + "]")
    R16_shifts = (R16_data.text)
    R16_shifts = R16_shifts.replace("FOH General\n", "")
    Row_16.append(R16_shifts)
    R16_Columns += 1 

#Row 17 
emp17 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[17]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][17]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp17_name = emp17.text
Row_17.append(emp17_name)

R17_Columns = 1
for A in range (0,7):
    R17_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[17]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][17]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R17_Columns) + "]")
    R17_shifts = (R17_data.text)
    R17_shifts = R17_shifts.replace("FOH General\n", "")
    Row_17.append(R17_shifts)
    R17_Columns += 1 

#Row 18 
emp18 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[18]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][18]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp18_name = emp18.text
Row_18.append(emp18_name)

R18_Columns = 1
for A in range (0,7):
    R18_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[18]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][18]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R18_Columns) + "]")
    R18_shifts = (R18_data.text)
    R18_shifts = R18_shifts.replace("FOH General\n", "")
    Row_18.append(R18_shifts)
    R18_Columns += 1 

#Row 19 
emp19 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[19]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][19]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp19_name = emp19.text
Row_19.append(emp19_name)

R19_Columns = 1
for A in range (0,7):
    R19_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[19]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][19]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R19_Columns) + "]")
    R19_shifts = (R19_data.text)
    R19_shifts = R19_shifts.replace("FOH General\n", "")
    Row_19.append(R19_shifts)
    R19_Columns += 1 

#Row 20 
emp20 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[20]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][20]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp20_name = emp20.text
Row_20.append(emp20_name)

R20_Columns = 1
for A in range (0,7):
    R20_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[20]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][20]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R20_Columns) + "]")
    R20_shifts = (R20_data.text)
    R20_shifts = R20_shifts.replace("FOH General\n", "")
    Row_20.append(R20_shifts)
    R20_Columns += 1 

#Row 21 
emp21 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[21]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][21]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp21_name = emp21.text
Row_21.append(emp21_name)

R21_Columns = 1
for A in range (0,7):
    R21_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[21]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][21]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R21_Columns) + "]")
    R21_shifts = (R21_data.text)
    R21_shifts = R21_shifts.replace("FOH General\n", "")
    Row_21.append(R21_shifts)
    R21_Columns += 1 

#Row 22 
emp22 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[22]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][22]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp22_name = emp22.text
Row_22.append(emp22_name)

R22_Columns = 1
for A in range (0,7):
    R22_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[22]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][22]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R22_Columns) + "]")
    R22_shifts = (R22_data.text)
    R22_shifts = R22_shifts.replace("FOH General\n", "")
    Row_22.append(R22_shifts)
    R22_Columns += 1 

#Row 23 
emp23 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[23]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][23]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp23_name = emp23.text
Row_23.append(emp23_name)

R23_Columns = 1
for A in range (0,7):
    R23_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[23]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][23]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R23_Columns) + "]")
    R23_shifts = (R23_data.text)
    R23_shifts = R23_shifts.replace("FOH General\n", "")
    Row_23.append(R23_shifts)
    R23_Columns += 1 

#Row 24 
emp24 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[24]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][24]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp24_name = emp24.text
Row_24.append(emp24_name)

R24_Columns = 1
for A in range (0,7):
    R24_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[24]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][24]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R24_Columns) + "]")
    R24_shifts = (R24_data.text)
    R24_shifts = R24_shifts.replace("FOH General\n", "")
    Row_24.append(R24_shifts)
    R24_Columns += 1 

#Row 25 
emp25 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[25]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][25]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp25_name = emp25.text
Row_25.append(emp25_name)

R25_Columns = 1
for A in range (0,7):
    R25_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[25]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][25]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R25_Columns) + "]")
    R25_shifts = (R25_data.text)
    R25_shifts = R25_shifts.replace("FOH General\n", "")
    Row_25.append(R25_shifts)
    R25_Columns += 1 

#Row 26 
emp26 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[26]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][26]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp26_name = emp26.text
Row_26.append(emp26_name)

R26_Columns = 1
for A in range (0,7):
    R26_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[26]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][26]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R26_Columns) + "]")
    R26_shifts = (R26_data.text)
    R26_shifts = R26_shifts.replace("FOH General\n", "")
    Row_26.append(R26_shifts)
    R26_Columns += 1 

#Row 27 
emp27 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[27]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][27]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp27_name = emp27.text
Row_27.append(emp27_name)

R27_Columns = 1
for A in range (0,7):
    R27_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[27]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][27]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R27_Columns) + "]")
    R27_shifts = (R27_data.text)
    R27_shifts = R27_shifts.replace("FOH General\n", "")
    Row_27.append(R27_shifts)
    R27_Columns += 1 

#Row 28 
emp28 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[28]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][28]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp28_name = emp28.text
Row_28.append(emp28_name)

R28_Columns = 1
for A in range (0,7):
    R28_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[28]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][28]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R28_Columns) + "]")
    R28_shifts = (R28_data.text)
    R28_shifts = R28_shifts.replace("FOH General\n", "")
    Row_28.append(R28_shifts)
    R28_Columns += 1 

#Row 29 
emp29 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[29]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][29]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp29_name = emp29.text
Row_29.append(emp29_name)

R29_Columns = 1
for A in range (0,7):
    R29_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[29]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][29]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R29_Columns) + "]")
    R29_shifts = (R29_data.text)
    R29_shifts = R29_shifts.replace("FOH General\n", "")
    Row_29.append(R29_shifts)
    R29_Columns += 1 

#Row 30 
emp30 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[30]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][30]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp30_name = emp30.text
Row_30.append(emp30_name)

R30_Columns = 1
for A in range (0,7):
    R30_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[30]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][30]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R30_Columns) + "]")
    R30_shifts = (R30_data.text)
    R30_shifts = R30_shifts.replace("FOH General\n", "")
    Row_30.append(R30_shifts)
    R30_Columns += 1 

#Row 31 
emp31 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[31]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][31]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp31_name = emp31.text
Row_31.append(emp31_name)

R31_Columns = 1
for A in range (0,7):
    R31_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[31]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][31]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R31_Columns) + "]")
    R31_shifts = (R31_data.text)
    R31_shifts = R31_shifts.replace("FOH General\n", "")
    Row_31.append(R31_shifts)
    R31_Columns += 1 

#Row 32 
emp32 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[32]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][32]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp32_name = emp32.text
Row_32.append(emp32_name)

R32_Columns = 1
for A in range (0,7):
    R32_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[32]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][32]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R32_Columns) + "]")
    R32_shifts = (R32_data.text)
    R32_shifts = R32_shifts.replace("FOH General\n", "")
    Row_32.append(R32_shifts)
    R32_Columns += 1 

#Row 33 
emp33 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[33]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][33]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp33_name = emp33.text
Row_33.append(emp33_name)

R33_Columns = 1
for A in range (0,7):
    R33_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[33]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][33]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R33_Columns) + "]")
    R33_shifts = (R33_data.text)
    R33_shifts = R33_shifts.replace("FOH General\n", "")
    Row_33.append(R33_shifts)
    R33_Columns += 1 

#Row 34 
emp34 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[34]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][34]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp34_name = emp34.text
Row_34.append(emp34_name)

R34_Columns = 1
for A in range (0,7):
    R34_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[34]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][34]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R34_Columns) + "]")
    R34_shifts = (R34_data.text)
    R34_shifts = R34_shifts.replace("FOH General\n", "")
    Row_34.append(R34_shifts)
    R34_Columns += 1 

#Row 35 
emp35 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[35]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][35]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp35_name = emp35.text
Row_35.append(emp35_name)

R35_Columns = 1
for A in range (0,7):
    R35_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[35]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][35]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R35_Columns) + "]")
    R35_shifts = (R35_data.text)
    R35_shifts = R35_shifts.replace("FOH General\n", "")
    Row_35.append(R35_shifts)
    R35_Columns += 1 

#Row 36 
emp36 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[36]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][36]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp36_name = emp36.text
Row_36.append(emp36_name)

R36_Columns = 1
for A in range (0,7):
    R36_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[36]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][36]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R36_Columns) + "]")
    R36_shifts = (R36_data.text)
    R36_shifts = R36_shifts.replace("FOH General\n", "")
    Row_36.append(R36_shifts)
    R36_Columns += 1 

#Row 37 
emp37 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[37]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][37]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp37_name = emp37.text
Row_37.append(emp37_name)

R37_Columns = 1
for A in range (0,7):
    R37_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[37]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][37]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R37_Columns) + "]")
    R37_shifts = (R37_data.text)
    R37_shifts = R37_shifts.replace("FOH General\n", "")
    Row_37.append(R37_shifts)
    R37_Columns += 1 

#Row 38 
emp38 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[38]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][38]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp38_name = emp38.text
Row_38.append(emp38_name)

R38_Columns = 1
for A in range (0,7):
    R38_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[38]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][38]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R38_Columns) + "]")
    R38_shifts = (R38_data.text)
    R38_shifts = R38_shifts.replace("FOH General\n", "")
    Row_38.append(R38_shifts)
    R38_Columns += 1 

#Row 39 
emp39 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[39]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][39]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp39_name = emp39.text
Row_39.append(emp39_name)

R39_Columns = 1
for A in range (0,7):
    R39_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[39]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][39]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R39_Columns) + "]")
    R39_shifts = (R39_data.text)
    R39_shifts = R39_shifts.replace("FOH General\n", "")
    Row_39.append(R39_shifts)
    R39_Columns += 1 

#Row 40 
emp40 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[40]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][40]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp40_name = emp40.text
Row_40.append(emp40_name)

R40_Columns = 1
for A in range (0,7):
    R40_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[40]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][40]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R40_Columns) + "]")
    R40_shifts = (R40_data.text)
    R40_shifts = R40_shifts.replace("FOH General\n", "")
    Row_40.append(R40_shifts)
    R40_Columns += 1 

#Row 41 
emp41 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[41]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][41]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp41_name = emp41.text
Row_41.append(emp41_name)

R41_Columns = 1
for A in range (0,7):
    R41_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[41]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][41]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R41_Columns) + "]")
    R41_shifts = (R41_data.text)
    R41_shifts = R41_shifts.replace("FOH General\n", "")
    Row_41.append(R41_shifts)
    R41_Columns += 1 

#Row 42 
emp42 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[42]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][42]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp42_name = emp42.text
Row_42.append(emp42_name)

R42_Columns = 1
for A in range (0,7):
    R42_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[42]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][42]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R42_Columns) + "]")
    R42_shifts = (R42_data.text)
    R42_shifts = R42_shifts.replace("FOH General\n", "")
    Row_42.append(R42_shifts)
    R42_Columns += 1 

#Row 43 
emp43 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[43]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][43]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp43_name = emp43.text
Row_43.append(emp43_name)

R43_Columns = 1
for A in range (0,7):
    R43_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[43]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][43]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R43_Columns) + "]")
    R43_shifts = (R43_data.text)
    R43_shifts = R43_shifts.replace("FOH General\n", "")
    Row_43.append(R43_shifts)
    R43_Columns += 1 

#Row 44 
emp44 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[44]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][44]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp44_name = emp44.text
Row_44.append(emp44_name)

R44_Columns = 1
for A in range (0,7):
    R44_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[44]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][44]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R44_Columns) + "]")
    R44_shifts = (R44_data.text)
    R44_shifts = R44_shifts.replace("FOH General\n", "")
    Row_44.append(R44_shifts)
    R44_Columns += 1 

#Row 45 
emp45 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[45]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][45]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp45_name = emp45.text
Row_45.append(emp45_name)

R45_Columns = 1
for A in range (0,7):
    R45_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[45]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][45]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R45_Columns) + "]")
    R45_shifts = (R45_data.text)
    R45_shifts = R45_shifts.replace("FOH General\n", "")
    Row_45.append(R45_shifts)
    R45_Columns += 1 

#Row 46 
emp46 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[46]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][46]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp46_name = emp46.text
Row_46.append(emp46_name)

R46_Columns = 1
for A in range (0,7):
    R46_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[46]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][46]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R46_Columns) + "]")
    R46_shifts = (R46_data.text)
    R46_shifts = R46_shifts.replace("FOH General\n", "")
    Row_46.append(R46_shifts)
    R46_Columns += 1 

#Row 47 
emp47 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[47]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][47]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp47_name = emp47.text
Row_47.append(emp47_name)

R47_Columns = 1
for A in range (0,7):
    R47_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[47]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][47]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R47_Columns) + "]")
    R47_shifts = (R47_data.text)
    R47_shifts = R47_shifts.replace("FOH General\n", "")
    Row_47.append(R47_shifts)
    R47_Columns += 1 

#Row 48 
emp48 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[48]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][48]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp48_name = emp48.text
Row_48.append(emp48_name)

R48_Columns = 1
for A in range (0,7):
    R48_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[48]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][48]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R48_Columns) + "]")
    R48_shifts = (R48_data.text)
    R48_shifts = R48_shifts.replace("FOH General\n", "")
    Row_48.append(R48_shifts)
    R48_Columns += 1 

#Row 49 
emp49 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[49]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][49]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp49_name = emp49.text
Row_49.append(emp49_name)

R49_Columns = 1
for A in range (0,7):
    R49_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[49]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][49]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R49_Columns) + "]")
    R49_shifts = (R49_data.text)
    R49_shifts = R49_shifts.replace("FOH General\n", "")
    Row_49.append(R49_shifts)
    R49_Columns += 1 

#Row 50 
emp50 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[50]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][50]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp50_name = emp50.text
Row_50.append(emp50_name)

R50_Columns = 1
for A in range (0,7):
    R50_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[50]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][50]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R50_Columns) + "]")
    R50_shifts = (R50_data.text)
    R50_shifts = R50_shifts.replace("FOH General\n", "")
    Row_50.append(R50_shifts)
    R50_Columns += 1 

#Row 51 
emp51 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[51]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][51]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp51_name = emp51.text
Row_51.append(emp51_name)

R51_Columns = 1
for A in range (0,7):
    R51_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[51]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][51]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R51_Columns) + "]")
    R51_shifts = (R51_data.text)
    R51_shifts = R51_shifts.replace("FOH General\n", "")
    Row_51.append(R51_shifts)
    R51_Columns += 1 

#Row 52 
emp52 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[52]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][52]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp52_name = emp52.text
Row_52.append(emp52_name)

R52_Columns = 1
for A in range (0,7):
    R52_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[52]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][52]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R52_Columns) + "]")
    R52_shifts = (R52_data.text)
    R52_shifts = R52_shifts.replace("FOH General\n", "")
    Row_52.append(R52_shifts)
    R52_Columns += 1 

#Row 53 
emp53 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[53]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][53]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp53_name = emp53.text
Row_53.append(emp53_name)

R53_Columns = 1
for A in range (0,7):
    R53_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[53]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][53]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R53_Columns) + "]")
    R53_shifts = (R53_data.text)
    R53_shifts = R53_shifts.replace("FOH General\n", "")
    Row_53.append(R53_shifts)
    R53_Columns += 1 

#Row 54 
emp54 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[54]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][54]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp54_name = emp54.text
Row_54.append(emp54_name)

R54_Columns = 1
for A in range (0,7):
    R54_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[54]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][54]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R54_Columns) + "]")
    R54_shifts = (R54_data.text)
    R54_shifts = R54_shifts.replace("FOH General\n", "")
    Row_54.append(R54_shifts)
    R54_Columns += 1 

#Row 55 
emp55 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[55]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][55]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp55_name = emp55.text
Row_55.append(emp55_name)

R55_Columns = 1
for A in range (0,7):
    R55_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[55]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][55]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R55_Columns) + "]")
    R55_shifts = (R55_data.text)
    R55_shifts = R55_shifts.replace("FOH General\n", "")
    Row_55.append(R55_shifts)
    R55_Columns += 1 

#Row 56 
emp56 = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[56]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][56]/div[@class='schedule-table-cell employee']/div[@class='employee-name']")
emp56_name = emp56.text
Row_56.append(emp56_name)

R56_Columns = 1
for A in range (0,7):
    R56_data = driver.find_element(By.XPATH, "/html[@class='hs-echo-ui clarifi-lobal-nav']/body[@class='screen-employeeHome employee-home-page']/div[@id='entire-taskarea-wrapper']/div[@id='root']/div[@class='employee-home']/div/div[@class='employee-home-inner-page']/div[@class='page-content']/div[@class='emp-home-widgets-dashboard']/div[@class='inner-content widgets-count-3']/div[@class='emp-home-base-widget is-expanded']/div[@class='inner different-layout']/div[@class='expanded-view all-schedules']/div[@class='children-container']/div[@class='emp-home-all-schedules-widget']/div[@class='all-schedules-container']/div[@class='all-schedules-details']/div[@class='my-schedules-items']/div[56]/div[@class='full-schedule']/div[@class='schedule-table']/div[@class='schedule-table-row'][56]/div[@class='days-row grayed border-top']/div[@class='schedule-table-cell scheduled-shift'][" + str (R56_Columns) + "]")
    R56_shifts = (R56_data.text)
    R56_shifts = R56_shifts.replace("FOH General\n", "")
    Row_56.append(R56_shifts)
    R56_Columns += 1 

print = (Row_1)
print = (Row_2)
print = (Row_3)
print = (Row_4)
print = (Row_5)
print = (Row_6)
print = (Row_7)
print = (Row_8)
print = (Row_9)
print = (Row_10)
print = (Row_11)
print = (Row_12)
print = (Row_13)
print = (Row_14)
print = (Row_15)
print = (Row_16)
print = (Row_17)
print = (Row_18)
print = (Row_19)
print = (Row_20)
print = (Row_21)
print = (Row_22)
print = (Row_23)
print = (Row_24)
print = (Row_25)
print = (Row_26)
print = (Row_27)
print = (Row_28)
print = (Row_29)
print = (Row_30)
print = (Row_31)
print = (Row_32)
print = (Row_33)
print = (Row_34)
print = (Row_35)
print = (Row_36)
print = (Row_37)
print = (Row_38)
print = (Row_39)
print = (Row_40)
print = (Row_41)
print = (Row_42)
print = (Row_43)
print = (Row_44)
print = (Row_45)
print = (Row_46)
print = (Row_47)
print = (Row_48)
print = (Row_49)
print = (Row_50)
print = (Row_51)
print = (Row_52)
print = (Row_53)
print = (Row_54)
print = (Row_55)
print = (Row_56)
