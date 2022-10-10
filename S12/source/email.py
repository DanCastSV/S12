from os import getenv
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List, Optional


class Email:

    def __init__(self):
        self.Server = SMTP(
            host=getenv("SMTP_HOSTNAME"),
            port=getenv("SMTP_PORT")
        )

    def conect_server(self):
        self.Server.starttls()
        self.Server.login(
            user=getenv("SMTP_USER"),
            password=getenv("SMTP_PASSWORD")
        )

    def mandar_email(self, destinatario:List[str], contenido:Optional[str], **kwargs):
        self.conect_server()
        for destn in destinatario:
            mime = MIMEMultipart()
            mime['From']=getenv("SMTP_USER")
            mime['To']=destn
            mime['Subject']=contenido
            format = MIMEText(kwargs['message_format'], kwargs['format'])
            mime.attach(format)
            self.Server.sendmail(getenv("SMTP_USER"),destn,mime.as_string())
            self.desconect_server()


    def desconect_server(self):
        self.Server.quit()
        self.Server.close()