import unittest

from daily_douban.spider import Spider


class TestSpider(unittest.TestCase):

    def setUp(self) -> None:
        self.spider = Spider()

    @unittest.skip("tmp skip")
    def test_update_sitemap(self):
        updates = self.spider.get_update_xmls()
        print(updates)
        self.assertTrue(1)
        self.spider.get_new_review()

    # @unittest.skip("tmp skip")
    def test_open_html(self):
        self.spider.show()

        
if __name__ == '__main__':
    unittest.main()