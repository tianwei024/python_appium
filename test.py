#coding=utf-8

import os

import sys
from appium import webdriver
# from selenium import webdriver
# from selenium.webdriver.common.touch_actions import TouchActions

from time import sleep
sys.path.append(r"D:\code\python_appium\testcase")
sys.path.append(r"D:\code\python_appium\testcase\public")


#启动模拟器
# script.emulator_start()
# sleep(60)

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
#4.1启动变量
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['version'] = '4.2'
desired_caps['deviceName'] = 'LG-V500-09f861ba1755a97f'
desired_caps['automationName'] = 'selendroid'
desired_caps['app'] = r'D:\code\app\acfun_2.5.7.0.apk'
desired_caps['appPackage'] = 'tv.acfundanmaku.video'
desired_caps['appActivity'] = 'tv.acfundanmaku.video.entity.activity.SplashActivity'

# desired_caps['platformName'] = 'selendroid'
# desired_caps['platformVersion'] = '4.2'
# desired_caps['device'] = 'selendroid'
# desired_caps['deviceName'] = 'EC233DA70E2F'
# desired_caps['app'] = r'D:\code\app\acfun_v2.5.6.0_43_build20140610_beta.apk'

# desired_caps['appPackage'] = 'tv.acufndanmaku.video'
# desired_caps['appActivity'] = 'tv.acfundanmaku.video.entity.activity.SplashActivity'
# #真机序列号
# # desired_caps['uuid'] = 'LG-V500-09f861ba1755a97f'
# #desired_caps['uuid'] = 'EC233DA70E2F'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

print 'app start ok'

# 做个延时，不然会报错
sleep(5)








#查找clickable是true，scrollable是false的节点
# el = driver.find_elements_by_android_uiautomator('new UiSelector().clickable(true).scrollable(false)')
# el = driver.find_element_by_id('tv.acfundanmaku.video:id/thumbnail_content')

# driver.swipe(30,171,192,500,1)
# action = TouchAction()
# action.press(None,x=108,y=276).move_to(None,x=117,y=184).release().perform()
# action.press(None,x=108,y=276).move_to(None,x=117,y=184).release()

# action.press(None,x=66,y=306)
# js_snippet = "mobile: swipe"
# args = {'startX':108, 'startY':276, 'startX':117, 'startY':184, 'tapCount':1, 'duration':10}
# driver.execute_script(js_snippet, args)

# pages = driver.find_element_by_id("tv.acfundanmaku.video:id/home_channel")
# touch_actions = TouchActions(driver)              
# # touch_actions.flick_element(pages,0,-600,0).perform()
# touch_actions.flick_element(pages,-300,0,0).perform()


# el =  driver.find_element_by_id('tv.acfundanmaku.video:id/home_channel')
# el.click()
# homepage.dht_click(driver)

# homepage.dht_click(driver)
# homepage.yl_random_click(driver)

#动画查看更多
# public.swipe_screen_down(driver, 'tv.acfundanmaku.video:id/home_channel',y=-367)
# sleep(2)

# el = driver.find_element_by_id('tv.acfundanmaku.video:id/home_channel')
# el.click()
# driver.find_element_by_id('tv.acfundanmaku.video:id/home_cover' + str(random.randint(1,4))).click()
# print '2 ok'

# el = driver.find_elements_by_name('查看更多')
# print len(el)

# homepage.yys_click(driver)
# homepage.yy_random_click(driver)

#音乐
# public.swipe_screen_down(driver,'tv.acfundanmaku.video:id/home_channel',y=-367)
# sleep(5)

# el = driver.find_element_by_id('tv.acfundanmaku.video:id/home_channel')
# el.click()

# driver.find_element_by_id('tv.acfundanmaku.video:id/home_cover' + str(random.randint(1,4))).click()
# homepage.yy_random_click(driver)

#影视
# public.swipe_screen_down(driver,'tv.acfundanmaku.video:id/home_channel',y=-430)
# sleep(5)
# el = driver.find_element_by_id('tv.acfundanmaku.video:id/home_channel')
# el.click()
# driver.find_element_by_id('tv.acfundanmaku.video:id/home_cover' + str(random.randint(1,4))).click()

# 体育
# public.swipe_screen_down(driver,'tv.acfundanmaku.video:id/home_channel',y=-501)
# sleep(5)
# el = driver.find_element_by_id('tv.acfundanmaku.video:id/home_channel')
# el.click()

# driver.find_element_by_id('tv.acfundanmaku.video:id/home_cover' + str(random.randint(1,4))).click()
# homepage.tys_click(driver)

#科技
# public.swipe_screen_down(driver,'tv.acfundanmaku.video:id/home_channel',y=-563)
# sleep(5)
# el = driver.find_element_by_id('tv.acfundanmaku.video:id/home_channel')
# el.click()
# homepage.kjs_click(driver)

# homepage.kj_random_click(driver)

# public.login(driver)
#
# sleep(10)
# el = driver.find_element_by_id("tv.acfundanmaku.video:id/main_pager_tab_rank")
# print "el ok"
# sleep(2)
#
# print el
# print el.text

el = driver.find_element_by_id('tv.acfundanmaku.video:id/main_pager_tab_more')
# el = driver.find_element_by_name(u'更多')
el.click()

# self.assertEqual(u'更多', el.text)




print 'script ok'