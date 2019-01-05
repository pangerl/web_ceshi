# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re

class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("https://edu.codeaha.com/school")
        driver.find_element_by_link_text(u"进入啊哈教室").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='下一步'])[1]/following::img[3]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='完成'])[1]/following::input[1]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | xpath=(.//*[normalize-space(text()) and normalize-space(.)='完成'])[1]/following::input[1] | ]]
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='完成'])[1]/following::input[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='完成'])[1]/following::input[1]").clear()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='完成'])[1]/following::input[1]").send_keys("cqteacher1")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='完成'])[1]/following::input[2]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | xpath=(.//*[normalize-space(text()) and normalize-space(.)='完成'])[1]/following::input[2] | ]]
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='完成'])[1]/following::input[2]").clear()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='完成'])[1]/following::input[2]").send_keys("cqteacher")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='完成'])[1]/following::button[1]").click()
        driver.find_element_by_link_text(u"进入啊哈教室").click()
        # driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='设置'])[1]/preceding::div[1]").click()
        driver.find_element_by_class_name('dropdown-toggle').click()
        time.sleep(1)
        # ActionChains(driver).click(driver.find_element_by_id("teacher_nav_btn_logout")).perform() 
        driver.find_element_by_id("teacher_nav_btn_logout").click()
        # js2 = "var q=document.getElementById('teacher_nav_btn_logout').click()"
        # driver.execute_script(js2)
        mouse = driver.find_element_by_xpath("//div[@id='app-navbar-collapse']/ul[2]/li[2]//div[@class='ivu-dropdown-rel']")
        ActionChains(driver).move_to_element(mouse).perform()
        driver.find_element_by_link_text(u"退出登录").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
