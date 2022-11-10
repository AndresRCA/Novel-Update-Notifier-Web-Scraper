from userInput import USER_NOVELS
from bs4 import BeautifulSoup
import requests

SYOSETU_ORIGIN = 'https://ncode.syosetu.com'
PIXIV_ORIGIN = 'https://www.pixiv.net'

def syosetuScrape(novels):
	fakeUserAgentHeader = {
		'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'
	}

	for novel in novels:
		page = requests.get(SYOSETU_ORIGIN + novel, headers=fakeUserAgentHeader) # 403 error (for some reason forbidden)
		if page.status_code != 200:
			print("couldn't establish a connection with " + SYOSETU_ORIGIN)
			break
		
		soup = BeautifulSoup(page.content, 'html.parser')

def pixivScrape(novels):
	for novel in novels:
		page = requests.get(PIXIV_ORIGIN + novel) # 403 error (for some reason forbidden)
		if page.status_code != 200:
			print("couldn't establish a connection with " + PIXIV_ORIGIN)
			break
		
		soup = BeautifulSoup(page.text, 'lxml')

syosetuScrape([novel['route'] for novel in USER_NOVELS if novel['origin'] == SYOSETU_ORIGIN])
pixivScrape([novel['route'] for novel in USER_NOVELS if novel['origin'] == PIXIV_ORIGIN])