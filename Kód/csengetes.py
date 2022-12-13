import RPi.GPIO as GPIO
import time
import smtplib
import pygame
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

GPIO.setmode(GPIO.BCM)

GPIO.setup(4,GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(4)
    if input_state==False:
        
        pygame.mixer.init()
        pygame.mixer.music.load("/home/pi/Desktop/projekt2.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy()==True:
            continue
        print('Gomb megnyomva')
        time.sleep(0.2)
        email_sender = 'projektmunka2sze@freemail.hu'
        email_receiver = 'vegh.adam2000@gmail.com'
        subject = 'Csengetes'
        msg = MIMEMultipart()
        msg['From'] = email_sender
        msg['To'] = email_receiver
        msg['Subject']= subject
        body = 'Valaki csengetett ha kivan reagalni kerjuk nyissa meg az alkalmazast.'
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        connection = smtplib.SMTP('smtp.freemail.hu', 587)
        connection.starttls()
        connection.login(email_sender,'Jelszo12345')
        connection.sendmail(email_sender, email_receiver, text )
        connection.quit()
        print('Uzenet elkuldve')
