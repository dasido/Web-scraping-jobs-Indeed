from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

opt_what = 'Intel'
opt_where = 'Haifa'

def process_manager():
    chrome_driver_path = r"C:/Projects/Web-scraping-jobs-main/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chrome_driver_path)

    job_title = []
    comp_name = []
    location = []
    print("what: " + opt_what)
    print("where: " + opt_where)
    driver.get(f"https://il.indeed.com/jobs?q={opt_what}&l={opt_where}")

 ### Date posted filter ###
    try:
       driver.find_element_by_xpath('//*[@id="filter-dateposted"]/div[1]').click()
       time.sleep(1)
    except:
     pass

 ### Last week filter ###
    try:
       driver.find_element_by_xpath('//*[@id="filter-dateposted-menu"]/li[3]/a').click()
       time.sleep(1)
    except:
     pass

 ### Attempt to get rid of the popup, in case it shows ###
    try:
       driver.find_element_by_xpath('//*[@id="popover-x"]/button').click()
    except NoSuchElementException:
       print("Popup did not pop up, all good.")

    job_cards = driver.find_elements_by_class_name("job_seen_beacon")

    countJobListingNumber = 1

    for job in job_cards:
        try:
           job_title_text = driver.find_element_by_xpath(f"/html/body/table[2]/tbody/tr/td/table/tbody/tr/td[1]/div[4]/div/a[{countJobListingNumber}]/div[1]/div/div[1]/div/table[1]/tbody/tr/td/div[1]/h2/span").text
           job_title.append(job_title_text)
           #print(job_title)
      
           #countJobListingNumber += 1
        except Exception as e:
           print(e)

        try:
           comp_name_text = driver.find_element_by_xpath(f"/html/body/table[2]/tbody/tr/td/table/tbody/tr/td[1]/div[4]/div/a[{countJobListingNumber}]/div[1]/div/div[1]/div/table[1]/tbody/tr/td/div[1]/h2/span").text
           comp_name.append(comp_name_text)
           #print(comp_name)
      
           #countJobListingNumber += 1
        except Exception as e:
           print(e)

        try:
           location_text = driver.find_element_by_xpath(f"/html/body/table[2]/tbody/tr/td/table/tbody/tr/td[1]/div[4]/div/a[{countJobListingNumber}]/div[1]/div/div[1]/div/table[1]/tbody/tr/td/div[1]/h2/span").text
           location.append(location_text)
           #print(location)
      
           #countJobListingNumber += 1
        except Exception as e:
           print(e)

        countJobListingNumber += 1

    df = pd.DataFrame({"Job Title": job_title, "Company Name": comp_name, "Location": location})
    df.head()
    #driver.close()
    return df


def init_user_filters(what, where):
   #global opt_what
   #global opt_where

   opt_what = what
   opt_where = where
    
   print("1: " + opt_what)
   print("2: " + opt_where)
