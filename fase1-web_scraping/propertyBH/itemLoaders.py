from email.policy import default
from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose, TakeFirst
from propertyBH.dataClean import clean


class propertyItemLoader(ItemLoader):

    default_output_processor = TakeFirst()
    price_in = MapCompose(lambda x: clean.price(x))
    area_m2_in = MapCompose(lambda x: clean.general(x))
    bedrooms_in = MapCompose(lambda x: clean.general(x))
    suites_in = MapCompose(lambda x: clean.suite(x))
    vacancies_in = MapCompose(lambda x: clean.general(x))
    bathrooms_in = MapCompose(lambda x: clean.general(x))
    neighborhoods_in = MapCompose(lambda x: clean.neighborhoods(x))
    description_in = MapCompose(lambda x: x.strip())