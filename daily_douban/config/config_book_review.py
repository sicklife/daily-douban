# encoding=utf-8
# created by 李际朝@istarshine.com
# created 2023/1/28 15:36:20
import pprint

from bs4 import BeautifulSoup
from requests import Response

from config.config import Config
from db.models import BookReview


class BookReviewConfig(Config):
    def __init__(self):
        super().__init__()

    def parse(self, response: Response):
        dom = BeautifulSoup(response.text, features="lxml")
        pprint.pprint(response.text)
        reviews = dom.find_all("div")
        print(len(reviews))
        return
