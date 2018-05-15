from wikipop.items import WikipopItem
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class WikipopPipeline(object):
	def __init__(self):
		self.filename = 'wikipop.csv'

	def open_spider(self, spider):
		self.file = open(self.filename, 'w')
		line = ','.join(['name','state','pop2017','pop2010']) + '\n'
		self.file.write(line)

	def close_spider(self, spider):
		self.file.close()

	def process_item(self, item, spider):
		line = ','.join(item.values()) + '\n'
		self.file.write(line)
		return item
