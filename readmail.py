import imaplib
mailserver=imaplib.IMAP4_SSL('imap.gmail.com',993)
username='username'
password='password'
mailserver.login(username,password)
status,count=mailserver.select('Inbox')
status,data=mailserver.fetch(count[0],'(UID BODY[TEXT])')
print data[0][1]


