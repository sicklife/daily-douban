# encoding=utf-8
# author Jizhao.li 
# email: tubkninght@gmail.com
import datetime
from dataclasses import dataclass


@dataclass
class Book:
    """
    图书
    """
    name: str
    author: str
    press: str
    press_date: datetime.datetime
    price: float
    current: str = "元"  # 货币单位
    page_num: int = 0


@dataclass
class BookReview:
    """
    书评
    """
    title: str
    author: str
    publish_time: datetime.datetime
    content: str
    is_short_review: bool
    score: int
    book: Book
