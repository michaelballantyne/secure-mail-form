import cgi, smtplib
from email.mime.text import MIMEText
def app(environ, start_response):
    if environ['REQUEST_METHOD'] == 'POST':
        try:
            form = cgi.FieldStorage(fp=environ['wsgi.input'], 
                                environ=environ)
            body = form['encrypted'].value
            addr = "michael.ballantyne@gmail.com"
            msg = MIMEText(body)
            msg['Subject'] = "Secure message form"
            msg['From'] = addr
            msg['To'] = addr

            s = smtplib.SMTP('localhost')
            s.sendmail(addr, [addr], msg.as_string())
            s.quit()

            start_response('301 Redirect', [('Location', 'sent.html'),])
            return []

        except:
            start_response('301 Redirect', [('Location', 'failed.html'),])
            return []
