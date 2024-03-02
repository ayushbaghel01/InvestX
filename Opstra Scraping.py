import os
import time
from matplotlib.dates import WE
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


os.environ['Path'] += "C:/Users/dell/Downloads/geckodriver-v0.33.0-win32.zip"
# os.environ['PATH'] +="C:/seleniumdriver"

website = 'https://opstra.definedge.com/'

driver = webdriver.Firefox()
driver.get(website)
driver.maximize_window()

login_button = driver.find_element(By.XPATH, "//button[@class='v-btn v-btn--flat theme--dark']")
login_button.click()

username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")

username.send_keys('ayushjln499@gmail.com')
password.send_keys('Ayush789%^')


login_button = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.ID, "kc-login")))
login_button.click()

open_interest_dropdown = WebDriverWait(driver,10).until(ec.element_to_be_clickable((By.XPATH,"//div[@class='v-menu v-menu--inline'][3]")))
open_interest_dropdown.click()

open_chain_select = WebDriverWait(driver,10).until(ec.element_to_be_clickable((By.XPATH,"//div[@style='height: 40px;'][9]")))
open_chain_select.click()


time.sleep(2)


for i in range(10):
    CALL_OI_chng=[]
    CALL_OI=[]
    CALL_Volume=[]
    CALL_ITM_prob=[]
    CALL_IV=[]
    CALL_LTP=[]
    CALL_CHNG=[]
    Strike=[]
    PUT_CHNG=[]
    PUT_LTP=[]
    PUT_IV=[]
    PUT_ITM_prob=[]
    PUT_Volume=[]
    PUT_OI=[]
    PUT_OI_chng=[]
    
    
    obscuring_element = WebDriverWait(driver,10).until(ec.invisibility_of_element((By.XPATH, "//div[@class = 'vid-background']")))
    date_select_dropdown = WebDriverWait(driver,10).until(ec.element_to_be_clickable((By.XPATH,"//div[@class='flex xs12 md4 ml-3'][2]")))
    date_select_dropdown.click()
    xpath_expression = f"//div[@role='listitem'][{i+1}]"

    date_select = WebDriverWait(driver,10).until(ec.element_to_be_clickable((By.XPATH, xpath_expression)))
    date_select.click()
    data_table = WebDriverWait(driver,10).until(ec.presence_of_all_elements_located((By.XPATH, "//table[@id='grid_2033181033_0_content_table']/tbody/tr")))

     
    if (i!=6) :
        for data in data_table:
                
                # print(data.text)
                CALL_OI_chng.append(data.find_element(By.XPATH,"./td[1]").text)
                CALL_OI.append(data.find_element(By.XPATH,"./td[2]").text)
                CALL_Volume.append(data.find_element(By.XPATH,"./td[3]").text)
                CALL_ITM_prob.append(data.find_element(By.XPATH,"./td[4]").text)
                CALL_IV.append(data.find_element(By.XPATH,"./td[5]").text)
                CALL_LTP.append(data.find_element(By.XPATH,"./td[6]").text)
                CALL_CHNG.append(data.find_element(By.XPATH,"./td[7]").text)
                Strike.append(data.find_element(By.XPATH,"./td[8]").text)
                PUT_CHNG.append(data.find_element(By.XPATH,"./td[9]").text)
                PUT_LTP.append(data.find_element(By.XPATH,"./td[10]").text)
                PUT_Volume.append(data.find_element(By.XPATH,"./td[11]").text)
                PUT_IV.append(data.find_element(By.XPATH,"./td[12]").text)
                PUT_ITM_prob.append(data.find_element(By.XPATH,"./td[13]").text)
                PUT_OI_chng.append(data.find_element(By.XPATH,"./td[14]").text)
                PUT_OI.append(data.find_element(By.XPATH,"./td[15]").text)
                
            
        df = pd.DataFrame({ 'CALL_OI_chng':CALL_OI_chng,'CALL_OI':CALL_OI,
                            'CALL_Volume':CALL_Volume,'CALL_ITM_prob':CALL_ITM_prob,
                            'CALL_LTP':CALL_LTP, 'CALL_CHNG':CALL_CHNG,'Strike':Strike,
                            'PUT_CHNG':PUT_CHNG,'PUT_LTP':PUT_LTP, 'PUT_Volume':PUT_Volume,
                            'PUT_IV': PUT_IV,  'PUT_ITM_prob': PUT_ITM_prob, 
                            'PUT_OI_chng':PUT_OI_chng,'PUT_OI':PUT_OI })
            
        csv_name=f'csv_({i+1}).csv'
        print("file_created")
        df.to_csv(csv_name, index=False)
driver.quit()