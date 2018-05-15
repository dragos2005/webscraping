from scrapy import Spider
from wikipop.items import WikipopItem
import re


class WikipopSpider(Spider):
	name = 'wikipop_spider'
	allowed_urls = ['en.wikipedia.org']
	start_urls = ['https://en.wikipedia.org/wiki/List_of_metropolitan_statistical_areas']

	def parse(self, response):
		cities = response.xpath('//table[@class="wikitable sortable"]')[0].xpath('./tr')[1:]
		citypattern = re.compile('^[^-,–/]+')
		statepattern = re.compile(', ([A-Z][A-Z])')
		for city in cities:
			fullname = city.xpath('./td[2]/a/text()').extract_first()
			fullpop2017 = city.xpath('./td[3]/text()').extract_first()
			fullpop2010 = city.xpath('./td[4]/text()').extract_first()

			item = WikipopItem()
			item['name'] = citypattern.search(fullname)[0]
			item['state'] = statepattern.search(fullname)[1]
			item['pop2017'] = fullpop2017.replace(',','')
			item['pop2010'] = fullpop2010.replace(',','')
			yield item

