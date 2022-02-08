"""Login/Signup portal with tkinter as GUI
    Used file based data system to store the acc/pwd""" 
import re
import tkinter
from tkinter import messagebox
from tkinter.ttk import Button,Entry

#checking for existing email,username on database
def check_existancy(data):
    file = open("accpdw.txt","rt")
    for i in file:
        exdata = i.split(" | ")
        print(exdata)
        mail_pattern = "^Email:"+str(data[0])+"$"
        matching_email = re.match(mail_pattern,exdata[0])
        username_pattern = "^Username:"+str(data[1])+"$"
        matching_username = re.match(username_pattern,exdata[1].rstrip())
        if matching_email:
            return 0
        elif matching_username:
            return 1
        else:
            continue
    file.close()
    return 2

#adding a new account in database
def add(data):
    return_value = check_existancy(data)
    if return_value == 0:
        messagebox.showinfo('Existing Account','Cannot create new account\nThis email account already exist')
    elif return_value == 1:
        messagebox.showinfo('Existing Account','Cannot create new account\nThis username already exist')
    else:
        print(data)
        pwd = re.findall("\w{8,32}",data[2])
        dig = re.findall("\d+",data[2])
        print(pwd,dig)
        mail = re.match("\w.+@",data[0])
        if mail:
            if (len(pwd)!= 0) & (len(dig)!=0):
                if data[2] == data[3]:
                    file = open("accpdw.txt","at")
                    file.write("\nEmail:%s | Username:%s | Password:%s"%(data[0],data[1],data[2]))
                    messagebox.showinfo('Account created','New account created')
                    signup_window.destroy()
                else:
                    messagebox.showinfo('password do not match','Entered password dosent')
            else:
                messagebox.showinfo('Incorrect password format','password must contain atleast 8 to 32 char\npassword must contain altest one number')

def ape():
        data = [email_input.get(),username_input.get(),password_input.get(),repassword_input.get(),TC_cb]
        add(data)

#login to account
def login():
    data = [username_input.get(),password_input.get()]
    file = open("accpdw.txt","rt")
    for i in file:
        exdata = i.split(" | ")
        username_pattern = "^Username:"+str(data[0])+"$"
        matching_username = re.match(username_pattern,exdata[1])
        password_pattern = "^Password:"+str(data[1])+"$"
        matching_password = re.match(password_pattern,exdata[2].rstrip())
        if matching_username:
            if matching_password:
                messagebox.showinfo('Logged in','You are logged in')
                return
            else:
                messagebox.showinfo('Invalid Password','Your password is invalid')
                return
        else:
            continue
    file.close()
    messagebox.showinfo('Invalid Username','Your username is invalid')


#GUI for sign up window
def signup():
    main_window.destroy()
    global signup_window
    signup_window = tkinter.Tk()
    signup_window.title("Sign Up")
    signup_window.geometry('350x300')
    signup_window.resizable(0,0)
    create_lable = tkinter.Label(text="Create Your Account",font="Arial 13").place(x=90,y=7)
    email_lable = tkinter.Label(text="Email",font="Arial 12").place(x=50,y=50)
    global email_input
    email_input = Entry(signup_window,width=30)
    email_input.place(x=130,y=50)
    username_lable = tkinter.Label(signup_window,text="Username",font="Arial 12").place(x=40,y=90)
    global username_input
    username_input = Entry(signup_window,width=20)
    username_input.place(x=130,y=90)
    password_lable = tkinter.Label(signup_window,text="Password",font="Arial 12").place(x=40,y=130)
    global password_input
    password_input = Entry(signup_window,width=20)
    password_input.place(x=130,y=130)
    repassword_lable = tkinter.Label(signup_window,text="Confirm Password",font="Arial 12").place(x=20,y=170)
    global repassword_input
    repassword_input = Entry(signup_window,width=20)
    repassword_input.place(x=160,y=170)
    global TC_cb
    TC_cb = tkinter.Checkbutton(signup_window,text="By checking the boxI accecpt all terms and conditions").place(x=30,y=210)
    submit_button = Button(text="Submit",width=20,command=ape).place(x=100,y=240)

#creating the main GUI for the login portal
main_window = tkinter.Tk()
main_window.title("Login")
main_window.geometry('350x200')
main_window.resizable(0,0)
username_lable = tkinter.Label(main_window,text="Username",font="Arial 14",pady=13,padx=50).grid(column=1,row=1)
username_input = Entry(main_window,width=20)
username_input.grid(column=2,row=1)
password_lable = tkinter.Label(main_window,text="Password",font="Arial 14").grid(column=1,row=4)
password_input = Entry(main_window,width=20)
password_input.grid(column=2,row=4)
ck = tkinter.Checkbutton(main_window,text="keep in logged in",pady=13).grid(column=1,row=5)
btn = Button(main_window,text="Log in",command=login).grid(column=2,row=5)
signup_lable = tkinter.Label(text="I don't have a account").grid(column=1,row=6)
signup_btn = Button(main_window,text="Sign Up",command=signup).grid(column=1,row=7)
tkinter.mainloop()
