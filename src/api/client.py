import requests


class MaximoClient:

    def __init__(self, server):

        self.server = server.rstrip("/")

        self.session = requests.Session()

        self.connected = False

    def get(self, url):

        return self.session.get(url)

    def post(self, url, data):

        return self.session.post(url, data=data)