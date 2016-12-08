#git pull
# smtplib module send mail
#add another line
import smtplib

TO = ''
SUBJECT = 'TEST MAIL'
TEXT = 'Here is a message from python.'
if 
else:
    pass



# Gmail Sign In
gmail_sender = '
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
