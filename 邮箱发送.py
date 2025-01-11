"""
======================模块功能描述=========================    
       @File     : 邮箱发送.py
       @IDE      : PyCharm
       @Date     : 2025/1/11 下午5:25 11 
       @Desc     : 
=========================================================   
"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send_email():
    # 第三方 SMTP 服务
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = "3252689175@qq.com"  # 邮件发送者，上面设置SMTP服务的邮箱地址
    mail_pass = "iucomcivfeoxcgjd"  # 上面配置SMTP服务时生成的授权码
    receivers = ['3252689175@qq.com']  # 邮件接收者，可设置为你的QQ邮箱或者其他邮箱
    mail_msg = '抢到票了，赶紧去付钱（正文）'  # 需要发送的正文内容

    # MIMEText(text, subtype, charset) 创建邮件正文
    # text: 正文内容，可以是纯文本或html格式；
    # subtype： 正文内容类型，可以是 "plain"(纯文本）或 "html"(HTML格式);
    # charset: 正文内容的编码方式，常用“utf-8"、"gbk"等等。
    message = MIMEText(mail_msg, 'html', 'utf-8')
    message['From'] = Header(mail_user)  # 邮件页面显示发件人；这里可以直接填写邮件发送者 message['From'] = Header(mail_user)
    message['To'] = Header("所有收到我信息的人", 'utf-8')  # 邮件页面显示收件人
    message['Subject'] = Header('抢票通知（主题）', 'utf-8')  # 邮件页面显示主题

    try:
        # 发起连接，smtplib.SMTP 端口一般为25；如果是使用SSL，则需要改成 smtplib.SMTP_SSL(mail_host, 465) 端口是465或587
        # smtpObj = smtplib.SMTP(mail_host, 25)
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)
        smtpObj.login(mail_user, mail_pass)  # 登录邮箱 参数： login(邮件发送者，授权码)
        smtpObj.sendmail(mail_user, receivers, message.as_string())  # 发送邮件 参数： sendmail(邮件发送者，邮件接受者，邮件内容)
        print("邮件发送成功")
        smtpObj.quit()  # 关闭连接
    except smtplib.SMTPException as e:
        print(f"Error: 无法发送邮件{e}")


send_email()