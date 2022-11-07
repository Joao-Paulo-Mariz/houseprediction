import scrapy
from propertyBH.items import propertyItem
from propertyBH.itemLoaders import propertyItemLoader

class propertySpider(scrapy.Spider):
    name = 'property_bh'
    start_urls = [f"https://loft.com.br/venda/imoveis/mg/belo-horizonte?typeRealState=imoveis&state=mg&city=belo-horizonte&pagina={i}" for i in range(1, 133)]

    custom_settings = {
        'DOWNLOAD_DELAY': 5
        }

    def parse(self, response):
        for link in response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "MuiGrid-grid-lg-3", " " ))]/a/@href'):
            yield response.follow(link.get(), callback=self.parse_properties)

    
    def parse_properties(self, response):
        
        properties = propertyItemLoader(item=propertyItem(), selector=response)

        properties.add_xpath('price', '//html/head/title/text()'),
        properties.add_xpath('area_m2', '//*[@id="__next"]/section/div[2]/div[1]/div[3]/div[2]/div[2]/p/text()'),
        properties.add_xpath('bedrooms','//*[@id="__next"]/section/div[2]/div[1]/div[3]/div[2]/div[3]/p/text()'),
        properties.add_xpath('suites', '//*[@id="__next"]/section/div[2]/div[1]/div[3]/div[2]/div[3]/p/span/text()'),
        properties.add_xpath('vacancies', '//*[@id="__next"]/section/div[2]/div[1]/div[3]/div[2]/div[4]/p/text()'),
        properties.add_xpath('bathrooms', '//*[@id="__next"]/section/div[2]/div[1]/div[3]/div[2]/div[5]/p/text()'),
        properties.add_xpath('neighborhoods', '//*[@id="location"]/header/div/h2/text()'),
        properties.add_xpath('description', '//*[@id="__next"]/section/div[2]/div[1]/div[1]/div/div/div[2]/h1/text()')
        
        yield properties.load_item()
