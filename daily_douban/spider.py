import requests
import re

from . import settings

class Spider:
    def __init__(self):
        self.session = requests.session()
        self.session.headers = {"User-Agent": "daily-douban spider"}
        pass

    def get_update_xmls(self):
        update_xmls_text = self.session.get(settings.douban_update_sitemap).text

        update_xmls = []
        for line in update_xmls_text.split('\n'):
            line = line.strip()
            if line.startswith("<loc>"):
                update_xml = re.split("[<>]", line)[2]
                update_xmls.append(update_xml)
        
        return update_xmls
    
    def get_new_review(self, only_book=True, max_num=100, multi_thread=False):
        
        pass
        




 