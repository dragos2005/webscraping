from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import numpy as np
import pandas as pd
import time
import csv

# Windows users need to specify the path to chrome driver you just downloaded.
# You need to unzip the zipfile first and move the .exe file to any folder you want.
driver = webdriver.Chrome(r'.\chromedriver.exe')
csv_file = open('reddit.csv', 'a')
writer = csv.writer(csv_file)

#driver = webdriver.Chrome()
# Go to the page that we want to scrape

citylist = pd.read_csv('./wikipop/wikipop.csv')
citylist = citylist[99:100]
print(citylist)
for i, city in citylist.iterrows():
	print(city)
	cityname = city['name']
	if city['name'] == 'New York':
		cityname = 'NYC'
	if city['name'] == 'Washington':
		cityname = 'WashingtonDC'
	if city['name'] == 'Richmond':
		cityname = 'RVA'
	if city['name'] == 'Urban Honolulu':
		cityname = 'Honolulu'
	if city['name'] == 'Bridgeport':
		cityname = 'BridgeportCT'
	if city['name'] == 'Worcester':
		cityname = 'WorcesterMA'
	if city['name'] == 'Columbia':
		cityname = 'ColumbiaSC'
	if city['name'] == 'North Port':
		cityname = 'Sarasota'
	if city['name'] == 'Greensboro':
		cityname = 'GSO'
	if city['name'] == 'Stockton':
		cityname = 'StocktonCA'
	if city['name'] == 'Boise City':
		cityname = 'Boise'
	if city['name'] == 'Winston':
		cityname = 'WinstonSalem'
	if city['name'] == 'Madison':
		cityname = 'MadisonWI'
	if city['name'] == 'Provo':
		cityname = 'ProvoUtah'
	if city['name'] == 'Jackson':
		cityname = 'JacksonMS'
	if city['name'] == 'Durham':
		cityname = 'BullCity'
	url = "https://www.reddit.com/r/" + cityname.lower().replace(' ','').replace('.','') + "/top/?t=all"
	print(url)
	try:
		driver.get(url)
	except Exception as e:
		print(e)
		continue
	time.sleep(5)

	index = 1
	while (index < 1000):
		print(index)
		try:
			posttable_wait = WebDriverWait(driver, 10)
			posttable = posttable_wait.until(EC.presence_of_element_located((By.XPATH,
				'//div[@id="siteTable"]')))
			posts = posttable.find_elements_by_xpath('./div[@data-context="listing"]')
			print('scraping post number = ' + str(index))
			print('len(posts) = ' + str(len(posts)))
			print('='*80)
			for post in posts:
				postdict = {}
				postname = post.find_element_by_xpath('./div[@class="entry unvoted"]/div[@class="top-matter"]/p[@class="title"]/a').text
				postcomments = post.get_attribute('data-comments-count')
				postscore = post.get_attribute('data-score')
				postdomain = post.get_attribute('data-domain')
				posttime = post.find_element_by_xpath('./div[@class="entry unvoted"]/div[@class="top-matter"]/p[@class="tagline "]/time').get_attribute('datetime')
				print('postname = ' + postname)
				print('postcomments = ' + postcomments)
				print('postscore = ' + postscore)
				print('postdomain = ' + postdomain)
				print('posttime = ' + posttime)
				print('*'*50)

				postdict['cityname'] = city['name']
				postdict['citystate'] = city['state']
				postdict['citypop2017'] = city['pop2017']
				postdict['citypop2010'] = city['pop2010']
				postdict['text'] = postname
				postdict['numcomments'] = postcomments
				postdict['score'] = postscore
				postdict['domain'] = postdomain
				postdict['datetime'] = posttime
				try:
					writer.writerow(postdict.values())
				except Exception as e:
					print(e)
					continue
			index = index + 25
			nextButton_wait = WebDriverWait(driver, 10)
			nextButton = nextButton_wait.until(EC.presence_of_element_located((By.XPATH,
				'//span[@class="next-button"]/a')))
			nextButton.click()
		except Exception as e:
			print(e)
			break
		print('Scraped ' + str(index) + ' items.')
csv_file.close()
driver.close()

# Click review button to go to the review section
# review_button = driver.find_element_by_xpath('//span[@class="padLeft6 cursorPointer"]')
# review_button.click()

# Page index used to keep track of where we are.
index = 1
# We want to start the first two pages.
# If everything works, we will change it to while True
# while index <=2:
# 	try:
# 		print("Scraping Page number " + str(index))
# 		index = index + 1
# 		# Find all the reviews. The find_elements function will return a list of selenium select elements.
# 		# Check the documentation here: http://selenium-python.readthedocs.io/locating-elements.html
# 		reviews = driver.find_elements_by_xpath('//div[@itemprop="review"]')
# 		print("Length of reviews: {}".format(len(reviews)))
# 		# Iterate through the list and find the details of each review.
# 		for review in reviews:
# 			# Initialize an empty dictionary for each review
# 			review_dict = {}
# 			# Use relative xpath to locate the title, content, username, date, rating.
# 			# Once you locate the element, you can use 'element.text' to return its string.
# 			# To get the attribute instead of the text of each element, use `element.get_attribute()`

# 			try:
# 				read_more = review.find_element_by_xpath('.//a[@role="button"]')
# 				read_more.click()
# 			except:
# 				pass
# 			finally:
# 				title = review.find_element_by_xpath('.//div[@itemprop="headline"]').text
# 				print(title)
# 				# Your code here
# 				text = review.find_element_by_xpath('.//span[@itemprop="reviewBody"]').text
# 				print(text)
# 				rating = review.find_element_by_xpath('.//span[@itemprop="ratingValue"]').text
# 				print(rating)
# 				date = review.find_element_by_xpath('.//meta[@itemprop="datePublished"]').get_attribute('content')
# 				print(date)
# 				print('='*50)

# 		# Locate the next button element on the page and then call `button.click()` to click it.
# 		button = driver.find_element_by_xpath('//li[@class="nextClick displayInlineBlock padLeft5 "]')
# 		button.click()
# 		time.sleep(2)

# 	except Exception as e:
# 		print(e)
# 		driver.close()
# 		break
