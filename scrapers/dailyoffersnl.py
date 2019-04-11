from requests import get
import bs4
import json


def get_deals():
	"""
	Get all deals from dailyoffers.nl

	"""
	deals = []

	url = 'https://www.dailyoffers.nl/solr/products/select/?facet.field=catId&facet.field=mainCatId&facet.field=shoId&wt=json&rows=10000000&facet=true&q=(active%3A1+AND+productType%3Adailydeal)+OR+(productType%3Aextradeal+AND+order_2%3A[1+TO+100000]+AND+startdate%3A[*+TO+NOW]+AND+enddate%3A[NOW+TO+*])&json.nl=map'

	response = get(url)
	json_resp = json.loads(response.text)

	for item in json_resp['response']['docs']:
	    title = item['title']
	    price = item['newprice']
	    shipping = item['shippingcosts']
	    url = 'https://www.dailyoffers.nl{}'.format(item['productUrl'])
	    deal = {'title': title, 'price': '{} ({} shipping)'.format(price, shipping), 'link': url}
	    deals.append(deal)

	return deals
