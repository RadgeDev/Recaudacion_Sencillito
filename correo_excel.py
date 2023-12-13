import smtplib
import mimetypes
from datetime import date
from datetime import datetime, timedelta
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

d = datetime.today() - timedelta(days=1)
emailfrom = ""
emailto =  'eavila@example'
fileToSend = 'D:\\excels\\recaudacioncyd_'+ d.strftime("%Y-%m-%d") + '.xls'
username = ""
password = ""


msg = MIMEMultipart()
msg["From"] = emailfrom
msg["To"] =  str(emailto)
msg["Subject"] = "Recaudacion Recepcionada por CYD a traves de Sencillito  para dia " + d.strftime("%d-%m-%Y") + ""
msg.preamble = "Recaudacion Recepcionada por CYD a traves de Sencillito  para dia " + d.strftime("%d-%m-%Y") + ""

ctype, encoding = mimetypes.guess_type(fileToSend)
if ctype is None or encoding is not None:
    ctype = "application/octet-stream"

maintype, subtype = ctype.split("/", 1)

if maintype == "text":
    fp = open(fileToSend)
    # Note: we should handle calculating the charset
    attachment = MIMEText(fp.read(), _subtype=subtype)
    fp.close()
elif maintype == "image":
    fp = open(fileToSend, "rb")
    attachment = MIMEImage(fp.read(), _subtype=subtype)
    fp.close()
elif maintype == "audio":
    fp = open(fileToSend, "rb")
    attachment = MIMEAudio(fp.read(), _subtype=subtype)
    fp.close()
else:
    fp = open(fileToSend, "rb")
    attachment = MIMEBase(maintype, subtype)
    attachment.set_payload(fp.read())
    fp.close()
    encoders.encode_base64(attachment)
attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
msg.attach(attachment)

server = smtplib.SMTP("")
server.starttls()
server.login(username,password)
server.sendmail(emailfrom,emailto , msg.as_string())
server.quit()
