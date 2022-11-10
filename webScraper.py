from userInput import USER_NOVELS, CHROMEDRIVER_PATH
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

SYOSETU_ORIGIN = 'https://ncode.syosetu.com'
PIXIV_ORIGIN = 'https://www.pixiv.net'

options = Options()
options.headless = True

service = Service(executable_path=CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)


def syosetuScrape(novels):
	"""Process the last line in a table which contains the last updated chapter of a given novel.

	novels -- array containing the string routes for novels
	"""
	for novel in novels:
		driver.get(SYOSETU_ORIGIN + novel)
		title = driver.title
		lastUpdateLink = driver.find_elements(by=By.CLASS_NAME, value='novel_sublist2')[-1]
		lastUpdateLink = lastUpdateLink.find_element(by=By.TAG_NAME, value='dd').find_element(by=By.TAG_NAME, value='a')
		chapterName = lastUpdateLink.text.strip()
		chapterLink = lastUpdateLink.get_attribute('href')
		print('Novel: ' + title)
		print('Check out chapter ' + chapterName + ' at ' + chapterLink)

	driver.quit()

def pixivScrape(novels):
	for novel in novels:
		driver.get(PIXIV_ORIGIN + novel)

syosetuScrape([novel['route'] for novel in USER_NOVELS if novel['origin'] == SYOSETU_ORIGIN])
#pixivScrape([novel['route'] for novel in USER_NOVELS if novel['origin'] == PIXIV_ORIGIN])