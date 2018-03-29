__author__ = 'olga.ostapenko'

from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.invoice import InvoiceHelper


class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.invoice = InvoiceHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://app.factoring.testit.lt/")

    def destroy(self):
        self.wd.quit()
