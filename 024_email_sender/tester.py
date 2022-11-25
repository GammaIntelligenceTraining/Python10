import smtplib
from email.message import EmailMessage

with smtplib.SMTP_SSL('smtp.zone.eu', 465) as server:
    server.login('tester@mrartful.com', 'test1269bfg90')

    msg = EmailMessage()
    msg['From'] = 'Python Script <tester@mrartful.com>'
    msg['To'] = 'Roman Kutselepa <roman.kutselepa@gmail.com>'
    msg['Subject'] = 'Python test'

    msg.set_content('This is a test email sent by Python script')
    msg.add_alternative(f'<h1>Hello world!</h1>'
                        f'<p style="color: red;">This is a test email sent by Python script</p>', subtype='html')

    server.send_message(msg)
    # server.sendmail('tester@mrartful.com', 'roman.kutselepa@gmail.com', text)