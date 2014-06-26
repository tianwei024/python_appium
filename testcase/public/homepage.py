#coding=utf-8
import random
import public
from time import sleep  	

#导航图点击
def dht_click(driver):
	el = driver.find_element_by_id('tv.acfundanmaku.video:id/thumbnail_content')
	el.click()

#频道点击
def pd_click(driver):
	pd = driver.find_element_by_id('tv.acfundanmaku.video:id/main_pager_tab_home')
	pd.click()

#排行点击
def ph_click(driver):
	ph = driver.find_element_by_id('tv.acfundanmaku.video:id/main_pager_tab_rank')
	ph.click()

#追剧点击
def zj_click(driver):
	zj = driver.find_element_by_id('tv.acfundanmaku.video:id/main_pager_tab_drama')
	zj.click()

#更多点击
def gd_click(driver):
	gd =  driver.find_element_by_id('tv.acfundanmaku.video:id/main_pager_tab_more')
	gd.click()

#娱乐查看更多点击
def yls_click(driver):
	el =  driver.find_element_by_id('tv.acfundanmaku.video:id/home_channel')
	el.click()


#随机点击娱乐
def yl_random_click(driver):
	el = driver.find_element_by_id('tv.acfundanmaku.video:id/home_cover' + str(random.randint(1,4)))
	el.click()


#动画查看更多点击
def dhs_click(driver):
	public.swipe_screen_down(driver, 'tv.acfundanmaku.video:id/home_channel',y=-243)
	sleep(5)

	el = driver.find_element_by_id('tv.acfundanmaku.video:id/home_channel')
	el.click()



#随机点击动画
def dh_random_click(driver):
	public.swipe_screen_down(driver, 'tv.acfundanmaku.video:id/home_channel',y=-243)
	sleep(5)
	driver.find_element_by_id('tv.acfundanmaku.video:id/home_cover' + str(random.randint(1,4))).click()


#游戏查看更多点击
def yxs_click(driver):
	public.swipe_screen_down(driver, 'tv.acfundanmaku.video:id/home_channel',y=-305)
	sleep(5)

	el = driver.find_element_by_id('tv.acfundanmaku.video:id/home_channel')
	el.click()

#随机点击游戏
def yx_random_click(driver):
	public.swipe_screen_down(driver, 'tv.acfundanmaku.video:id/home_channel',y=-305)
	sleep(5)
	driver.find_element_by_id('tv.acfundanmaku.video:id/home_cover' + str(random.randint(1,4))).click()

#音乐查看更多点击
def yys_click(driver):
	public.swipe_screen_down(driver,'tv.acfundanmaku.video:id/home_channel',y=-367)
	sleep(5)
	el = driver.find_element_by_id('tv.acfundanmaku.video:id/home_channel')
	el.click()

#随机点击音乐
def yy_random_click(driver):
	public.swipe_screen_down(driver,'tv.acfundanmaku.video:id/home_channel',y=-367)
	sleep(5)
	driver.find_element_by_id('tv.acfundanmaku.video:id/home_cover' + str(random.randint(1,4))).click()

#影视查看更多点击
def yss_click(driver):
	public.swipe_screen_down(driver,'tv.acfundanmaku.video:id/home_channel',y=-430)
	sleep(5)
	el = driver.find_element_by_id('tv.acfundanmaku.video:id/home_channel')
	el.click()

# 随机点击影视
def ys_random_click(driver):
	public.swipe_screen_down(driver,'tv.acfundanmaku.video:id/home_channel',y=-430)
	sleep(5)
	driver.find_element_by_id('tv.acfundanmaku.video:id/home_cover' + str(random.randint(1,4))).click()

#体育查看更多点击
def tys_click(driver):
	public.swipe_screen_down(driver,'tv.acfundanmaku.video:id/home_channel',y=-502)
	sleep(5)
	el = driver.find_element_by_id('tv.acfundanmaku.video:id/home_channel')
	el.click()

#随机点击体育
def ty_random_click(driver):
	public.swipe_screen_down(driver,'tv.acfundanmaku.video:id/home_channel',y=-501)
	sleep(5)
	driver.find_element_by_id('tv.acfundanmaku.video:id/home_cover' + str(random.randint(1,4))).click()

#科技查看更多点击
def kjs_click(driver):
	public.swipe_screen_down(driver,'tv.acfundanmaku.video:id/home_channel',y=-560)
	sleep(5)
	el = driver.find_element_by_id('tv.acfundanmaku.video:id/home_channel')
	el.click()

def kj_random_click(driver):
	public.swipe_screen_down(driver,'tv.acfundanmaku.video:id/home_channel',y=-561)
	sleep(5)
	driver.find_element_by_id('tv.acfundanmaku.video:id/home_cover' + str(random.randint(1,4))).click()


