import scrapy
from ..items import QuotetutorialItem

class QuoteSpider(scrapy.Spider):
    name ='quotes'
    start_urls=[
        'https://quotes.toscrape.com/'
    ]

    def parse(seft,response):
        #title=response.css('title::text').extract()
        #yield{'titletext':title}
        items=QuotetutorialItem()


        all_div_quotes=response.css('div.quote')
        for quote in all_div_quotes:
            title= quote.css('span.text::text').extract()
            author= quote.css('.author::text').extract()
            tag=quote.css('.tag::text').extract()

            items['title']=title
            items['author']=author
            items['tag']=tag

            yield items

        #next_page=response.css('li.next a::attr(href)').get()
        next_page = response.xpath('//*[@class="next"]/a/@href').get()

        if next_page is not  None:
            yield response.follow(next_page, callback= self.parse ) 

# scrapy shell "https://quotes.toscrape.com/"
# response.xpath("//title/text()").extract() 
# response.xpath("//span[@class='text']/text()").extract() // dung "" thi ben trong "" phai la ''
# response.css("li.next a").xpath("@href").extract()
# response.css("a").xpath("@href").extract()
# scrapy crawl  quotes -o items.csv //json xml