from config import mail_user, mail_pwd, smtp_host, mail_to_list, mail_title
from ketang_login import Browser
from send_mail import SendEmail
from logger import Logger

logger = Logger('edu').logger
mail = SendEmail(smtp_host, mail_user, mail_pwd)
browser = Browser()


# def alert(msg):
#     logger.info(msg)
#     msg = str(msg)
#     mail.sendTxtMail(mail_to_list, mail_title, msg, logger)
#     return False


if __name__ == '__main__':
    url = 'https://edu.codeaha.com/school'
    if browser.web_test(url, logger, mail, mail_to_list, mail_title):
        print('测试通过')
    else:
        print('测试失败，请看日志')
    # 分割行
    logger.info('================================================')
