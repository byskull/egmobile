#-*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


myid = ''
mypwd = ''

# selenium 로 브라우저에 접속
options = webdriver.FirefoxOptions()
options.headless = True	
browser = webdriver.Firefox(options=options)

browser.get("https://www.egmobile.co.kr/member/login")

elem = browser.find_element_by_xpath("//input[@id='userid']")
elem.send_keys( myid )

elem = browser.find_element_by_xpath("//input[@id='password']")
elem.send_keys( mypwd + Keys.RETURN)

browser.find_element_by_xpath("//*[@id='flogin']/fieldset/div[2]/button").click()

browser.get("https://www.egmobile.co.kr/mypage/cost_time")
	
elem = browser.find_element_by_xpath("//div[@class='scroll_wrap']")

print(elem.text)

browser.quit()

a = input()
