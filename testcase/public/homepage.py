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
    # el = driver.find_elements_by_class_name('android.widget.RadioButton')
    # el[1].click()

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

#随机点击科技
def kj_random_click(driver):
	public.swipe_screen_down(driver,'tv.acfundanmaku.video:id/home_channel',y=-561)
	sleep(5)
	driver.find_element_by_id('tv.acfundanmaku.video:id/home_cover' + str(random.randint(1,4))).click()


#视频播放页面收藏元素
def play_sc(driver):
    el = driver.find_element_by_id('tv.acfundanmaku.video:id/content_video_info_stows_add')
    return el

#视频播放页面评论元素
def play_pl(driver):
    el = driver.find_element_by_id('tv.acfundanmaku.video:id/content_video_info_comment')
    return el

#视频播放页面视频播放元素
def play_sp(driver):
    el = driver.find_element_by_id('tv.acfundanmaku.video:id/content_video_info_title')
    return el

#评论页面的评论元素
def pl_pl(driver):
    el = driver.find_element_by_name(u'评论')
    return el

#各页面排序按钮元素
def px(driver):
    el = driver.find_element_by_name(u'排序')
    return el


#文章页面漫画模式元素
def wz_mhms(driver):
    el = driver.find_element_by_id('tv.acfundanmaku.video:id/content_article_info_comicmode')
    return el

#文章页面评论元素
def wz_pl(driver):
    el = driver.find_element_by_id('tv.acfundanmaku.video:id/content_article_info_comment')
    return el

#文章页面收藏元素
def wz_sc(driver):
    el =driver.find_element_by_name(u'添加收藏')
    return el

#文章页面分享文章元素
def wz_fx(driver):
    el = driver.find_element_by_name(u'分享文章')
    return el



