import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html =Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] ='Abayomi Ogunnusi'
email['to'] = 'drsimplegraffiti@gmail.com'
email['subject'] = 'you won yippe'

email.set_content(html.substitute({'name':'Lovely'}), 'html')

with smtplib.SMTP(host='sandbox.smtp.mailtrap.io', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('aaa5ecc1a6c063', 'd8179f9411ebda')
    smtp.send_message(email)
    print("all good")
