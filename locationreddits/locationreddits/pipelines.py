# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class LocationredditsPipeline(object):

	def __init__(self):
		self.filename = 'locationreddits.txt'

	def open_spider(self, spider):
		self.file = open(self.filename, 'w')

	def close_spider(self, spider):
		self.file.close()

	def process_item(self, item, spider):
		line = ','.join(item.values()) + '\n'
		self.file.write(line)
		return item
