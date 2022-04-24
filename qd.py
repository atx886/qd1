
from selenium import webdriver

  

options = webdriver.FirefoxOptions()
# options.set_headless(True)
options.add_argument("--headless")  # 设置火狐为headless无界面模式
options.add_argument("--disable-gpu")
d = webdriver.Firefox(options=options)


# d = webdriver.Firefox()

d.implicitly_wait(5)
def rw():
    time.sleep(1)


def dl(phone):
    d.get('https://www.chaojijishi.com/h5/#/pages/login/login?from=user')
    d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[5]/uni-view[1]/uni-input/div/input').send_keys(
        phone)
    rw()
    d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[5]/uni-view[2]/uni-input/div/input').send_keys(
        123456)
    rw()
    d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[5]/uni-view[3]/uni-view[1]/uni-view').click()
    rw()
    d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[5]/uni-view[5]/uni-view/uni-view').click()
    rw()
    d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[5]/uni-view[4]').click()
    rw()
    d.get('https://www.chaojijishi.com/h5/#/pages/subpack1/set/user-id-card-data?type=1')
dl(17000651668)
