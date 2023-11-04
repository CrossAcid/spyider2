# https://tieba.baidu.com/f?kw=python&ie=utf-8&pn=50
# https://tieba.baidu.com/f?kw=python&ie=utf-8&pn=0


from urllib import request, parse
import time
import random
from utils.ua_info import ua_list #使用自定义的ua池

class TiebaSpider:

    def __init__(self):
        self.url = 'https://tieba.baidu.com/f?{}'

    def get_html(self, url):
        req = request.Request(url=url, headers={'User-Agent': random.choice(ua_list)})
        res = request.urlopen(req)
        html = res.read().decode("gbk", "ignore")
        return html

    def parse_html(self):
        pass

    def save_html(self, filename, html):
        with open(filename, 'w') as f:
            f.write(html)

    def run(self):
        name = input('输入贴吧名：')
        begin = int(input('输入起始页：'))
        stop = int(input('输入终止页：'))

        for page in range(begin, stop + 1):
            pn = (page - 1) * 50
            params = {
                'kw': name,
                'pn': str(pn)
            }
            # 拼接URL地址
            params = parse.urlencode(params)
            url = self.url.format(params)
            # 发请求
            html = self.get_html(url)
            # 定义路径
            filename = '{}-{}页.html'.format(name, page)
            self.save_html(filename, html)
            # 提示
            print('第%d页抓取成功' % page)
            # 每爬取一个页面随机休眠1-2秒钟的时间
            time.sleep(random.randint(1, 2))


if __name__ == "__main__":
    start = time.time()
    spider = TiebaSpider()
    spider.run()
    end = time.time()
    print('执行时间:%.2f'%(end - start))


