import unittest

from daily_douban.spider import Spider

class TestSpider(unittest.TestCase):
    def test_update_sitemap(self):
        self.spider = Spider()
        updates = self.spider.get_update_xmls()
        print(updates)
        self.assertTrue(1)
        self.spider.get_new_review()

        
if __name__ == '__main__':
    unittest.main()