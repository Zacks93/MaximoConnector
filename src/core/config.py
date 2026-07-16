import configparser
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

CONFIG_FILE = BASE_DIR / "config.ini"


class Config:

    def __init__(self):

        self.config = configparser.ConfigParser()

        self.config.read(CONFIG_FILE)

    @property
    def server(self):
        return self.config["MAXIMO"]["SERVER"]

    @property
    def username(self):
        return self.config["MAXIMO"]["USERNAME"]

    @property
    def password(self):
        return self.config["MAXIMO"]["PASSWORD"]

    @property
    def page_size(self):
        return int(self.config["MAXIMO"]["PAGE_SIZE"])