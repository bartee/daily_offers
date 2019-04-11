import os
import importlib
from sheets_data_client import DataClient
from datetime import datetime
from pprint import pprint as pp

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

# WORKS!

# Next up: Google Sheets connection
# - (/) Connect to Sheet.
# - (/) Find the "Filter" sheet, collect the keywords from the A-column
# - (/) Filter the total_deals on given keywords, and store in filtered_deals dictionary. filtered_deals['filter term'] = [deals matching the filter on title]
# - (/) Append the current datetime to each filtered list item
# - Store the filtered items in a separate sheet.
"""
filtered_deals = {}
client = DataClient()

filterlist = client.get_filter_values()


counter = 0
for filter_term in filterlist:
    filtered = [deal for deal in total_deals if filter_term.lower() in deal['title'].lower()]
    map(lambda item: item.update({'timestamp': now.strftime('%Y-%m-%d')}), filtered)

    filtered_deals.update({filter_term: filtered})
    pp(total_deals)
    counter += len(filtered)

pp(filtered_deals)
"""
