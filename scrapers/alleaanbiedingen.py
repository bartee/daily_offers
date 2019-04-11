from requests import get
import bs4

def get_deals():

	deals = []

	url = 'https://alleaanbiedingen.info'
	# Paginated. To be fixed.
	response = get(url)

	htmlsoup = bs4.BeautifulSoup(response.text, 'html.parser')
	deal_containers = htmlsoup.find_all(class_ = 'widget deal')

	paginated_pages = htmlsoup.find_all('li', class_="page-item")
	max_pages = int(paginated_pages[len(paginated_pages)-2].a.text)

	for deal_container in deal_containers:
	    title = deal_container.find('h6', class_='deal-title').text
	    price = deal_container.find('h5', class_='float-right').text
	    link = deal_container.find('a', class_='more-info').get('href')

	    deal = {'title': title, 'price': price, 'link': '{0}{1}'.format(url,link)}
	    deals.append(deal)

	return deals
