from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.chrome.service import Service
import json

fh=open("job_description.json", "w", encoding="utf-8")

### Read keyword
jobroles=["machine learning engineer","data engineer","business","customer success","management","business development","business analyst","graduate analyst","marketing analyst","backend developer","front end","full stack developer","sde","framework engineer","product engineer","test engineer","consulting engineer","advanced application engineering analyst","hardware engineer","user experience"]

### load selenium driver
PATH = "C:\Program Files (x86)\chromedriver.exe"
servic= Service(executable_path=PATH)
driver = webdriver.Chrome(service=servic)
driver.get("https://www.linkedin.com")
sleep(1)

### login
username = driver.find_element(By.ID,"session_key")
username.send_keys("shaloobsaluwdr@gmail.com")
password = driver.find_element(By.ID,"session_password")
password.send_keys("Skilltec@123")
driver.find_element(By.CLASS_NAME,"sign-in-form__submit-button").click()
sleep(2)

##search job
driver.get("https://www.linkedin.com/jobs")
sleep(2)


def search(i):
   search = driver.find_element(By.CLASS_NAME,"jobs-search-box__text-input")
   search.clear()
   search.send_keys(i)
   sleep(2)
   search.send_keys(Keys.RETURN)
   sleep(5)
      

descriptionlist=list()

def dataextract():
   i=1
   while i<=25:
      try:
         element=driver.find_element(By.XPATH,value='(//a[@class="disabled ember-view job-card-container__link job-card-list__title"])['+str(i)+']')
         element.click()
         if i%3==0:
            element.send_keys(Keys.PAGE_DOWN)
            sleep(2)
         sleep(1)   
         extracted_data=driver.find_element(By.XPATH,value='//div[@id="job-details"]')
         description=extracted_data.text.lower()
         descriptionlist.append(description)
         print("data extraction of job "+str(i)+" is completed")        
         sleep(1)
         i+=1
      except:
         print("Job",i,"not found")
         if i%3==0:
            element.send_keys(Keys.PAGE_DOWN)
            sleep(2)     
         sleep(1)     
         i+=1
         continue

def page(j):
   nextpage_buttons=driver.find_element(By.XPATH,value='//li[@data-test-pagination-page-btn="'+str(j)+'"]')       ##   //li[@data-test-pagination-page-btn="2"]
   nextpage_buttons.click()
new_dict = dict()   

for x in jobroles:
   search(x)
   for i in range(2,8): ## number of pages
      dataextract()
      page(i)
      print("\ndata extraction of page"+str(i-1)+" is completed")
      sleep(3)
      print("retrieving data from page "+str(i),"\n")
   #print("old count",len(descriptionlist))
   new_dict[x] =list(set(descriptionlist))
   descriptionlist.clear()


#print("new count",len(descriptionlist))
json.dump(new_dict, fh, indent=4)
print("\n---database creation for",len(new_dict),"jobs successfull---")