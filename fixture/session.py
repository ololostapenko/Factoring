__author__ = 'olga.ostapenko'


class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_css_selector("input.ant-input").click()
        wd.find_element_by_css_selector("input.ant-input").clear()
        wd.find_element_by_css_selector("input.ant-input").send_keys(username)
        wd.find_element_by_id("app-container").click()
        wd.find_element_by_xpath("//div[@id='app-container']/form/div[2]/div/div/span/span/input").click()
        wd.find_element_by_xpath("//div[@id='app-container']/form/div[2]/div/div/span/span/input").clear()
        wd.find_element_by_xpath("//div[@id='app-container']/form/div[2]/div/div/span/span/input").send_keys(password)
        wd.find_element_by_css_selector("body").click()
        wd.find_element_by_xpath("//div[@id='app-container']//button[.='Sign in']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@class='ant-layout-sider-children']//span[.='Logout']").click()