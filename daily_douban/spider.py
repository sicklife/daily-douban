import gzip
import os
import pickle

import requests
import re

from . import settings


class Spider:
    def __init__(self):
        self.session = requests.session()
        self.session.headers = {"User-Agent": "daily-douban spider"}
        self.reviews = self.update_time = None
        self._cache_name = ".db_review.pkl"
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
                self.update_time =
                break
        for line in update_xmls_text.split('\n'):
            line = line.strip()
            if line.startswith("<loc>"):
                update_xml = re.split("[<>]", line)[2]
                update_xmls.append(update_xml)
        
        self.updates = update_xmls
    
    def get_new_review(self, only_book=True, max_num=10, multi_thread=False):
        if self.updates:
            for u in self.updates:
                print(u)
                content = self.session.get(u).content
                # print(content)
                num = 0
                c = gzip.decompress(content)
                c = c.decode()
                for line in c.split("\n"):
                    if "review" in line and "book" in line:
                        print(line)
                        num += 1
                        if num > max_num:
                            break

        pass
        




 