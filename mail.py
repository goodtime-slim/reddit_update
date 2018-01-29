import imaplib


SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993

mail = imaplib.IMAP4_SSL(SMTP_SERVER)
mail.login(FROM_EMAIL,FROM_PWD)

mail.select('inbox')
mails = mail.search(None, 'Unseen')
if mails[1][0]:
    ids = mails[1][0].decode("utf-8").split(' ')
else:
    ids = []

for id in ids:
    t, data = mail.fetch(id, '(RFC822)')
    body = data[0][1]
    print(body)



