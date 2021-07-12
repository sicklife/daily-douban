import unittest

from daily_douban.spider import Spider

class TestSpider(unittest.TestCase):
    def test_update_sitemap(self):
        self.spider = Spider()
        self.spider.get_update_xmls()
        self.assertTrue(1)
        
if __name__ == '__main__':
    unittest.main()