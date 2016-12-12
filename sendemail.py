import smtplib
import base64
from passlib.hash import pbkdf2_sha256

TO = 'jzoudavy@gmail.com'
SUBJECT = 'TEST MAIL'
TEXT = 'Here is a message from python.'

#read the hidden file for the hashed password

#from passlib.hash import pbkdf2_sha256
#pbkdf2_sha256.verify("password", hash)
#hash = pbkdf2_sha256.encrypt("password", rounds=200000, salt_size=16)

# Gmail Sign In
gmail_sender = TO
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
