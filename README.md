[![Build Status](https://api.travis-ci.org/bartee/daily_offers.svg?branch=master)](https://travis-ci.org/bartee/daily_offers)
[![Coverage Status](https://coveralls.io/repos/github/bartee/daily_offers/badge.svg?branch=master)](https://coveralls.io/github/bartee/daily_offers?branch=master)

Aim 1:
- scrape a shitload of sites
- store the offer in a standardized form:
    - title
    - price
    - url
- store the output in a google spreadsheet

Aim 2:
- Get a list of keywords to filter the title on
- filter the scraped resultset on the keyword
- store the found result per keyword in a separate sheet with the date appended to it
 

Plan du Pomodori:
- Scraper returns json with title, price and url by convention
- Scrapers in separate dir
- Connect to sheet for filter
