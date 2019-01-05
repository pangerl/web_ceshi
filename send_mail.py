# from config import mail_user, mail_pwd, smtp_host, mail_to_list, mail_title
from email.mime.text import MIMEText
from email.header import Header
import smtplib


class SendEmail:
    # 构造函数：初始化基本信息
    def __init__(self, smtp, user, passwd):
        info = user.split("@")
        self._user = user
        self._account = info[0]
        self._me = self._account + "<" + self._user + ">"

        server = smtplib.SMTP(smtp)
        # server.connect(host)
        server.login(user, passwd)
        self._server = server

    # 发送文件或html邮件
    def sendtxtmail(self, to_list, title, content,
                    logger=None, subtype='html'):
        # 如果发送的是文本邮件，则_subtype设置为plain
        # 如果发送的是html邮件，则_subtype设置为html
        msg = MIMEText(content, _subtype=subtype, _charset='utf-8')
        msg['Subject'] = Header(title, 'utf-8')
        msg['From'] = self._me
        msg['To'] = ";".join(to_list)
        try:
            self._server.sendmail(self._me, to_list, msg.as_string())
            return True
        except Exception as e:
            if logger:
                logger.info(e)
            return False

    # 析构函数：释放资源
    def __del__(self):
        self._server.quit()
        self._server.close()


# mail = SendEmail(smtp_host, mail_user, mail_pwd)
# if mail.sendTxtMail(mail_to_list, mail_title, '蓝胖,<br><h1>你好，发送文本文件测试<h1>'):
#     print("发送成功")
# else:
#     print("发送失败")
