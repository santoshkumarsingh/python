import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
fromaddr='santosh.ksingh03@gmail.com'
text='Hello world'
to='santosh.ksingh03@gmail.com'
username='[username]'
password='*[password]'
msg=MIMEMultipart()
msg['From']=fromaddr
msg['To']=to
msg['Subject']='test'
msg.attach(MIMEText(text))
server=smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.ehlo()
server.login(username,password)
server.sendmail(fromaddr,to,msg.as_string())