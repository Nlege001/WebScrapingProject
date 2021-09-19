# importing the modules
import urllib
import ssl
from urllib.request import Request, urlopen

import bs4
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

ssl._create_default_https_context = ssl._create_unverified_context

url = Request("https://www.plattsburgh.edu/directory/", headers= {'User-Agent':'Mozilla/5.0'})
url_contents = urlopen(url).read()

baseURL ="https://www.plattsburgh.edu/directory/"
driver = webdriver.Chrome(executable_path= "/Users/naol/Downloads/chromedriver")
driver.get(baseURL)

soup = bs4.BeautifulSoup(url_contents, "html")

div = soup.findAll("div", {'class':'platts-custom-form-style'})
#print(div)

elem= driver.find_element_by_xpath("//div[@id='findpeople']")
#faculty = []
faculty = elem.find_elements_by_tag_name('ul')


print(faculty)

faculty_list = []

for f in faculty:
    faculty_list.append(f.text.split('\n'))

print(faculty_list)


