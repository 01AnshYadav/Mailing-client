import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()

with open('password.txt') as f:
    password = f.read().strip()



server.login('cantsharethis01@gmail.com', password)


msg = MIMEMultipart()
msg['From'] = 'Ansh'
msg['To'] = 'yadav01ansh2006@gmail.com'
msg['Subject'] = 'Test Email'

with open("email msg.txt", "r") as f:
    message = f.read()


msg.attach(MIMEText(message, 'plain'))

filename = "email pic.png"
attachment = open(filename, "rb")

p=MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())


encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('cantsharethis01@gmail.com', 'yadav01ansh2006@gmail.com', text)