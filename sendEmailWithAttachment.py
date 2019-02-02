import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def sendEmail(imgList):
    msg = MIMEMultipart()
    msg['Subject'] = 'Face detected'
    msg['From'] = 'sarkar.soumyabrata2@gmail.com'
    msg['To'] = 'sarkar.soumyabrata2@gmail.com'

    text = MIMEText("Face detected. Find the image in the attachment")
    msg.attach(text)
    for image in imgList:
        img_data = open(image, 'rb').read()
        image = MIMEImage(img_data, name=os.path.basename(image))
        msg.attach(image)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login('usename@gmail.com', 'password')
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()
