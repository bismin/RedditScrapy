# -*- coding: utf-8 -*-
import scrapy


class RedditscrapySpider(scrapy.Spider):
	name = 'Redditscrapy'
	allowed_domains = ['reddit.com/r/programming']
	start_urls = ["https://www.reddit.com/r/programming/",
				  "http://reddit.com/r/python",]

	def parse(self, response):
		jobs=response.xpath('//div[@class="s1bh7rp0-0 cJDENw s12udrmv-0 ljTnwX"]/div')
		for job in jobs:
				title =job.xpath('div//h2/text()').extract_first()
				link=job.xpath('div//a[h2]/@href').extract_first()
				username=job.xpath('div//a[starts-with(@href, "/user/")]/text()').extract_first()
				user_url=job.xpath('div//a[starts-with(@href, "/user/")]/text()').extract_first()
				score=job.xpath('div//button[@data-click-id="upvote"]/following-sibling::div/text()').extract_first()
				time=job.xpath('div//a[@data-click-id="timestamp"]/text()').extract_first()
				yield{'title':title,'link':link,'username':username,'user_url':user_url,'score':score,'time':time}