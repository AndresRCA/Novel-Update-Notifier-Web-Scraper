# Python based Web Scraper for novel update notifications

## Requirements

* Python Ver. 3.10.6
* The dependencies set in requirements.txt

## What does this app do

This app scrapes the websites (https://ncode.syosetu.com and https://www.pixiv.net) that contain the list of novels that the user is currently reading, when there's an update on what's the latest chapter a notification will be send by mail alerting the user.

In order for this web scraper to work, follow the next steps:

1. Rename userInput.example.py to userInput.py and set the values to your preference (the routes to the novels they read, their website, what email they want to receive the notifications from (your own personal email is fine too, or a SMTP Service Provider)).
2. Download the proper Chrome Driver for your version of Chrome, then place the executable at root of the app's folder

### Personal dev corner

Unexpected issues encountered and their solutions:

* BeautifulSoup's functions find() and find_all() returning empty: turns out the only reliable source is the "View page source" option in Chrome, not Inspect (in most cases the content is loaded after the user enters the page).
* Websites returning http code 403: by adjusting User-Agent in the headers you can fool the website into thinking you're an user rather than a web scraper.
* Changed BeautifulSoup to Selenium, which makes things a lot more manageable.