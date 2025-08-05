# import sys
# sys.path.insert(0, "/home/jachymhodek/Coding/NeuroScout/src")
#
# from neuroscout.database.db import SessionLocal, OtevrenaVedaOpportunity, init_db
#
# def print_all_opportunities():
#     session = SessionLocal()
#     try:
#         opportunities = session.query(OtevrenaVedaOpportunity).all()
#         if not opportunities:
#             print("Database is empty.")
#         for opp in opportunities:
#             # Remove SQLAlchemy internal attributes
#             opp_data = {key: value for key, value in vars(opp).items() if not key.startswith('_')}
#             print(opp_data)
#     finally:
#         session.close()
#
# if __name__ == "__main__":
#     init_db()  # Ensure the database and table exist
#     print_all_opportunities()

""""
#Running this script will print out the contents of your SQLite database.# filepath: /home/jachymhodek/Coding/NeuroScout/debug.py
import sys
sys.path.insert(0, "/home/jachymhodek/Coding/NeuroScout/src")

from neuroscout.database.db import SessionLocal, OtevrenaVedaOpportunity, init_db

def print_all_opportunities():
    session = SessionLocal()
    try:
        opportunities = session.query(OtevrenaVedaOpportunity).all()
        if not opportunities:
            print("Database is empty.")
        for opp in opportunities:
            # Remove SQLAlchemy internal attributes
            opp_data = {key: value for key, value in vars(opp).items() if not key.startswith('_')}
            print(opp_data)
    finally:
        session.close()

if __name__ == "__main__":
    init_db()  # Ensure the database and table exist
    print_all_opportunities()

#Running this script will print out the contents
"""

import sys
sys.path.insert(0, "/home/jachymhodek/Coding/NeuroScout/src")

from scrapy.crawler import CrawlerProcess
from scrapy import signals
from neuroscout.scraper.spiders.orevrenaveda import OtevrenaVedaSpider

# Container to collect items
collected_items = []

def item_scraped(item, response, spider):
    collected_items.append(item)

if __name__ == "__main__":
    process = CrawlerProcess(settings={
        "LOG_ENABLED": False,  # Disable Scrapy logs
    })

    # Connect the signal to collect each scraped item
    crawler = process.create_crawler(OtevrenaVedaSpider)
    crawler.signals.connect(item_scraped, signal=signals.item_scraped)
    process.crawl(crawler)

    # Start crawling
    process.crawl(OtevrenaVedaSpider)
    process.start()  # Blocks until crawling is finished

    # Print out the pure dictionary items
    for item in collected_items:
        print(item)