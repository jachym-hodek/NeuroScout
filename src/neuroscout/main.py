import sys
from scraper.spiders.orevrenaveda import OtevrenaVedaSpider
from scrapy.crawler import CrawlerProcess
from scrapy import signals
from database.db import SessionLocal, OtevrenaVedaOpportunity, init_db



# Container to collect items
collected_items = []

def item_scraped(item, response, spider):
    collected_items.append(item)

if __name__ == "__main__":
    # Initialize the database and table
    init_db()

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

    # After crawling, store items in the database
    session = SessionLocal()
    try:
        for item in collected_items:
            opportunity = OtevrenaVedaOpportunity(**item)
            session.add(opportunity)
        session.commit()
        print(f"Inserted {len(collected_items)} opportunities into the database.")
    except Exception as e:
        session.rollback()
        print("An error occurred:", e)
    finally:
        session.close()