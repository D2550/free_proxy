import re
import threading
import requests


class scan(threading.Thread):
    def __init__(self, thread):
        threading.Thread.__init__(self)
        self.thread = thread

    def check_proxy(self, proxy):
        check_url = 'https://www.baidu.com'
        proxies = {
            'https': fr'http://{proxy}'
        }
        try:
            requests.get(url=check_url, proxies=proxies, timeout=3)
            print('success: ' + proxy)
        except requests.exceptions.ConnectionError:
            print('error')
        except requests.exceptions.ReadTimeout:
            print('timeout')
        except KeyboardInterrupt:
            print('用户退出')
            exit()
        except requests.exceptions.InvalidSchema:
            exit()

    def run(self):
        for k in proxy_list:
            self.check_proxy(k)


if __name__ == '__main__':
    print('start success')
    proxy_list = []
    for i in range(1, 5):
        url = 'https://ip.jiangxianli.com/?page=%s' % str(i)
        r = requests.get(url)
        pattern = re.compile(r'href="//(((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d?\d:.*)">)')
        m = pattern.findall(r.text)
        for j in range(0, len(m)):
            a = (m[j])[0].replace('">', '')
            proxy_list.append(a)
        print(proxy_list)
    threads = []
    thread_count = 10
    for i in range(thread_count):
        t = scan(i)
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
