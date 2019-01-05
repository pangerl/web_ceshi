import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
from config import username, password


class Browser:
    # 构造函数：初始化基本信息
    def __init__(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(30)
        self.driver = driver

    def web_test(self, url, logger, mail, mail_to_list, mail_title):
        try:
            logger.info('开始访问{}'.format(url))
            self.driver.get(url)
        except Exception as e:
            msg = '{}无法打开'.format(url) + str(e)
            logger.info(msg)
            mail.sendtxtmail(mail_to_list, mail_title, msg, logger)
            return False

        try:
            self.driver.find_element_by_link_text(u"进入啊哈教室").click()
            logger.info('准备登陆账号{}'.format(username))
            self.driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='下一步'])[1]/following::img[3]").click()
            self.driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='完成'])[1]/following::input[1]").click()
            self.driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='完成'])[1]/following::input[1]").click()
            self.driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='完成'])[1]/following::input[1]").clear()
            self.driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='完成'])[1]/following::input[1]").send_keys(username)
            self.driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='完成'])[1]/following::input[2]").click()
            self.driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='完成'])[1]/following::input[2]").clear()
            self.driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='完成'])[1]/following::input[2]").send_keys(password)
            self.driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='完成'])[1]/following::button[1]").click()
        except NoSuchElementException as e:
            msg = '输入异常：' + e.msg
            logger.info(msg)
            mail.sendtxtmail(mail_to_list, mail_title, msg, logger)
            return False

        try:
            self.driver.find_element_by_link_text(u"进入啊哈教室").click()
            logger.info('登录成功，准备进入啊哈教室')
        except NoSuchElementException as e:
            msg = '登录失败：' + e.msg
            logger.info(msg)
            mail.sendtxtmail(mail_to_list, mail_title, msg, logger)
            return False

        try:
            logger.info('进入成功，准备退出')
            self.driver.find_element_by_class_name('dropdown-toggle').click()
            time.sleep(1)
            self.driver.find_element_by_id("teacher_nav_btn_logout").click()
            mouse = self.driver.find_element_by_xpath(
                "//div[@id='app-navbar-collapse']/ul[2]/li[2]//div[@class='ivu-dropdown-rel']")
            ActionChains(self.driver).move_to_element(mouse).perform()
            self.driver.find_element_by_link_text(u"退出登录").click()
        except NoSuchElementException as e:
            msg = '登出啊哈教室失败：' + e.msg
            logger.info(msg)
            mail.sendtxtmail(mail_to_list, mail_title, msg, logger)
            return False

        logger.info('成功登出{}账号'.format(username))
        return True

    # 析构函数：释放资源
    def __del__(self):
        self.driver.close()
        # self.driver.quit()
