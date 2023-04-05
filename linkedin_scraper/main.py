from linkedin_api import Linkedin
import json
from linkedin_custom_search import LinkedinCustomSearch
from processor import Processor
from scraper import Scraper, ScraperConfig2
from dotenv import dotenv_values

file = open("datatry.json", "w")
config = dotenv_values(".env")
EMAIL=config['EMAIL']
USRNAME=config['USRNAME']
api = Linkedin(EMAIL,USRNAME)

processor = Processor()
searcher = LinkedinCustomSearch(api)
scraper = Scraper(searcher, processor, ScraperConfig2())

res = scraper.fetch_job_descriptions_by_scraping_plan()
final = json.dumps(res)
file.write(final)
file.close()


"""
 - addattare la job search al pagination plan
 - usare pagination plan per parallelizzare le richieste
 - fare le richiesta in base alla location
 - criterio di parallelizzazione customizzabile: parallelizza per paginazione, parallelizza per nazione
 - limite 
 - evade
 - parametrizzare per backfilling, creare cli
 - come funziona listed at per backfilling
 - scraped date
"""
