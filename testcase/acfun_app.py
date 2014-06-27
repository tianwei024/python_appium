#coding=utf-8

import os
import unittest
import sys
sys.path.append(r"D:\code\appium_python\testcase")
sys.path.append(r"D:\code\appium_python\testcase\public")

from selenium import webdriver
import public
from time import sleep
import homepage



PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class Acfun(unittest.TestCase):
    def setUp(self):
        SYSTEM_VERSION = 4.1
        

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

    def test_random_click(self):
        u'''app娱乐随机点击用例'''
        homepage.yl_random_click(self.driver)
        el = self.driver.find_element_by_id('tv.acfundanmaku.video:id/content_video_info_stows_add')
        self.assertIsNotNone(el)

    def test_sc(self):
        u'''app收藏测试用例'''
        #登陆
        public.login(self.driver)
        #返回到频道
        homepage.pd_click(self.driver)
        #随机点击娱乐栏目
        homepage.yl_random_click(self.driver)
        #点击收藏
        homepage.play_sc(self.driver).click()
        #查找以已收藏元素
        el = self.driver.find_element_by_id('tv.acfundanmaku.video:id/content_video_info_stows_remove')
        self.assertIsNotNone(el)




    def test_pl(self):
        u'''app评论测试用例'''
        #登陆
        public.login(self.driver)
        #返回到频道
        homepage.pd_click(self.driver)
        #随机点击娱乐栏目
        homepage.yl_random_click(self.driver)
        #点击评论进入评论界面
        homepage.play_pl(self.driver).click()
        #点击右上角评论按钮发布评论
        self.driver.find_element_by_name('评论').click()
        #输入评论内容
        el = self.driver.find_element_by_id('tv.acfundanmaku.video:id/post_input')
        el.send_keys('thanks ok!')
        #点击发送
        self.driver.find_element_by_name(u'发送').click()
        #等页面自动跳转
        sleep(2)
        #断言 评论跳转后页面的评论元素是否为空
        self.assertIsNotNone('homepage.pl_pl(self.driver)')


    #有元素定位不到，后面在完成用例
    def test_px(self):
        u'''app排序测试用例'''
        #点击娱乐栏目查看更多
        homepage.yls_click(self.driver)
        #点击右上角排序
        homepage.px(self.driver)

    #文章收藏
    def test_wzsc(self):
        u'''app文章收藏测试用例'''
        #登陆
        public.login(self.driver)
        #返回到排行
        homepage.ph_click(self.driver)
        #点击排行按钮
        self.driver.find_element_by_id('tv.acfundanmaku.video:id/rank_popup').click()
        sleep(2)
        #选文章排行
        el = self.driver.find_elements_by_class_name('android.widget.LinearLayout')
        el[8].click()
        sleep(2)
        #点击文章
        ele = self.driver.find_elements_by_class_name('android.widget.LinearLayout')
        ele[0].click()
        #收藏
        homepage.wz_sc(self.driver).click()
        sleep(2)
        # #断言 收藏成功判断已收藏元素是否为空
        el = self.driver.find_element_by_name(u'取消收藏')
        # el[0] = self.driver.find_elements_by_class_name('android.widget.TextView')
        self.assertIsNotNone(el)



    def test_wzpl(self):
        u'''app文章评论测试用例'''
        #登陆
        public.login(self.driver)
        #返回到排行
        homepage.ph_click(self.driver)
        #点击排行按钮
        self.driver.find_element_by_id('tv.acfundanmaku.video:id/rank_popup').click()
        sleep(2)
        #选文章排行
        el = self.driver.find_elements_by_class_name('android.widget.LinearLayout')
        el[8].click()
        sleep(2)
        #点击文章
        ele = self.driver.find_elements_by_class_name('android.widget.LinearLayout')
        ele[0].click()
        #文章评论
        homepage.wz_pl(self.driver).click()
        #点击评论

        self.driver.find_element_by_name(u'评论').click()
        #输入评论
        self.driver.find_element_by_id('tv.acfundanmaku.video:id/post_input').send_keys('thinks ok!')
        self.driver.find_element_by_name(u'发送').click()
        sleep(2)
        el = self.driver.find_element_by_name(u'评论')
        self.assertIsNotNone(el)


    def test_wzmhms(self):
        u'''app文章漫画模式测试用例'''
        #登陆
        public.login(self.driver)
        #返回到排行
        homepage.ph_click(self.driver)
        #点击排行按钮
        self.driver.find_element_by_id('tv.acfundanmaku.video:id/rank_popup').click()
        sleep(2)
        #选文章排行
        el = self.driver.find_elements_by_class_name('android.widget.LinearLayout')
        el[8].click()
        sleep(2)
        #点击文章
        ele = self.driver.find_elements_by_class_name('android.widget.LinearLayout')
        ele[0].click()
        #点击漫画模式
        homepage.wz_mhms(self.driver).click()
        sleep(2)
        #断言 判断漫画模式变为文章模式按键是否为空
        el = self.driver.find_element_by_id('tv.acfundanmaku.video:id/content_article_info_comic_articlemode')
        self.assertIsNotNone(el)


if __name__ == '__main__':
    unittest.main()






