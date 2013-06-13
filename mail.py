import cgi, smtplib
from email.mime.text import MIMEText
def application(environ, start_response):
    if environ['REQUEST_METHOD'] == 'POST':
        try:
            form = cgi.FieldStorage(fp=environ['wsgi.input'], 
                                environ=environ)
            body = form['encrypted'].value
            fromaddr = "securemessage@mballantyne.net"
            toaddr = "michael.ballantyne@gmail.com"
            msg = MIMEText(body)
            msg['Subject'] = "Secure message"
            msg['From'] = fromaddr
            msg['To'] = toaddr

            s = smtplib.SMTP('localhost')
            s.sendmail(fromaddr, [toaddr], msg.as_string())
            s.quit()

            start_response('301 Redirect', [('Location', 'sent.html'),])
            return []

        except:
            start_response('301 Redirect', [('Location', 'failed.html'),])
            return []
