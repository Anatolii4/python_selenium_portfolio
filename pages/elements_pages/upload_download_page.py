import base64
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage

import random
from random import randint


class UploadDownloadPage(BasePage):
    __URL = "https://demoqa.com/upload-download"
    __UPLOAD_FILE = (By.CSS_SELECTOR, "#uploadFile")
    __UPLOADED_FILE_PATH = (By.CSS_SELECTOR, "#uploadedFilePath")
    __DOWNLOAD_FILE = (By.CSS_SELECTOR, "a[id=downloadButton]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_page(self):
        super()._open(self.__URL)

    def upload_file(self, path: str):
        super()._find(self.__UPLOAD_FILE).send_keys(path)

    def actual_uploaded_path(self) -> str:
        return super()._get_text(self.__UPLOADED_FILE_PATH)

    def remove_generated_file(self, path: str):
        os.remove(path)

    def download_file(self):
        link = super()._find(self.__DOWNLOAD_FILE).get_attribute("href")
        link_b = base64.b64decode(link)
        path_new_image = rf"C:\Users\48788\PycharmProjects\python_selenium_portfolio\generated_file\{random.randint(0, 999)}.jpeg"
        with open(path_new_image, "wb+") as f:
            offset = link_b.find(b'\xff\xd8')
            f.write(link_b[offset:])
        assert os.path.exists(path_new_image), "the file has not been downloaded"
        os.remove(path_new_image)