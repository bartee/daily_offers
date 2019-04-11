
from sheets_data_client import DataClient
from pprint import pprint as pp
from datetime import datetime

# Next up: Google Sheets connection, or a simple vue-frontend?
# - (/) Connect to Sheet.
# - (/) Find the "Filter" sheet, collect the keywords from the A-column
# - (/) Filter the total_deals on given keywords, and store in filtered_deals dictionary.
#           filtered_deals['filter term'] = [deals matching the filter on title]
#
# - (/) Append the current datetime to each filtered list item
# - Store the filtered items in a separate sheet.


filtered_deals = {}
client = DataClient()
now = datetime.now()

total_deals = []

filterlist = client.get_filter_values()

counter = 0
for filter_term in filterlist:
    filtered = [deal for deal in total_deals if filter_term.lower() in deal['title'].lower()]
    map(lambda item: item.update({'timestamp': now.strftime('%Y-%m-%d')}), filtered)

    filtered_deals.update({filter_term: filtered})
    pp(total_deals)
    counter += len(filtered)

pp(filtered_deals)
