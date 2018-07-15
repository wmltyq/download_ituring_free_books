from urllib import request
from lxml import etree
import os
import time

# 爬虫起始地址
start_url = 'http://www.ituring.com.cn/book?tab=free&sort=hot&page=0'
# 网站根地址，用于后面构造图书地址和下载地址
base_url = 'http://www.ituring.com.cn'
# 保存目录，可自行修改
save_dir = '图灵社区/'
# True: 表示网络状态良好，False: 表示请求出现问题
NETWORK_STATUS = True


# 获取页面 HTML 源码
def get_html(url):
    global NETWORK_STATUS
    req = request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
    try:
        resp = request.urlopen(url)
    except Exception as e:
        NETWORK_STATUS = False
    if NETWORK_STATUS == False:
        for count in range(1, 6):
            print('请求失败：第 %d 尝试重新发送请求' % count)
            try:
                resp = request.urlopen(url)
                NETWORK_STATUS = True
                break
            except Exception as e:
                pass
    html = etree.HTML(resp.read().decode('utf-8'))
    return html


# 获取当前分页的所有图书链接
def get_books_url(html):
    books_url = html.xpath('//h4[@class="name"]/a/@href')
    for book_url in books_url:
        book_url = base_url + book_url
        print('图书链接：' + book_url)
        html = get_html(book_url)
        # if html != None:
        download_books(html)
        # 不要爬取太快
        time.sleep(0.5)


# 下载图书
def download_books(html):
    a_tag = html.xpath('//a[contains(@id, "book-resources")]')
    if a_tag != []:
        href = a_tag[0].xpath('@href')[0]
        file_name = a_tag[0].xpath('text()')[0].strip().replace('\r\n', '')
        download_url = base_url + href
    else:
        print('下载链接：该电子刊不方便批量下载，请点击上方的图书链接手动下载\n')
        return
    print('下载链接：' + download_url)
    full_dir = save_dir + file_name
    # 如果存储目录下有该文件就无须下载了
    if os.path.exists(full_dir):
        print('下载状态：已下载\n')
    else:
        try:
            request.urlretrieve(download_url, full_dir)
            print('下载状态：成功\n')
        except Exception as e:
            print(e)
            print('下载状态：失败\n')


if __name__ == '__main__':
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    html = get_html(start_url)
    get_books_url(html)
    li = html.xpath('//li[contains(@class, "PagedList-skipToPage")]/a')
    for key, value in enumerate(li):
        # 跳过首页
        if key == 0:
            continue
        next_page = value.xpath('@href')[0]
        html = get_html(base_url + next_page)
        get_books_url(html)
