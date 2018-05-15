from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import numpy as np
import pandas as pd
import time
import csv
import re

driver = webdriver.Chrome(r'.\chromedriver.exe')
csv_file = open('cities.csv', 'w')
writer = csv.writer(csv_file)

driver.get('https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population')
time.sleep(5)
list_table = driver.find_element_by_xpath('//table[@class="wikitable sortable jquery-tablesorter"]')
rows = list_table.find_elements_by_xpath('.//tr')
for row in rows:
	try:
		city = {}
		name = row.find_element_by_xpath('./td[2]').text
		area = row.find_element_by_xpath('./td[8]').text
		density = row.find_element_by_xpath('./td[10]').text
		geo = row.find_element_by_xpath('./td[11]//span[@class="geo-dec"]').text
		lat = re.findall('\d+\.\d+',geo)[0]
		lon = re.findall('\d+\.\d+',geo)[1]
		city['name'] = re.sub('\[\d+\]','',name)
		city['area'] = area.replace(' km2','').replace(',','')
		city['density'] = density.replace('/km2','').replace(',','')
		city['lat'] = lat
		city['lon'] = lon
		print('#', end='', flush=True)
		writer.writerow(city.values())
	except Exception as e:
		print(e)
		continue
csv_file.close()
driver.close()