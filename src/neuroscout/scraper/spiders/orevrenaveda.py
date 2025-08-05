# optimised to scrape the website of Otevřená věda (https://www.otevrenaveda.cz/)

import scrapy

class OtevrenaVedaSpider(scrapy.Spider):
    name = "otevrenaveda"
    allowed_domains = ["otevrenaveda.cz"]
    start_urls = [
        "https://www.otevrenaveda.cz/cs/staze-pro-studenty/"
    ]

    def parse(self, response):
        for opportunity in response.css("div.staz-blok"):
            yield {
                "city": opportunity.css("div.categories span::text").get(),
                "field": opportunity.css("div.categories span+span::text").get(),
                "title": opportunity.css("h3.xx136::text").get(),
                "mentor": opportunity.css("div.tags div:nth-child(1) span:nth-child(2)::text").get(),
                "institution": opportunity.css("div.tags div:nth-child(2) a::text").get(),
                "duration": opportunity.css("div.tags div:nth-child(3) span:nth-child(2)::text").get(),
                "hours_per_month": opportunity.css("div.tags div:nth-child(4) span:nth-child(2)::text").get(),
                "time_details": opportunity.css("div.tags div:nth-child(5) span:nth-child(2)::text").get(),
                "location": opportunity.css("div.tags div:nth-child(6) span:nth-child(2)::text").get(),
                "description": opportunity.css("div.annotation::text").get(),
                "student": opportunity.css("div.tags ~ div.tags span:nth-child(2)::text").get(),
            }
        next_page = response.css('a.next.page-numbers::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

