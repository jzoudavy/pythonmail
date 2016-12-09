import smtplib
import base64
from passlib.hash import pbkdf2_sha256

TO = ''
SUBJECT = 'TEST MAIL'
TEXT = 'Here is a message from python.'


# Gmail Sign In
gmail_sender = ''
gmail_passwd = ''

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_sender, gmail_passwd)

BODY = '\r\n'.join(['To: %s' % TO,
                    'From: %s' % gmail_sender,
                    'Subject: %s' % SUBJECT,
                    '', TEXT])

try:
    server.sendmail(gmail_sender, [TO], BODY)
    print ('email sent')
except:
    print ('error sending mail')

server.quit()
