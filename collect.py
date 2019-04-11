import os
import importlib
from datetime import datetime
import json

# Find all scrapers in scrapers-dir
# Scraper has to have:
# - get_deals method
# - get_deals has to return list of dicts containing
# - { 'title', 'price', 'link'}
scrapers = [name for name in os.listdir('scrapers') if name.endswith('.py')]
now = datetime.now()
total_deals = []
for name in scrapers:
    scr = name.replace('.py','')
    unit = importlib.import_module('scrapers.{0}'.format(scr))
    deals = unit.get_deals()

    # Map a timestamp on each deal
    for item in deals:
        item.update({'timestamp': now.strftime('%Y-%m-%d')})

    print("\n Collected {0} deals for {1} \n\n".format(len(deals), scr))

    total_deals += deals

# @TODO store the results somewhere.
datadir = os.path.join(os.getcwd(), 'data')
filename = '{0}_resultset.json'.format(now.strftime('%Y%m%d_%H%I%S'))

fh = open(os.path.join(datadir, filename), 'w+')
fh.write(json.dumps(total_deals))
fh.close()
