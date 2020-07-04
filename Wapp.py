from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime
import time as t


m=Tk()
m.geometry('600x300')
m.title('Whatsapp Message Automator')
m.iconbitmap('wap.ico')
m.resizable(0,0)
n=None


def getvalue(event=None):
	global n, driver
	time=e4.get()
	l=Label(f,text='This message is scheduled after {} minutes'.format(time)).grid(row=6,columnspan=2)
	time=int(time)
	user=e1.get()
	msg=e2.get('1.0','end-1c')
	count=e3.get()
	count=int(count)
	wait=40

	user_path='//span[@title="{}"]'.format(user)
	msg_path='//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'

	if n is None:
		global driver
		driver=webdriver.Chrome(executable_path=r'D:\Python\chromedriver.exe')
		driver.get('https://web.whatsapp.com/')
		n=1
	t.sleep(20)
	driver.minimize_window()
	sec=time*60
	t.sleep(sec)
	ctct=WebDriverWait(driver,wait).until(lambda driver:driver.find_element_by_xpath(user_path))
	ctct.click()
	mg=driver.find_element_by_xpath(msg_path)
	for i in range(count):
		mg.send_keys(msg)
		mg.send_keys(Keys.RETURN)


def send():
	global n, driver
	user=e1.get()
	msg=e2.get('1.0','end-1c')
	count=e3.get()
	count=int(count)
	wait=40

	user_path='//span[@title="{}"]'.format(user)
	msg_path='//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'

	# button_path='//*[@id="main"]/footer/div[1]/div[3]/button'
	if n is None:
		global driver
		driver=webdriver.Chrome(executable_path=r'D:\Python\chromedriver.exe')
		driver.get('https://web.whatsapp.com/')
		n=1
	# print(time.process_time())
	ctct=WebDriverWait(driver,wait).until(lambda driver:driver.find_element_by_xpath(user_path))
	ctct.click()
	driver.minimize_window()
	mg=driver.find_element_by_xpath(msg_path)
	# butn=driver.find_element_by_xpath(button_path)
	for i in range(count):
		mg.send_keys(msg)
		mg.send_keys(Keys.RETURN)


f=Frame(m,borderwidth=5,height=300,width=580).grid(row=0,rowspan=7,columnspan=2,ipadx=10)
l=Label(f,text='Whatsapp',bg='yellow').grid(row=0,columnspan=2,ipadx=300,ipady=5)
l1=Label(f,text='Contact Name').grid(row=1,column=0)
l2=Label(f,text='Message').grid(row=2,column=0)
l3=Label(f,text='Count').grid(row=3,column=0)
b=Button(f,text='Send',command=send).grid(row=5,column=0)
e1=Entry(f,width=40,borderwidth=2,relief='groove')
e1.grid(row=1,column=1)
e2=Text(f,width=30,height=5,borderwidth=2,relief='groove')
e2.grid(row=2,column=1)
e3=Entry(f,width=20,borderwidth=2,relief='groove')
e3.grid(row=3,column=1)

l4=Label(f,text='Schedule After (mins)').grid(row=4,column=0)
# time=IntVar()
e4=Entry(f,width=20,borderwidth=1,relief='sunken')
e4.grid(row=4,column=1)
# e4.bind('<Return>',getvalue)
b2=Button(f,text='schedule',command=getvalue).grid(row=5,column=1)


search_path='//*[@id="side"]/div[1]/div/div'
search_btn='//*[@id="side"]/div[1]/div/button/div[1]/span/svg/path'


mainloop()
