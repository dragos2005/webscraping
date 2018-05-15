from scrapy import Spider
from locationreddits.items import LocationredditsItem
import re


class LocationredditsSpider(Spider):
	name = 'locationreddits_spider'
	allowed_urls = ['www.reddit.com']
	start_urls = ['https://www.reddit.com/r/LocationReddits/wiki/faq/northamerica']

	def parse(self, response):
		linktable = response.xpath('//a[@href]')
		patt = re.compile('^/r/\w+$')
		for link in linktable:
			ref = link.xpath('@href').extract_first()
			if patt.match(ref) is None:
				continue
			value = link.xpath('./text()').extract_first()
			print('ref = ' + ref + ' , value = ' + value)

			item = LocationredditsItem()
			item['url'] = ref
			item['name'] = value
			yield item