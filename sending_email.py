import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = input("Please enter your_email")
password = "please_enter_your_password"
toaddr = "uditasen.makaut.it@gmail.com"
text = MIMEMultipart()
text['From'] = fromaddr
text['To'] = toaddr
text['Subject'] = input("What is the subject of the email")

body = input("Please enter body of the email")
text.attach(MIMEText(body, 'plain'))

filename = "code1.py" #please enter a valid file present in your computer
attachment = open(filename, "rb")
final = MIMEBase('application', 'octet-stream')

final.set_payload((attachment).read())

encoders.encode_base64(final)

final.add_header('Content-Disposition', "attachment; filename= %s" % filename)
text.attach(final)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr,password)
print("Email Sent!")
text_str = text.as_string()

server.send_message(text)

server.quit()
