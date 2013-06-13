import cgi, smtplib, sys, datetime
from email.mime.text import MIMEText
def application(environ, start_response):
    if environ['REQUEST_METHOD'] == 'POST':
        try:
            form = cgi.FieldStorage(fp=environ['wsgi.input'], 
                                environ=environ)
            body = form['encrypted'].value
            fromaddr = "michael.ballantyne@gmail.com"
            toaddr = "michael.ballantyne@gmail.com"
            msg = MIMEText(body)
            msg['Subject'] = "Secure message" + datetime.datetime.
            msg['From'] = fromaddr
            msg['To'] = toaddr

            s = smtplib.SMTP('localhost')
            s.sendmail(fromaddr, [toaddr], msg.as_string())
            s.quit()

            start_response('301 Redirect', [('Location', 'sent.html'),])
            return []

        except Exception as e:
            print >> sys.stderr, e 
            start_response('301 Redirect', [('Location', 'failed.html'),])
            return []
