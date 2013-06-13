import cgi, smtplib
from email.mime.text import MIMEText
def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    
    if environ['REQUEST_METHOD'] == 'POST':
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

        return ['Thanks! Your message has been sent.\n']
