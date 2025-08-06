# optimised to scrape the website of Otevřená věda (https://www.otevrenaveda.cz/)

import os
import json
import scrapy
import re


# Compute the project dir by moving 5 levels up from the current file
project_dir = os.path.dirname(
                os.path.dirname(
                os.path.dirname(
                os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))))))
config_path = os.path.join(project_dir, "config", "keyword_sets.json")

class OtevrenaVedaSpider(scrapy.Spider):
    name = "otevrenaveda"
    allowed_domains = ["otevrenaveda.cz"]
    start_urls = [
        "https://www.otevrenaveda.cz/cs/staze-pro-studenty/"
    ]

    # Initialize with a keyword set
    # Right now, the default is "neuro", but it can be changed to any other set defined in the config file
    def __init__(self, keyword_set="neuro", *args, **kwargs):
        super(OtevrenaVedaSpider, self).__init__(*args, **kwargs)
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)
        # Set keyword patterns from the chosen keyword set
        self.keyword_patterns = config.get(keyword_set, [])

    def parse(self, response):
        # Extract opportunities from the page
        # Each opportunity is contained in a div with class "staz-blok"
        for opportunity in response.css("div.staz-blok"):
            item = {
            "city": opportunity.css("div.categories span::text").get(),
            "field": opportunity.css("div.categories span+span::text").get(),
            "title": opportunity.css("h3[class^='xx']::text").get(),
            "mentor": opportunity.css("div.tags div:nth-child(1) span:nth-child(2)::text").get(),
            "institution": opportunity.css("div.tags div:nth-child(2) a::text").get(),
            "duration": opportunity.css("div.tags div:nth-child(3) span:nth-child(2)::text").get(),
            "hours_per_month": opportunity.css("div.tags div:nth-child(4) span:nth-child(2)::text").get(),
            "time_details": opportunity.css("div.tags div:nth-child(5) span:nth-child(2)::text").get(),
            "location": opportunity.css("div.tags div:nth-child(6) span:nth-child(2)::text").get(),
            "description": opportunity.css("div.annotation::text").get(),
            "student": opportunity.css("div.tags ~ div.tags span:nth-child(2)::text").get(),
        }
            # Skip items if title is empty or missing
            if not item.get("title"):
                continue
            
            # Combine selected fields for keyword search
            combined_text = " ".join([
                item.get("title") or "",
                item.get("field") or "",
                item.get("institution") or "",
                item.get("description") or "",
                item.get("location") or "",
            ])

            # Check if any keyword pattern matches the combined text
            if not any(re.search(pattern, combined_text, re.IGNORECASE) for pattern in self.keyword_patterns):
                continue
            
            # Yield the item to be processed by the pipeline
            yield item
        
        # Follow pagination links to the next page
        next_page = response.css("div.paginate a[title='Další stránka seznamu']::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

