#coding=utf-8

import os
import unittest
import sys
sys.path.append(r"D:\code\appium_python\testcase")
sys.path.append(r"D:\code\appium_python\testcase\public")

from selenium import webdriver
import public
from time import sleep



PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class Acfun(unittest.TestCase):
    def setUp(self):
        SYSTEM_VERSION = 4.2
        

        if SYSTEM_VERSION != 4.2:
            # 4.1启动变量
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['version'] = '4.1'
            #华为c8813d手机序号
            desired_caps['deviceName'] = 'EC233DA70E2F'
            desired_caps['automationName'] = 'selendroid'
            desired_caps['app'] = r'D:\code\app\acfun_2.5.7.0.apk'
            desired_caps['appPackage'] = 'tv.acfundanmaku.video'
            desired_caps['appActivity'] = 'tv.acfundanmaku.video.entity.activity.SplashActivity'

            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            print 'app start ok'
            # 做个延时，减少报错几率
            sleep(5)

        else:
            # 4.2启动变量
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

            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

            print 'app start ok'

            # 做个延时，不然会报错
            sleep(5)
    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        u"""app登陆用例"""
        public.login(self.driver)
        # el = self.driver.find_element_by_id('tv.acfundanmaku.video:id/main_pager_tab_more')
        el = self.driver.find_element_by_id('tv.acfundanmaku.video:id/main_pager_tab_more')
        print el.text
        self.assertEqual(u'更多', el.text)

    def test_search(self):
        u"""app搜索用例"""
        public.search(self.driver,'1217843')
    
    def test_homepage_pd(self):
        u"""app频道元素用例"""
        pd = self.driver.find_element_by_id('tv.acfundanmaku.video:id/main_pager_tab_home')
        print pd.text
        self.assertEqual(u'频道', pd.text)
    
    def test_homepage_ph(self):
        u'''app排行点击用例'''
        ph = self.driver.find_element_by_id('tv.acfundanmaku.video:id/main_pager_tab_rank')
        ph.click()
        el = self.driver.find_element_by_id('tv.acfundanmaku.video:id/rank_popup')
        sleep(2)
        self.assertIsNotNone(el)
    
    def test_homepage_zj(self):
        u''' app追剧点击用例'''
        zj = self.driver.find_element_by_id('tv.acfundanmaku.video:id/main_pager_tab_drama')
        zj.click()
        sleep(2)
        el = self.driver.find_element_by_id('tv.acfundanmaku.video:id/weekly_popup')
        self.assertIsNotNone(el)

if __name__ == '__main__':
    unittest.main()






