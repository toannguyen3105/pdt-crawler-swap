import scrapy


class ItemsSpider(scrapy.Spider):
    name = 'items'
    allowed_domains = ['swap.gg']
    start_urls = ['https://api.swap.gg/prices/730']

    def parse(self, response):
        items = response.json()['result']
        for item in items:
            name = item['marketName']
            original_price = item['price']['value']
            price = original_price / 100
            have_stock = item['stock']['have']

            yield {
                'name': name,
                'price': price,
                'have_stock': have_stock
            }
