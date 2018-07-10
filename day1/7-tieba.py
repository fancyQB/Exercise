

def build_url(url, page, tname):
    #拼接url
    page = oafe

def main():
    start_page = int(input('请输入起始页码:'))
    end_page = int(input('请输入结束页码:'))
    tname = input('请输入贴吧名:')
    url = 'http://tieba.baidu.com/f?&ie=utf-8&'
    for page in range(start_page, end_page+1):
        req = build_url(url, page, tname)
        download(req, page)

if __name__ == '__main__':
    main()