# -*- coding: utf-8 -*-
# @Time    : 2020-5-27 18:51
# @Author  : suk
# @FileName: send_mail.py
# @Software: PyCharm
# @Blog    ：https://www.cnblogs.com/xjin/
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send_mail(receviers, mail_msg):
    mail_host = "smtp.qq.com"
    user_name = "suksite@qq.com"
    password = "12345"

    sender = user_name
    receviers = receviers

    message = MIMEText(mail_msg, "html", 'utf-8')
    message["From"] = Header("Suk", 'utf-8')
    message["To"] = Header("Developers", 'utf-8')

    subject = "UI自动化测试报告"
    message["Subject"] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP_SSL()
        smtpObj.connect(mail_host, 465)
        smtpObj.login(user_name, password)
        smtpObj.sendmail(sender, receviers, message.as_string())
        smtpObj.close()
        print("发送成功")
    except smtplib.SMTPException as error:
        print(error)


if __name__ == "__main__":
    receviers = ["xjinhz@126.com", "xu_j22@ecidi.com"]
    f = open("../testreport/report.html", 'r', encoding='utf-8')
    mail_msg = f.read()
    f.close()

    send_mail(receviers, mail_msg)
