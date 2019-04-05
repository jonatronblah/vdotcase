rom selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time
import pandas as pd


#access RWIS login
driver = webdriver.Chrome()
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

#go to stations page
time.sleep(3)
driver.get('https://rds.vaisala.com/apps/#stations/station-overview')
time.sleep(10)

#locate station parent
stationparent = driver.find_element_by_xpath('//*[@id="gwt-debug-SingleStationSidePanelStations"]/div[2]')

stationlist = stationparent.find_elements_by_xpath(".//*")

list_of_stations = []
for station in stationlist:
        if len(str(station.get_attribute("innerText"))) >= 3 and len(str(station.get_attribute("innerText"))) < 60:
            list_of_stations.append(str(station.get_attribute("innerText")))

list_of_stations.remove('All Sites\n')
list_of_stations.remove('All Sites')
#not sure why this didn't work - add manually
list_of_stations.remove('I-95 Exit 170 Ramp I-95 S (Site B)')
list_of_stations.remove('I-95 Exit 170 Ramp I-95 S (Site B)')
stationlist_pd = pd.DataFrame(list_of_stations)

stationlist_pd = stationlist_pd[~stationlist_pd[0].str.contains('(F)', regex=False)]

stationlist_pd = stationlist_pd.drop_duplicates()



lat = []
lon = []
alt = []
for element in stationlist_pd.iloc[:,0]:
        #use text names to locate each station
        element_location = stationparent.find_element_by_xpath(f"//*[contains(text(), '{element}')]")
        element_location.click()
        time.sleep(1)
        lat.append(driver.find_element_by_xpath('//*[@id="rds-body"]/div[4]/div[2]/div/div/div/div[2]/div/div[3]/div/div[2]/div/div[3]/div/div[3]/div/div[2]/div/div[2]/div/div[4]/div/div[2]/div/div[2]/table/tbody/tr[2]/td/div/div/table/tbody/tr/td[1]/div/div[2]/span[1]').get_attribute('innerText'))
        lon.append(driver.find_element_by_xpath('//*[@id="rds-body"]/div[4]/div[2]/div/div/div/div[2]/div/div[3]/div/div[2]/div/div[3]/div/div[3]/div/div[2]/div/div[2]/div/div[4]/div/div[2]/div/div[2]/table/tbody/tr[2]/td/div/div/table/tbody/tr/td[1]/div/div[2]/span[2]').get_attribute('innerText')) 

        #add conditional: if altitude element exists, get it, otherwise insert null value
        if driver.find_elements_by_xpath('//*[@id="rds-body"]/div[4]/div[2]/div/div/div/div[2]/div/div[3]/div/div[2]/div/div[3]/div/div[3]/div/div[2]/div/div[2]/div/div[4]/div/div[2]/div/div[2]/table/tbody/tr[2]/td/div/div/table/tbody/tr/td[1]/div/div[4]/span[1]'):
                alt.append(driver.find_element_by_xpath('//*[@id="rds-body"]/div[4]/div[2]/div/div/div/div[2]/div/div[3]/div/div[2]/div/div[3]/div/div[3]/div/div[2]/div/div[2]/div/div[4]/div/div[2]/div/div[2]/table/tbody/tr[2]/td/div/div/table/tbody/tr/td[1]/div/div[4]/span[1]').get_attribute('innerText'))
        else:
                alt.append('NaN')

stationlist_pd['lat'] = lat
stationlist_pd['lon'] = lon
stationlist_pd['alt'] = alt