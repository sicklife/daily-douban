import datetime
import gzip
import os
import pickle
import urllib.parse

import requests
import re

from . import settings


class Spider:
    def __init__(self):
        self.session = requests.session()
        self.session.headers = {"User-Agent": "daily-douban spider"}
        self.update_time = self.update_xmls = None
        self.reviews = []
        self._cache_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),  "db")
        self._cache_name = os.path.join(os.path.dirname(os.path.abspath(__file__)),  "db/.db_review.pkl")
        if os.path.isfile(self._cache_name):
            _local_cache = pickle.load(open(self._cache_name, 'rb'))
            self.update_time = _local_cache['update_time']
            self.reviews = _local_cache['reviews']

        pass

    def get_update_xmls(self):
        update_xmls_text = self.session.get(settings.douban_update_sitemap).text

        update_xmls = []
        # 获取更新时间
        for line in update_xmls_text.split('\n'):
            line = line.strip()
            if line.startswith("<lastmod>"):
                update_time = re.split("[<>]", line)[2]
                self.update_time = datetime.datetime.strptime(update_time, "%Y-%m-%dT%H:%M:%SZ")
                print(update_time)
                break
        for line in update_xmls_text.split('\n'):
            line = line.strip()
            if line.startswith("<loc>"):
                update_xml = re.split("[<>]", line)[2]
                update_xmls.append(update_xml)
        
        self.update_xmls = update_xmls
    
    def get_new_review(self, only_book=True, max_num=10, multi_thread=False):
        if self.update_xmls:
            self.reviews = []
            for u in self.update_xmls:
                print(u)
                content = self.session.get(u).content
                # print(content)
                c = gzip.decompress(content)
                file_name = urllib.parse.urlsplit(u).path[1:]
                c = c.decode()
                with open(os.path.join(self._cache_dir, file_name[:-3]), 'w', encoding='utf-8') as f:
                    f.write(c)
                reviews = []
                for line in c.split("\n"):
                    re_s = re.search("https://book.douban.com/review/\d+/", line)
                    if re_s:
                        # print(re_s.group())
                        reviews.append(re_s.group())
                self.reviews.extend(reviews)
                # print(reviews[-10:])
                if not reviews:
                    break
        self._save_cache()

    def _save_cache(self):
        cache = {
            "update_time": self.update_time,
            "reviews": self.reviews,
        }
        pickle.dump(cache, open(self._cache_name, 'wb'))

    def show(self):
        html_file = os.path.join(self._cache_dir, ".reviews.html")
        with open(html_file, 'w', encoding="utf-8") as f:
            f.write("""
            <html>
            <body>
            """)

            for review in self.reviews:
                f.write(f"<h3><a href=\"{review}\">{review}</a></h3>")

            f.write("""
            </body>
            </html>
            """)

        import subprocess
        # TODO 这里要做多平台的适配。
        subprocess.run(['open', str(html_file)])







 
