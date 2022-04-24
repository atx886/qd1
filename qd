from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # 和上面WebDriverWait一起用的
from selenium.webdriver.support.wait import WebDriverWait


def html_selenium_firefox(url):
    """
    依据 url 应用 selenium 获取网页源码
    :param url: url
    :return: 网页源码
    """
    opt = webdriver.FirefoxOptions()
    # 设置无界面
    opt.add_argument("--headless")
    # 禁用 gpu
    opt.add_argument('--disable-gpu')
    # 指定 firefox 的装置门路，如果配置了环境变量则不需指定
    firefox_binary = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"
    # 指定 geckodirver 的装置门路，如果配置了环境变量则不需指定
    executable_path = "E:\\Downloads/geckodriver\\geckodriver.exe"
    driver = webdriver.Firefox(firefox_binary=firefox_binary, executable_path=executable_path, options=opt)
    # 发送申请
    driver.get(url)
    # 显式期待：显式地期待某个元素被加载
    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'article-content')))
    wait.until(EC.presence_of_element_located((By.TAG_NAME, 'span')))
    # 获取网页源码
    html = driver.page_source
    # 敞开浏览器开释资源
    driver.quit()
    return html


def get_news_content(url):
    html = html_selenium_firefox(url)
    tree = etree.HTML(html)
    title = tree.xpath('//div[@class="article-content"]/h1/text()')[0]
    # xpath 查找没有 class 的元素：span[not(@class)]
    pubtime = tree.xpath('//div[@class="article-meta mt-4"]/span[not(@class)]/text()')[0]
    # xpath 查找 class="name" 的元素：span[@class="name"]
    source = tree.xpath('//div[@class="article-meta mt-4"]/span[@class="name"]/a/text()')[0]
    # xpath 某个标签中的所有元素：//div
    content = tree.xpath('//article')[0]
    # 解决 content 乱码问题
    content = str(etree.tostring(content, encoding='utf-8', method='html'), 'utf-8')
    # 提取 content 中所有图片的地址
    images = etree.HTML(content).xpath('//img/@src')

    result = {
        "title": title,
        "pubtime": pubtime,
        "source": source,
        "content": content,
        "images": images,
    }
    return result


if __name__ == '__main__':
    url = "https://www.toutiao.com/a6969138023774667264/"
    result = get_news_content(url)
    print(result)
