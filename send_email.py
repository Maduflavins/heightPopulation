# from email.mime.text import MIMEText
# import smtplib
#
#
# def send_email(email, height, average_height, count):
#     from_email="email@gmail.com"
#     from_password= "password"
#     to_email = email
#
#
#     subject="Height Data"
#     message="Hey dear, your height is<strong>%s</strong>. Average height of people witin your bracket is<strong> %s</strong> caluculated out %s of users" % (height, average_height, count)
#
#     msg=MIMEText(message, 'html')
#     msg['subject']=subject
#     msg['To']=to_email
#     msg['From']=from_email
#
#     gmail=smtplib.SMTP('smtp.gmail.com',587)
#     gmail.ehlo()
#     gmail.starttls()
#     gmail.login(from_email, (from_password))
#     gmail.sendmail(mesg)


import smtplib
from email.mime.text import MIMEText

def send_email(email, height, average_height, count):
    SMTP_SERVER = "smtp.mail.yahoo.com"
    SMTP_PORT = 587
    SMTP_USERNAME = "myemail@yahoo.com"
    SMTP_PASSWORD = "mypassword"
    EMAIL_FROM = "myemail@yahoo.com"
    EMAIL_TO = email
    EMAIL_SUBJECT = "Height Data:"
    message="Hey dear, your height is<strong>%s</strong>. Average height of people witin your bracket is<strong> %s</strong> caluculated out %s of users" % (height, average_height, count)
    msg = MIMEText(message)
    msg['Subject'] = EMAIL_SUBJECT + "Company - Service at appointmentTime"
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO
    debuglevel = True
    mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    mail.set_debuglevel(debuglevel)
    mail.starttls()
    mail.login(SMTP_USERNAME, SMTP_PASSWORD)
    mail.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    mail.quit()

if __name__=='__main__':
    send_email()
