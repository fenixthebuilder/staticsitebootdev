from bs4 import BeautifulSoup as scraper

html = ''

#soup = scraper(html, 'html.parser')


def get_h1_from_html(html):
	soup = scraper(html, 'html.parser')
	h1_finder = soup.find('h1')
	
	if h1_finder is None:
		return ""
	
	return h1_finder.get_text()


def get_first_paragraph_from_html(html):
	soup = scraper(html, 'html.parser')
	p_finder = soup.find('p')

	if p_finder is None:
		return ""

	return p_finder.get_text()

