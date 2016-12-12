#add some more lines for push test
import smtplib
from cryptography.fernet import Fernet

#############################################################
# read login and password

file= open("/home/ubuntu/test_key",'rb')
stored_key=file.readline()
file.close()

file= open("/home/ubuntu/test_login",'rb')
stored_login=file.readline()
file.close()

file= open("/home/ubuntu/test_pwd",'rb')
stored_pwd=file.readline()
file.close()

f = Fernet(stored_key)
f.decrypt(stored_login)
f.decrypt(stored_pwd)

# Gmail Sign In
gmail_sender = str(f.decrypt(stored_login))
gmail_passwd = str(f.decrypt(stored_pwd))

#need to strip out the quotes and b at the beginning
gmail_sender = gmail_sender[2:-1]
gmail_passwd = gmail_passwd[2:-1]

############################################################
#print("gmail sender is "+gmail_sender)
#print("gmail password is "+gmail_passwd)

############################################
# compose message
TO = 'cerfvolant8@gmail.com'
SUBJECT = 'TEST MAIL'
TEXT = 'Here is a message from python.'


##########################################


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
    print('email sent')
except:
    print('error sending mail')

server.quit()
