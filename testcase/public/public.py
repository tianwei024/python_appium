#coding=utf-8
from time import sleep 

#登陆
def login(driver):
	#点击更多按键
	el = driver.find_element_by_id('tv.acfundanmaku.video:id/main_pager_tab_more')
	# el = driver.find_element_by_name(u'更多')
	el.click()

	sleep(3)
	#点击登陆
	dl_page = driver.find_element_by_id('tv.acfundanmaku.video:id/more_user')
	dl_page.click()

	#账号
	zh = driver.find_element_by_id('tv.acfundanmaku.video:id/authorize_account')
	sleep(2)
	zh.send_keys("tianwei024")


	sleep(3)
	#密码
	mm = driver.find_element_by_id('tv.acfundanmaku.video:id/authorize_password')
	mm.send_keys('tw19840324!!')

	#点击登陆
	dl = driver.find_element_by_id('tv.acfundanmaku.video:id/authorize_login')
	dl.click()

#搜索
def search(driver,name):
	ss = driver.find_element_by_name(u'搜索')
	ss.click()

	el = driver.find_element_by_id('tv.acfundanmaku.video:id/post_input')
	el.send_keys(name)
	sleep(2)
	driver.find_element_by_id('tv.acfundanmaku.video:id/post_send').click()
	sleep(2)

# 划动
#direction 参数：element_id参照对象，x偏移量，y偏移量，speed划动速度
def swipe_screen_down(driver,element_id,x=0,y=-300,speed=0):
	from selenium import webdriver
	from selenium.webdriver.common.touch_actions import TouchActions
	pages = driver.find_element_by_id(element_id)
	touch_actions = TouchActions(driver)              
	touch_actions.flick_element(pages,x,y,speed).perform()


def random():
	import random
	return random.randint(1,4)

