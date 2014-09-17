import requests
from PIL import Image
from StringIO import StringIO

import gevent
from gevent.queue import JoinableQueue
from gevent import monkey

monkey.patch_all()
tasks = JoinableQueue()


def main(i):
    tpl = "http://uploadadult.com/i/2014/08/13/IMG_%s.jpg"
    for i in range(i * 100, i * 100 + 100):
        s = (str(i).zfill(4))
        url = tpl % s
        response = requests.get(url)
        print url, response.status_code
        if response.status_code == 200:
            image = Image.open(StringIO(response.content))
            image.save('%s.jpg' % s)


url = 'http://cl.man.lv/htm_data/16/1409/1212650.html'
import bs4


def test2():
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content)
    div = soup.find('div', class_="tpc_content")
    inputs = div.find_all("input")
    return [tag['src'] for tag in inputs]


def save_img(src):
    print src
    try:
        response = requests.get(src, timeout=100)
    except requests.exceptions.ConnectionError:
        response = requests.get(src, timeout=100)
    else:
        if response.status_code == 200:
            file_name = src.split('/')[-1]
            image = Image.open(StringIO(response.content))
            image.save('mt/%s.jpg' % file_name)


if __name__ == "__main__":
    srcs = test2()
    jobs = []
    for src in srcs:
        jobs.append(gevent.spawn(save_img, src))
    gevent.joinall(jobs)




