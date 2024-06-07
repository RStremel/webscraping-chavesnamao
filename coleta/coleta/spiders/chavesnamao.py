import scrapy


class ChavesnamaoSpider(scrapy.Spider):
    name = "chavesnamao"
    allowed_domains = ["www.chavesnamao.com.br"]
    start_urls = ["https://www.chavesnamao.com.br/apartamentos-para-alugar/sp-sao-paulo/consolacao/2-quartos/"]

    def parse(self, response):
        pass
