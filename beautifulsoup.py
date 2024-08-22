from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# res = requests.get("sdasda")
# html_content = res.content
# sp = BeautifulSoup(html_content,"lxml")

driver.get("https://ca.indeed.com/")
time.sleep(10)
html_page = driver.page_source
sp = BeautifulSoup(html_page,'lxml')

job_title = "manager"
location = "toronto"

pos_elmt = driver.find_element(By.XPATH,'//div[@class="css-nfhrw4 eu4oa1w0"]//input')
pos_elmt.click()
pos_elmt.send_keys(job_title)
pos_elmt.send_keys(Keys.ENTER)
time.sleep(3)
loc_elmt = driver.find_element(By.XPATH,'//div[@class="css-1jk1vg0 eu4oa1w0"]//input')
loc_elmt.click()
time.sleep(2)
loc_elmt.send_keys(Keys.CONTROL + "a")
loc_elmt.send_keys(Keys.DELETE)
print("waiting for 5 sec....")
time.sleep(5)
loc_elmt.send_keys(location)
loc_elmt.send_keys(Keys.ENTER)
time.sleep(5)

headings = driver.find_elements(By.XPATH,"//h2//a")
for i in headings:
    print(i.text)
print("******        ************")
html_page = driver.page_source
sp = BeautifulSoup(html_page,'lxml')
res_pos = sp.select("h2 a")
for position in res_pos:
    print(position.get_text())

# print(sp)
































# from bs4 import BeautifulSoup as bts
# import requests

# res = requests.get("http://example.com")
# html_cnt = res.content

# sp = bts(html_cnt, 'lxml')

# title_tag = sp.title
# print(title_tag)
# print(title_tag.string)

# link_emt = sp.find('a',href=True)
# print(link_emt['href'])

# links = sp.find_all('a')
# for link in links:
#     print(link['href'])

# new_tag = sp.new_tag("a", href="http:.com")
# new_tag.string = "Link"
# sp.body.append(new_tag)
# print(sp.body) 




