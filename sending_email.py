import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "your_email"
password = "please_enter_your_password"
toaddr = "uditasen.makaut.it@gmail.com"
text = MIMEMultipart()
text['From'] = fromaddr
text['To'] = toaddr
text['Subject'] = "I am sending this email using terminal"

body = ""
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
print("Hello,Our Mission is successful")
text_str = text.as_string()

server.send_message(text)

server.quit()
