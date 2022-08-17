import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_message():
    print("КУКУ")
    fromaddr = "dryabovichev@mail.ru"
    mypass = "TQzX3hE6w5EJMHc4MT3c"
    toaddr = "dryabovichev@mail.ru"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Отправитель: HR-KRIAL"  # + str(message.chat.id)
    body = "Message: Telegram_bot \n\n"
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.mail.ru')
    server.starttls()
    server.login(fromaddr, mypass)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

