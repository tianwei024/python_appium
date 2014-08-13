# coding=utf-8

def login(driver, username=None, password=None):
    els = driver.find_elements_by_class_name("android.widget.TextView")

    # 点击进入更多频道
    els[3].click()

    # 点击登陆
    driver.find_element_by_id('tv.acfun.animation:id/signin_text').click()


    # 输入用户名
    username = 'tianwei024'
    driver.find_element_by_id('tv.acfun.animation:id/username_edit').send_keys(username)

    # 输入密码
    password = 'tw19840324!!'
    driver.find_element_by_id('tv.acfun.animation:id/password_edit').send_keys(password)

    # 点击登陆
    driver.find_element_by_id('tv.acfun.animation:id/signin_text').click()


class recommend_page(object):
    def __init__(self):
        self.top_picture = None
        self.driver = None

    def set_top_picture(self, driver, id='tv.acfun.animation:id/stick_image0'):
        return driver.find_element_by_id(id)



