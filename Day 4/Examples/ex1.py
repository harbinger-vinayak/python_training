"""
Wap to accept directory name from user and remove all the empty files, from that directory. (os.path.getsize)
"""

import os
import zipfile
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

path = raw_input("Enter file name: ")
zf = zipfile.ZipFile(path+"\myzipfile.zip", "w", zipfile.ZIP_DEFLATED)
if os.path.isdir(path):
    for root, dir, files in os.walk(path):
        zf.write(root)
        for filename in files:
            zf.write(os.path.join(root, filename))
            fsize = os.path.getsize(root + "\\" + filename)
            if fsize <= 0:
                os.remove(root + "\\" + filename)
                print "File removed."
        break

    fromaddr = "vinayak.katawe@harbinger.com"
    toaddr = "vinayakkatawe@gmail.com"

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = "Subject of the Mail"

    # string to store the body of the mail
    body = "Body_of_the_mail"

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # open the file to be sent
    filename = "File_name_with_extension"
    attachment = open(path+"\\myzipfile.zip", "rb")

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload((attachment).read())

    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, "India@1234")

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()

    zf.close()
else:
    print "Path not find."
