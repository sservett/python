import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj = MIMEMultipart()

mesaj["From"] = "Servet INCE"

mesaj["To"] = "servet.ince@yahoo.com"

mesaj["Cc"] = "sservetincee@gmail.com"

mesaj["Subject"] = "TESEKKURLER // Smtp Mail Gönderme"


yazi = """

BU bir test mailidir.

"""


mesaj_govdesi = MIMEText(yazi,"plain")

mesaj.attach(mesaj_govdesi)

try:
    mail = smtplib.SMTP("smtp.gmail.com",587)

    mail.ehlo()

    mail.starttls()

    mail.login("sservetincee@gmail.com","***************************")

    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())

    print("Mail Başarıyla Gönderildi....")

    mail.close()

except:
    sys.stderr.write("Bir sorun oluştu!")
    sys.stderr.flush()
