#!/usr/bin/env python3
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from crontab import CronTab
import time
import pathlib
import os
import sys


ID = sys.argv[1]
try:
    email = sys.argv[2]
    password = sys.argv[3]
    subject = sys.argv[4]
    prof = sys.argv[5]
    time = sys.argv[6]
    days = sys.argv[7].split(',')
except IndexError:
    email = None
print("Let's Go!")
def insert(email,password,subject,prof,time,days):
    cron = CronTab(user='ark')
    job = cron.new(command='export DISPLAY=:0 && cd ~/ms-teams-auto-attend/ && python3 chrome.py \"'+
            subject+"\" \""+email+"\" \""+password+'\"' " \""+prof+"\"",comment=ID)
    for day in days:
        job.dow.also.on(day)
    job.hour.on(time[0:2])
    job.minute.on(time[3:5])
    cron.write()
    messagebox.showinfo("Success","Successfully Added The Task")
    print("Success")
def delete():
    cron = CronTab(user=True)
    for job in cron:
        if job.comment == ID:
            cron.remove(job)
            cron.write()
def deleteAll():
    cron = CronTab(user=True)
    cron.remove_all()
    cron.write()
    messagebox.showinfo("Success","Deleted All Scheduled Tasks")
    print("Deleted All")

if email is None:
    delete()
else:
    insert(email,password,subject,prof,time,days)