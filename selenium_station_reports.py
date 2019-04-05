from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time
import pandas as pd
import os
import glob

#generate list of month start/end dates
months = pd.date_range('2014-01-01', '2018-12-31', freq='1M')



#access RWIS login
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "D:/vdot_reports"}
chromeOptions.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chromeOptions)

driver.get('<website>')

#locate username form
user_login = driver.find_element_by_id('username')
#enter username login
user_login.send_keys('<username>')
user_login.send_keys(Keys.RETURN)

#locate password form
pass_login = driver.find_element_by_id('password')
#enter username login
pass_login.send_keys('<password>')
pass_login.send_keys(Keys.RETURN)

#go to reports page
time.sleep(3)
driver.get('https://rds.vaisala.com/apps/#reports')
time.sleep(15)
#locate station dropdown
station_form = driver.find_element_by_id('chozen_container__0_chzn')


#locate date forms
start_date_form = driver.find_element_by_id('gwt-debug-start-date')
start_time_form = driver.find_element_by_id('gwt-debug-start-time')
end_date_form = driver.find_element_by_id('gwt-debug-end-date')
end_time_form = driver.find_element_by_id('gwt-debug-end-time')
#locate submit button
submit_button = driver.find_element_by_xpath('//*[@id="rds-body"]/div[4]/div[2]/div/div/div/div[2]/div/div[3]/div/div[2]/div/div[3]/div/div[3]/div/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[1]/div[2]/div/table/tbody/tr[4]/td[2]/table/tbody/tr/td[2]')

#click to open station dropdown
#station_form.click()
#time.sleep(1)

#set time period
select_start_time = Select(start_time_form)
select_start_time.select_by_visible_text('12:00 AM UTC')

select_end_time = Select(end_time_form)
select_end_time.select_by_visible_text('11:00 PM UTC')


#main loop

stationidx = 0
for station in range(96):
    station_form.click()
    time.sleep(1)
    station_element = driver.find_element_by_id('chozen_container__0_chzn_o_' + str(stationidx))
    station_element.click()
    time.sleep(1)
    #set dates
    for month in months:
        start_date_form.clear()
        start_date_form.send_keys((month-pd.offsets.MonthBegin(1)).strftime("%m.%d.%Y"))
        end_date_form.clear()
        end_date_form.send_keys(month.strftime("%m.%d.%Y"))
        #clean up calendar day picker
        driver.find_element_by_id('rds-body').click()
        #click submit button
        time.sleep(1)
        submit_button.click()
        time.sleep(6)
    time.sleep(10)
    station_months = []
    path = r'D:/vdot_reports/'
    files_remove = glob.glob(path + '*')

    for filename in os.listdir(path):
        if filename.endswith(".xlsx") and os.stat(path+filename).st_size > 15000:
            station_months.append(pd.read_excel(path+filename, header=4))
    if len(station_months) > 0:
        stationdf_full = pd.concat(station_months, sort=False)
        stationdf_full.to_csv(str(stationidx)+'.csv')
    for f in files_remove:
        if filename.endswith(".xlsx"):
            os.remove(f)
    stationidx = stationidx + 1
    time.sleep(1)
