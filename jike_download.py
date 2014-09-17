#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'liuzhijun'
import requests
import re
import bs4
import urllib2

import os, errno

COOKIES = {"PHPSESSID": "m72srkjdm5cfedp7ssg74k4395",
           "SCHOOL_IS_FROM_CONNECT": "czowOiIiOw%3D%3D",
           "SCHOOL_SS__CURRENT": "czoxOiIxIjs%3D",
           "sso_temp_uid": "20140913121549-113-103-88-156",
           "_ga": "GA1.2.1416692351.1410526796",
           "sso_eoe_auth": "65deHqNxAGMcb6zyBVdMBRf3DwbzOH5UlYvtWbZnOjQJdBMkmnd8SR%2FYPzvwgyWke9brghtm469JbuakSmrMwtyf%2FOr7lXA7FLBzsaEVwUjpA7L90CzTDdo34GqVwg",
           "sso_uid": "2610044",
           "sso_code": "KNIWDE",
           "sso_uname": "lzjun",
           "sso_uhash": "97855291b3d97f860766ffd352ce19e5"}


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise

def main2():
    home_url = "http://android.jikexueyuan.com/"
    response = requests.get(home_url)
    soup = bs4.BeautifulSoup(response.text)
    study_path_list = soup.find_all(class_="ue-studyPath-list-box")
    # 创建章节目录

    jike = []

    for sp in study_path_list:
        greens = sp.find_all(class_="green")
        name = ' '.join([green.string for green in greens])

        video_list = sp.find_all(class_="ue-video-list-box")
        for video in video_list:
            video_name = video.find(class_='ue-video-show-name').string
            video_path = name + "/" + video_name.replace(u"、", '_').replace(":", '_')
            print video_path
            video_url = video.a.get('href')
            jike.append((video_path, video_url))

    return jike


def download(video_save_path, video_url):
    mkdir_p(video_save_path)
    response = requests.get(video_url, cookies=COOKIES)
    ss = bs4.BeautifulSoup(response.text)
    courses = ss.find_all(class_='ue-player-courseDir-name-l')
    for course in courses:
        a = course.find("a")
        link = a.get('href')
        r = requests.get(link, cookies=COOKIES)
        name = get_keyword_from_text(r.text, "bdText : '([\s\S]*?)'")
        src = get_keyword_from_text(r.text, '<source src="([\s\S]*?\.mp4)"')
        print src
        f = urllib2.urlopen(src)
        with open(video_save_path + '/' + name + '.mp4', 'wb') as code:
            code.write(f.read())


def main():

    url2 = "http://www.jikexueyuan.com/study/9/lid/1.html"
    cookies = {"PHPSESSID": "m72srkjdm5cfedp7ssg74k4395",
               "SCHOOL_IS_FROM_CONNECT": "czowOiIiOw%3D%3D",
               "SCHOOL_SS__CURRENT": "czoxOiIxIjs%3D",
               "sso_temp_uid": "20140913121549-113-103-88-156",
               "_ga": "GA1.2.1416692351.1410526796",
               "sso_eoe_auth": "65deHqNxAGMcb6zyBVdMBRf3DwbzOH5UlYvtWbZnOjQJdBMkmnd8SR%2FYPzvwgyWke9brghtm469JbuakSmrMwtyf%2FOr7lXA7FLBzsaEVwUjpA7L90CzTDdo34GqVwg",
               "sso_uid": "2610044",
               "sso_code": "KNIWDE",
               "sso_uname": "lzjun",
               "sso_uhash": "97855291b3d97f860766ffd352ce19e5"}
    response = requests.get(url2, cookies=cookies)

    print get_keyword_from_text(response.text, "bdText : '([\s\S]*?)'")
    print get_keyword_from_text(response.text, '<source src="([\s\S]*?\.mp4)"')


def get_keyword_from_text(text, regex):
    """
    根据正则表达式从文本中获取关键字
    提取的关键字是在正则表达式中括号对，因此必须提供一个分组

    参数regex支持字符串和列表类型，返回与之对应的字符串或列表
    """
    if isinstance(regex, basestring):
        p = re.compile(regex, re.IGNORECASE)
        m = p.search(text)
        if m:
            # raise tornado.gen.Return(m.group(1))
            return m.group(1)
    elif isinstance(regex, list):
        rtn = []
        for r in regex:
            p = re.compile(r, re.IGNORECASE)
            m = p.search(text)
            rtn.append(m.group(1)) if m else rtn.append('')
        return rtn


import urllib2
import gevent
from gevent.queue import JoinableQueue
from gevent import monkey

monkey.patch_all()
tasks = JoinableQueue()


if __name__ == "__main__":
    srcs = main2()
    srcs = [src for src in srcs if src[0].startswith(u"第3阶段")]
    jobs = []
    for src in srcs:
        jobs.append(gevent.spawn(download, src[0], src[1]))
    gevent.joinall(jobs)
    # a = u"你"+":"
    # print a
    # a = u"你"
    # with open('xx', 'w') as f:
    # f.write(a)

    # video_url = 'http://cv1.jikexueyuan.com/201409131549/6f9f105eba412a97d39ee6d82f49801d/android/course_surface_view_game/01/video/c104b_06_h264_sd_960_540.mp4'
    # f = urllib2.urlopen(video_url)
    # with open('xx.mp4', 'wb') as code:
    #     code.write(f.read())