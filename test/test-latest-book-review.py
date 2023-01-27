import pprint
import unittest

from downloaders.downloader import WgetDownloader


class MyTestCase(unittest.TestCase):
    def test_something(self):
        downloader = WgetDownloader()

        latest_book_review_addr = "https://book.douban.com/review/latest/"
        latest_book_addr = "https://book.douban.com/latest/"
        for url in [latest_book_review_addr, latest_book_addr]:
            resp = downloader.download(url)
            print(resp.status_code)
            pprint.pprint(resp.text)
            self.assertEqual(resp.status_code, 200)  # add assertion here


if __name__ == '__main__':
    unittest.main()
