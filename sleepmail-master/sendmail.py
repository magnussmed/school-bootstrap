import smtplib
import config
import time

def sendMail(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_FROM, config.PASS)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.EMAIL_FROM, config.EMAIL_TO, message)
        server.quit()
        print("Email sendt!")
    except Exception as e: 
        print(e)
        
def run():
    #init time vars
    t = time.localtime()
    now = time.strftime("%H:%M", t)

    while now != config.TIME_TO_SEND: #not the same time?
        t = time.localtime() #update variable
        now = time.strftime("%H:%M", t) #update variable
        print("now:" + now)
        print("send: " + config.TIME_TO_SEND)
        time.sleep(5) #wait 5 secs before trying again
        
    else:
        sendMail(config.SUBJECT, config.MESSAGE)

run()
