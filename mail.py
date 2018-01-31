import imaplib
import re
import praw

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

regex = r"www\.reddit\.com\/r\/\w+\/\w+\/(\w+)"

for id in ids:
    t, data = mail.fetch(id, '(RFC822)')
    body = data[0][1].decode("utf-8")
    matches = re.findall(regex, body)
    thread = matches[0]
    kill = 'kill' in body.lower()
    if kill:
        kill(thread)
    else:
        comment_ids = get_comment_ids(thread)
        insert_comment_ids(thread, comment_ids)



