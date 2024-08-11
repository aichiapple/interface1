import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

base_dir = Path(__file__).parent.parent


def email_util(att=None, content=None, subject=None, ):
    """发送邮件的工具方法"""
    username = '1542462018@qq.com'
    password = 'otjwptmunyqpgjgg'
    receiver = 'runtingqiao@163.com'
    content = content
    if att is None:  # 不带附件
        message = MIMEText(content)
        message['subject'] = subject
        message['from'] = username
        message['to'] = receiver
    else:
        message = MIMEMultipart()
        txt = MIMEText(content, _charset='utf-8', _subtype="html")
        part = MIMEApplication(open('%s/%s' % (base_dir, att), 'rb').read())
        part.add_header('Content-Disposition', 'attachment', filename=att.split('\\')[-1])
        message['subject'] = subject
        message['from'] = username
        message['to'] = receiver
        message.attach(txt)
        message.attach(part)

        # 登录smtp服务器
        smtpserver = 'smtp.qq.com'
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(username, password)
        smtp.sendmail(username, receiver, message.as_string())
        #smtp.quit()


# if __name__ == '__main__':
#     email_util(content="<i>测试发送邮件</i>", subject="测试发送邮件主题", att='output/logs/20240713OkayProject.txt')
