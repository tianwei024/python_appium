# coding=utf-8
'''
安卓动画自动化调试脚本
'''
import os

import sys
from appium import webdriver
from time import sleep
# from selenium import webdriver
# from selenium.webdriver.common.touch_actions import TouchActions
sys.path.append(r"D:\code\python_appium\testcase")
sys.path.append(r"D:\code\python_appium\testcase\public")
import homepage
import animation_public


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
desired_caps['version'] = '4.3'
desired_caps['deviceName'] = '192.168.56.101:5555'
desired_caps['automationName'] = 'selendroid'
desired_caps['app'] = r'D:\code\app\acfun-animation_android\beta\acfun_animation_v0.8.2.apk'
desired_caps['appPackage'] = 'tv.acfun.animation'
desired_caps['appActivity'] = 'tv.acfun.app.view.activity.SplashActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


print 'app start ok'

sleep(5)


els = driver.find_elements_by_class_name("android.widget.TextView")

# 点击进入分类频道
els[1].click()

# 搜索
driver.find_element_by_id('tv.acfun.animation:id/search_edit').send_keys('bl')
driver.find_element_by_id('tv.acfun.animation:id/search_image').click()

#进入动画剧
el = driver.find_elements_by_class_name('android.widget.LinearLayout')
print len(el)

el[0].click()

#缓存
driver.find_element_by_id('tv.acfun.animation:id/cache_image').click()

#选择下载缓存
hc = driver.find_element_by_id('tv.acfun.animation:id/video_text')

hc.click()

driver.find_element_by_id('tv.acfun.animation:id/ok_text').click()








