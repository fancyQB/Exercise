import json
import urllib.parse
import urllib.request

from bs4 import BeautifulSoup


class QianChen(object):
    def __init__(self, url, keyword, start_page, end_page):
        super(QianChen, self).__init__()
        self.url = url
        self.keyword = keyword
        self.start_page = start_page
        self.end_page = end_page
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0'
        }
        self.items = []
     #下载信息
    def down_data(self, req):

        res = urllib.request.urlopen(req)

        #构建bs对象
        bs = BeautifulSoup(res.read(), 'lxml')
        info_list = bs.select('#resultList .el')[1:]
        for table in info_list:
            item = {}

            zwm = table.select('p a')[0].get_text()
            gsmc = table.select('.t2 > a')[0].get_text()
            gzdd = table.select('.t3')[0].get_text()
            xz = table.select('.t4')[0].get_text()
            fbrq = table.select('.t5')[0].get_text()
            item['zwm'] = zwm.strip()
            item['gsmc'] = gsmc
            item['gzdd'] = gzdd
            item['xz'] = xz
            item['fbrq'] = fbrq

            self.items.append(item)

        json_str = json.dumps(self.items, ensure_ascii=False)

        with open('info.json', 'w', encoding='utf-8') as fw:
            fw.write(json_str)
        # print(json_str)

    #拼接url，并构建请求对象返回
    def build_url(self, page):
        data = {
            'keyword': self.keyword,
            'page': str(page)
        }
        url = self.url + urllib.parse.quote(data['keyword']) + ',2,' +data['page']+'.html'
        req = urllib.request.Request(url=url, headers=self.headers)
        return req


    #对外提供的接口函数
    def start(self):
        for page in range(self.start_page, self.end_page+1):
            req = self.build_url(page)
            self.down_data(req)









def main():
    url = 'https://search.51job.com/list/040000,000000,0000,00,9,99,'
    keyword = input('请输入工作岗位:')
    start_page = int(input('请输入开始页码:'))
    end_page = int(input('请输入结束页码'))
    qianchen = QianChen(url, keyword, start_page, end_page)
    qianchen.start()

if __name__ == '__main__':
    main()