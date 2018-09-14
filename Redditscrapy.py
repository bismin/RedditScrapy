# -*- coding: utf-8 -*-
import scrapy


class RedditscrapySpider(scrapy.Spider):
    name = 'Redditscrapy'
    allowed_domains = ['reddit.com/r/programming']
    start_urls = ["https://www.reddit.com/r/programming/",
    			  "http://reddit.com/r/python",]

    def parse(self, response):
    	jobs =response.xpath('//div[@class="s1bh7rp0-0 cJDENw s12udrmv-0 ljTnwX"]/div/div/div')
    	for job in jobs:
		        title =job.xpath('div[@class="_1poyrkZ7g36PawDueRza-J s1wkwgow-7 iewpIB"]/article[@class="s1wkwgow-0 eSaXox"]/div[@class="s1wkwgow-2 jeuFCV"]/div[@class="s1wkwgow-3 jTUsRG"]/span[@class="y8HYJ-y_lTUHkQIc1mdCq"]/a[@class="SQnoC3ObvgnGjWt90zD9Z"]/h2[@class="pd8yw6-0 dZOwqG"]/text() | div[@class="_1poyrkZ7g36PawDueRza-J _11R7M_VOgKO1RJyRSRErT3"]/div[@class="_3wiKjmhpIpoTE2r5KCm2o6 pd8yw6-1 bYvOLl"]/span[@class="y8HYJ-y_lTUHkQIc1mdCq"]/a[@class="SQnoC3ObvgnGjWt90zD9Z"]/h2[@class="pd8yw6-0 dZOwqG"]/text()').extract_first()
		        link=job.xpath('div[@class="_1poyrkZ7g36PawDueRza-J s1wkwgow-7 iewpIB"]/article[@class="s1wkwgow-0 eSaXox"]/div[@class="s1wkwgow-2 jeuFCV"]/div[@class="s1wkwgow-3 jTUsRG"]/span[@class="y8HYJ-y_lTUHkQIc1mdCq"]/a[@class="SQnoC3ObvgnGjWt90zD9Z"]/@href | div[@class="_1poyrkZ7g36PawDueRza-J _11R7M_VOgKO1RJyRSRErT3"]/div[@class="_3wiKjmhpIpoTE2r5KCm2o6 pd8yw6-1 bYvOLl"]/span[@class="y8HYJ-y_lTUHkQIc1mdCq"]/a[@class="SQnoC3ObvgnGjWt90zD9Z"]/@href').extract_first()
		        username=job.xpath('div[@class="_1poyrkZ7g36PawDueRza-J s1wkwgow-7 iewpIB"]/article[@class="s1wkwgow-0 eSaXox"]/div[@class="s1wkwgow-2 jeuFCV"]/div[@class="r1fz0-0 eRGyhr"]/div[@class="cZPZhMe-UCZ8htPodMyJ5"]/div[@class="_3AStxql1mQsrZuUIFP9xSg nU4Je7n-eSXStTBAPMYt8"]/div[@class="wx076j-0 hPglCh"]/a[@class="_2tbHP6ZydRpjI44J3syuqC s1461iz-1 gWXVVu"]/text() | div[@class="_1poyrkZ7g36PawDueRza-J _11R7M_VOgKO1RJyRSRErT3"]/div[@class="r1fz0-0 fVnYQE"]/div[@class="cZPZhMe-UCZ8htPodMyJ5"]/div[@class="_3AStxql1mQsrZuUIFP9xSg nU4Je7n-eSXStTBAPMYt8"]/div[@class="wx076j-0 hPglCh"]/a[@class="_2tbHP6ZydRpjI44J3syuqC s1461iz-1 gWXVVu"]/text()').extract_first()
		        user_url=job.xpath('div[@class="_1poyrkZ7g36PawDueRza-J s1wkwgow-7 iewpIB"]/article[@class="s1wkwgow-0 eSaXox"]/div[@class="s1wkwgow-2 jeuFCV"]/div[@class="r1fz0-0 eRGyhr"]/div[@class="cZPZhMe-UCZ8htPodMyJ5"]/div[@class="_3AStxql1mQsrZuUIFP9xSg nU4Je7n-eSXStTBAPMYt8"]/div[@class="wx076j-0 hPglCh"]/a[@class="_2tbHP6ZydRpjI44J3syuqC s1461iz-1 gWXVVu"]/@href | div[@class="_1poyrkZ7g36PawDueRza-J _11R7M_VOgKO1RJyRSRErT3"]/div[@class="r1fz0-0 fVnYQE"]/div[@class="cZPZhMe-UCZ8htPodMyJ5"]/div[@class="_3AStxql1mQsrZuUIFP9xSg nU4Je7n-eSXStTBAPMYt8"]/div[@class="wx076j-0 hPglCh"]/a[@class="_2tbHP6ZydRpjI44J3syuqC s1461iz-1 gWXVVu"]/@href').extract_first()
		        score=job.xpath('div[@class="_23h0-EcaBUorIHC-JZyh6J"]/div[@class="s7z12f0-0 iHQyRe"]/div[@class="_1rZYMD_4xY3gRcSS3p8ODO"]/text()').extract_first()
		        time=job.xpath('div[@class="_1poyrkZ7g36PawDueRza-J s1wkwgow-7 iewpIB"]/article[@class="s1wkwgow-0 eSaXox"]/div[@class="s1wkwgow-2 jeuFCV"]/div[@class="r1fz0-0 eRGyhr"]/div[@class="cZPZhMe-UCZ8htPodMyJ5"]/div[@class="_3AStxql1mQsrZuUIFP9xSg nU4Je7n-eSXStTBAPMYt8"]/a[@data-click-id="timestamp"]/text() | div[@class="_1poyrkZ7g36PawDueRza-J _11R7M_VOgKO1RJyRSRErT3"]/div[@class="r1fz0-0 fVnYQE"]/div[@class="cZPZhMe-UCZ8htPodMyJ5"]/div[@class="_3AStxql1mQsrZuUIFP9xSg nU4Je7n-eSXStTBAPMYt8"]/a[@class="_3jOxDPIQ0KaOWpzvSQo-1s"]/text()').extract_first()
		        yield{'title':title,'link':link,'username':username,'user_url':user_url,'score':score,'time':time}
 