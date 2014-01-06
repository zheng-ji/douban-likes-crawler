# -*- coding:utf-8 -*-
import os
import urllib2
import HTMLParser

from BeautifulSoup import BeautifulSoup

def get_like_urls(user_name):
    url = "http://www.douban.com/people/" + user_name + "/likes"
    response = urllib2.urlopen(url)
    soup = BeautifulSoup(response.read())
    items = soup.findAll(name="div", attrs={"class": "fav-main"})
    return [item.h3.a["href"] for item in items]


def get_notes(user_name, note_urls):
    for url in note_urls:
        if url.find("note") == -1:
            continue

        try:
            response = urllib2.urlopen(url)
        except urllib2.HTTPError as e:
            print e.geturl() + " " + str(e)
            continue

        soup = BeautifulSoup(response.read())
        header = soup.findAll(name="div", attrs={"class": "note-header"})

        if not header:
            header = soup.findAll(name="div", attrs={"class": "note-hd"})
            date_str = soup.findAll(name="span", attrs={"class": "datetime"})[0].string
        else:
            date_str = header[0].span.string

        post = soup.findAll(name="div", attrs={"id": "link-report"})[0]
        body = post.renderContents().replace("<br />", "\n")

        title = header[0].h1.string
        content_escaped = "\n\n".join([str(title), str(date_str), body])
        content = HTMLParser.HTMLParser().unescape(content_escaped.decode("utf-8"))

        dst_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "tmp", user_name)
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        dst_file = open(os.path.join(dst_dir, title + ".txt"), 'w')
        dst_file.write(content.encode("utf-8"))
        dst_file.close()


if __name__ == "__main__":
    # usrnames = ["ruitao", "loviselu", "laiyonghao", "fenng"]
    usr_names = ["litten"]
    for name in usr_names:
        like_urls = get_like_urls(name)
        get_notes(name, like_urls)
