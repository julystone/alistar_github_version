# 用于发送邮件的模块
import re
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class MyEmailSender:
    def __init__(self):
        HOST = 'smtp.qq.com'
        PORT = '465'
        self.smtp_obj = smtplib.SMTP_SSL(host=HOST)
        self.smtp_obj.connect(host=HOST, port=PORT)

    def send(self, sender, receiver, message):
        con_res = self.smtp_obj.login(user=sender, password='avgaqokikhrjhbdi')
        print('登录结果：', con_res)

        self.smtp_obj.sendmail(from_addr=sender, to_addrs=receiver, msg=message.as_string())

    @staticmethod
    def message_gen(From, To, Subject, Attachment):
        message = MIMEMultipart()
        message['From'] = Header(From, 'utf-8')
        message['To'] = Header(To, 'utf-8')
        message['Subject'] = Header(Subject, 'utf-8')

        message.attach(MIMEText('Here is the result of automation:', 'plain', 'utf-8'))
        # 构造附件1，传送当前目录下的 test.txt 文件
        for item in Attachment:
            att1 = MIMEText(open(item, 'rb').read(), 'base64', 'utf-8')
            att1["Content-Type"] = 'application/octet-stream'
            item_file = re.split(r"/|//|\\", item)[-1]
            att1["Content-Disposition"] = f'attachment; filename={item_file}'
            message.attach(att1)
        return message
