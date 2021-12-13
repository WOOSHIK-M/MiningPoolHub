import ssl
from typing import Dict
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

####################
## Helper Command ##
####################

# run chrome web driver
driver = webdriver.Chrome(r'/usr/bin/chromedriver')
driver.get("https://www.naver.com")

exit()
# run the site thorugh `get` method
driver.get("https://ethereum.miningpoolhub.com/index.php?page=login")

# wait 3s to loading
# if the less time is used, it implements the next step
driver.implicitly_wait(3)

# click the login
login = driver.find_element_by_css_selector("li.my_page_service>a")

print(login)
print(log.tag_name)
print(login.text)
print(login.get_attribute("href"))


# email = input("email: ")
# password = input("password: ")

# # mining pool hub
# MPH_URL = "https://ethereum.miningpoolhub.com/index.php?page=account&action=pooledit"

# context = ssl._create_unverified_context()
# request_url = Request(MPH_URL, headers={"User-Agent": "Mozilla/5.0"})
# html = urlopen(request_url, context=context).read()
# soup = BeautifulSoup(html, "html.parser")

# blocks = soup.find_all(class_="module_content")

# print(blocks)
