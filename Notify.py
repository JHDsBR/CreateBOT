import smtplib
from SECRET import GMAIL_FROM, GMAIL_FROM_PASSORD, GMAIL_TO


def SendEmail(assunto, relatorio, _from=None, _from_password=None, _to=None):
    
    _from = _from if _from else GMAIL_FROM
    _from_password = _from_password if _from_password else GMAIL_FROM_PASSORD
    _to = _to if _to else GMAIL_TO

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(_from, _from_password)
            message = 'Subject: {}\n\n{}'.format(assunto, relatorio)
            server.sendmail(_from, _to, message.encode("utf8"))
            server.quit()

        print('Email enviado com sucesso\n')
        return True
    except Exception as ex:
        print('Erro ao enviar email\n')
        print(ex)
        return False 
        

