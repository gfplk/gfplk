from __future__ import absolute_import, unicode_literals
from celery import shared_task

import smtplib
import email.mime.multipart
import email.mime.text


@shared_task
def send_email_task(subject, to, content):
    msg = email.mime.text.MIMEText(content, 'html', 'utf-8')
    msg['From'] = From
    msg['To'] = to
    msg['Subject'] = subject

    smtp = smtplib.SMTP()
    smtp.set_debuglevel(1)
    smtp.connect('smtp.163.com')
    smtp.login('gfplk_admin@163.com', 'sc5201314')
    smtp.sendmail('gfplk_admin@163.com', to, msg.as_string())
    smtp.quit()