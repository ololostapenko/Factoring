__author__ = 'olga.ostapenko'

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InvoiceHelper:
    def __init__(self, app):
        self.app = app

    def create(self, invoice):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@class='ant-layout-sider-children']//div[.='Invoices']").click()
        wd.find_element_by_link_text("All invoices").click()
        wd.find_element_by_link_text("Create new").click()
        wd.find_element_by_css_selector("button.ant-btn.ant-btn-primary").click()
        wd.find_element_by_css_selector("input.ant-select-search__field").click()
        wd.find_element_by_css_selector("input.ant-select-search__field").clear()
        wd.find_element_by_css_selector("input.ant-select-search__field").send_keys(invoice.Customer)
        wd.find_element_by_css_selector("li.ant-select-dropdown-menu-item.ant-select-dropdown-menu-item-active").click()
        wd.find_element_by_xpath(
            "//div[@class='page-padding']/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/span/div/div/div/ul/li/div/input").click()
        wd.find_element_by_css_selector("li.ant-select-dropdown-menu-item.ant-select-dropdown-menu-item-active").click()
        wd.find_element_by_xpath(
            "//div[@class='page-padding']/div[1]/div[2]/div[1]/div[3]/div/div[2]/div/span/div/div/div/ul/li/div/input").click()
        wd.find_element_by_xpath(
            "//div[@class='page-padding']/div[1]/div[2]/div[1]/div[3]/div/div[2]/div/span/div/div/div/ul/li/div/input").clear()
        wd.find_element_by_xpath(
            "//div[@class='page-padding']/div[1]/div[2]/div[1]/div[3]/div/div[2]/div/span/div/div/div/ul/li/div/input").send_keys(
            invoice.Buyer)
        wd.find_element_by_css_selector("li.ant-select-dropdown-menu-item.ant-select-dropdown-menu-item-active").click()
        wd.find_element_by_id("document_no").click()
        wd.find_element_by_id("document_no").clear()
        wd.find_element_by_id("document_no").send_keys(invoice.Document_Number)
        wd.find_element_by_xpath("//div[@class='page-padding']/div[1]/div[2]/div[2]/div[3]/div/div[1]").click()
        wd.find_element_by_xpath("//span[@id='payment_due_to']/div/input").click()
        wd.find_element_by_xpath("//tbody[@class='ant-calendar-tbody']//div[.='29']").click()
        wd.find_element_by_id("price_total").click()
        wd.find_element_by_id("price_total").clear()
        wd.find_element_by_id("price_total").send_keys(invoice.Total_Value)
        wd.find_element_by_css_selector("button.ant-btn.ant-btn-primary").click()
        wd.find_element_by_link_text("sdxcfgvbhnm").click()