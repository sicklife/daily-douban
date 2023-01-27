# encoding=utf-8
# created by 李际朝@istarshine.com
# created at 23/1/27  22:57:54
import requests


class Downloader:
    def __init__(self, *args, **kwargs):
        self.session = requests.Session()
        headers = kwargs.get("headers")
        if headers and isinstance(headers, dict):
            self.session.headers = headers

    def download(self,url,  method="get"):
        return self.session.request(method=method, url=url)


class WgetDownloader(Downloader):
    def __init__(self, *args, **kwargs):
        headers = {"user-agent": "Wget/1.20.3 (linux-gnu)"}
        kwargs.update({"headers": headers})
        super().__init__(*args, **kwargs)
