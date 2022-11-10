from userInput import USER_NOVELS
from bs4 import BeautifulSoup
import requests

SYOSETU_ORIGIN = 'https://ncode.syosetu.com'
PIXIV_ORIGIN = 'https://www.pixiv.net'

def syosetuScrape(novels):
	return None

def pixivScrape(novels):
	return None

syosetuScrape([novel['route'] for novel in USER_NOVELS if novel['origin'] == SYOSETU_ORIGIN])
pixivScrape([novel['route'] for novel in USER_NOVELS if novel['origin'] == PIXIV_ORIGIN])