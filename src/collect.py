from importlib.machinery import SourceFileLoader
import json
import os
from datetime import datetime

def get_scraper_list(scraper_dir):
    """
    Collect all scraper instances

    :return:
    """
    scraper_files = [name for name in os.listdir(scraper_dir) if name.endswith('.py')]
    scrapers = []
    for filename in scraper_files:
        scr = filename.replace('.py', '')
        scr_inst = SourceFileLoader(fullname=scr, path='{0}/{1}'.format(scraper_dir, filename)).load_module()
        if hasattr(scr_inst, "get_deals"):
            scrapers.append(scr_inst)

    return scrapers

def collect():
    """
    Find all scrapers in scrapers-dir
    Scraper has to have:
    - get_deals method
    - get_deals has to return list of dicts containing
    - { 'title', 'price', 'link'}

    :return:
    """
    datadir = 'data'
    if 'OUTPUT_DATA_DIR' in os.environ:
        datadir = os.environ['OUTPUT_DATA_DIR']

    scraper_dir = os.path.join(os.getcwd(), 'scrapers')
    scrapers = get_scraper_list(scraper_dir)
    now = datetime.now()
    total_deals = []
    for scr_instance in scrapers:
        deals = scr_instance.get_deals()

        # Map a timestamp on each deal
        for item in deals:
            item.update({'timestamp': now.strftime('%Y-%m-%d')})

        print("\n Collected {0} deals for {1} \n\n".format(len(deals), scr))

        total_deals += deals

    filename = '{0}_resultset.json'.format(now.strftime('%Y%m%d_%H%I%S'))

    fh = open(os.path.join(datadir, filename), 'w+')
    fh.write(json.dumps(total_deals))
    fh.close()

if __name__ == "__main__":
    collect()

