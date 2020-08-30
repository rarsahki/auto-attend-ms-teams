#!/usr/bin/env python3
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from crontab import CronTab
import time
import pathlib
import os

class NewprojectApp:
    def __init__(self, master=None):
        # build ui
        a = []
        def insert():
            cron = CronTab(user=True)
            job = cron.new(command='export DISPLAY=:0 && cd ~/Desktop && ./chrome \"'+
                    entry_1.get().strip()+"\" \""+roll_entry.get().strip()+"\" \""+pass_entry.get().strip()+'\"')
            if(len(checkbutton_1.state()) > 0 and checkbutton_1.state()[0] == "selected"):
                job.dow.also.on('MON')
            if(len(checkbutton_2.state()) > 0 and checkbutton_2.state()[0] == "selected"):
                job.dow.also.on('TUE')
            if(len(checkbutton_3.state()) > 0 and checkbutton_3.state()[0] == "selected"):
                job.dow.also.on('WED')
            if(len(checkbutton_4.state()) > 0 and checkbutton_4.state()[0] == "selected"):
                job.dow.also.on('THU')
            if(len(checkbutton_5.state()) > 0 and checkbutton_5.state()[0] == "selected"):
                job.dow.also.on('FRI')
            if(len(checkbutton_6.state()) > 0 and checkbutton_6.state()[0] == "selected"):
                job.dow.also.on('SAT')
            if(len(checkbutton_7.state()) > 0 and checkbutton_7.state()[0] == "selected"):
                job.dow.also.on('SUN')
            job.hour.on(entry_2.get()[0:2])
            job.minute.on(entry_2.get()[3:5])
            cron.write() 
            messagebox.showinfo("Success","Successfully Added The Task")
            print("Success")
        def deleteAll():
            cron = CronTab(user=True)
            cron.remove_all()
            cron.write()
            messagebox.showinfo("Success","Deleted All Scheduled Tasks")
            print("Deleted All")
            
        frame_1 = tk.Frame(master)
        roll_label = ttk.Label(frame_1)
        roll_label.config(text="Roll No")
        roll_label.grid()
        roll_entry = ttk.Entry(frame_1)
        roll_entry.grid(column='1', row='0')
        pass_label = ttk.Label(frame_1)
        pass_label.config(text="Password")
        pass_label.grid(column='0', row='1')
        pass_entry = ttk.Entry(frame_1)
        pass_entry.grid(column='1', row='1')

        label_1 = ttk.Label(frame_1)
        label_1.config(text="Subject(as on MS Teams)")
        label_1.grid(column='0', row='2')
        entry_1 = ttk.Entry(frame_1)
        entry_1.grid(column='1', row='2')
        var1 = tk.StringVar()
        checkbutton_1 = ttk.Checkbutton(frame_1,variable=var1,onvalue="MON",offvalue="")
        checkbutton_1.config(text='MON')
        checkbutton_1.grid(column='0', row='3')
        var2 = tk.StringVar()
        checkbutton_2 = ttk.Checkbutton(frame_1,variable=var2,onvalue="TUE",offvalue="")
        checkbutton_2.config(text='TUE')
        checkbutton_2.grid(column='1', row='3')
        var3 = tk.StringVar()
        checkbutton_3 = ttk.Checkbutton(frame_1,variable=var3,onvalue="WED",offvalue="")
        checkbutton_3.config(text='WED')
        checkbutton_3.grid(column='0', row='4')
        var4 = tk.StringVar()
        checkbutton_4 = ttk.Checkbutton(frame_1,variable=var4,onvalue="THU",offvalue="")
        checkbutton_4.config(text='THU')
        checkbutton_4.grid(column='1', row='4')
        var5 = tk.StringVar()
        checkbutton_5 = ttk.Checkbutton(frame_1,variable=var5,onvalue="FRI",offvalue="")
        checkbutton_5.config(text='FRI')
        checkbutton_5.grid(column='0', row='5')
        var6 = tk.StringVar()
        checkbutton_6 = ttk.Checkbutton(frame_1,variable=var6,onvalue="SAT",offvalue="")
        checkbutton_6.config(text='SAT')
        checkbutton_6.grid(column='1', row='5')
        var7 = tk.StringVar()
        checkbutton_7 = ttk.Checkbutton(frame_1,variable=var7,onvalue="SUN",offvalue="")
        checkbutton_7.config(text='SUN')
        checkbutton_7.grid(column='0', row='6')
        label_2 = ttk.Label(frame_1)
        label_2.config(text='Time')
        label_2.grid(column='0', row='7')
        entry_2 = ttk.Entry(frame_1)
        _text_ = '''Eg:21:30'''
        entry_2.delete('0', 'end')
        entry_2.insert('0', _text_)
        entry_2.grid(column='1', row='7')
        button_1 = ttk.Button(frame_1,command=insert)
        button_1.config(text='Submit')
        button_1.grid(column='0', row='8')
        button_2 = ttk.Button(frame_1,command=deleteAll)
        button_2.config(text='Delete All')
        button_2.grid(column='1', row='8')
        frame_1.config(height='200', width='200')
        frame_1.grid()

        # Main widget
        self.mainwindow = frame_1


    def run(self):
        self.mainwindow.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Create Task")
    app = NewprojectApp(root)
    app.run()

print("success")