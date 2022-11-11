from userInput import USER_NOVELS, CHROMEDRIVER_PATH
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

SYOSETU_ORIGIN = 'https://ncode.syosetu.com'
PIXIV_ORIGIN = 'https://www.pixiv.net'

options = Options()
options.headless = True

service = Service(executable_path=CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)


def syosetuScrape(novels):
	"""Access the last updated chapter of a given novel.

	novels -- array containing the routes for novels
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

def pixivScrape(novels):
	"""Access the last updated chapter of a given novel.

	novels -- array containing the routes for novels
	"""
	for novel in novels:
		driver.get(PIXIV_ORIGIN + novel)
		# get novel title and author from <title></title> at the same time
		title = driver.title.split('/')
		novelTitle = title[0].strip('"')
		author = title[1].replace(' Series [pixiv]', '').strip('"')

		try:
			# the page is javascript heavy, so measures are needed to load before proceeding
			latestChapterLink = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div[3]/div/div/main/section/div[1]/div[2]/div[2]/div[4]/div/a')) # wait until element is found
			chapterLink = latestChapterLink.get_attribute('href')
			# go to link and check chapter
			driver.get(chapterLink)
			chapterName = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(by=By.XPATH, value='//*[@id="root"]/div[2]/div/div[3]/div/div/main/section/div[1]/div/div[2]/h1')).text
		except:
			print('Something went wrong')
			continue

		print('Novel: ' + novelTitle + ' by ' + author)
		print('Check out chapter ' + chapterName + ' at ' + chapterLink)
		
		

syosetuScrape([novel['route'] for novel in USER_NOVELS if novel['origin'] == SYOSETU_ORIGIN])
pixivScrape([novel['route'] for novel in USER_NOVELS if novel['origin'] == PIXIV_ORIGIN])
driver.quit()