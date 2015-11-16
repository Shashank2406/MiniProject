from matplotlib import pyplot as plt
from Tkinter import *
import csv
import numpy as np

def Graph():							#Graph Plotter
	f = open('data.txt', 'w')
	i = 0
	year = e2.get()
	mylist = [10]
	y = [10]
	year = int (year)
	mylist[0] = year
	r = 2014 - year
	for i in range(0,int(r)):
		mylist= int(year + i)
		s = str(mylist)
		f.write(s)
		f.write('\n')
	f.close()

	f1 = open('data1.txt','w')
	while(year <= 2013):
		str2 = e3.get()
		x=str2.lower() + '_cy' + str(year) + '_top.csv'
		f=open(x)
		csv_f=csv.reader(f)
		str1 = e1.get()
		header=next(csv_f)
		for row in csv_f:
			if(row[0] == str1.upper()):
				y= row[1]	
				break
		s = str(y)
		f1.write(s)
		f1.write('\n')	
		year = year +1	
	f1.close()
	data = np.loadtxt("data.txt")
	data1 = np.loadtxt("data1.txt")
	x=np.loadtxt("data.txt",unpack=True)
	y=np.loadtxt("data1.txt",unpack=True)
	plt.plot(x, y, linewidth=2.0)
	plt.title('Popularity of Name')
	plt.ylabel('Name Frequency')
	plt.xlabel('Year')
	plt.show()
def Graphps():
	f = open('data.dat', 'w')
	i = 0
	year = e2.get()
	mylist = [10]
	y = [10]
	year = int (year)
	mylist[0] = year
	r = 2014 - year
	for i in range(0,int(r)):
		mylist= int(year + i)
		s = str(mylist)
		f.write(s)
		f.write('\n')
	f.close()
	f1 = open('data1.dat','w')
	while(year <= 2013):
		str2 = e3.get()
		x=str2.lower() + '_cy' + str(year) + '_top.csv'
		f=open(x)
		str1 = rx.get()
		csv_f=csv.reader(f)
		header=next(csv_f)
		for row in csv_f:
			if(row[0] == str1.upper()):
				y= row[1]	
				break
		s = str(y)
		f1.write(s)
		f1.write('\n')	
		year = year +1	
	f1.close()
	x=np.loadtxt("data.dat",unpack=True)
	y=np.loadtxt("data1.dat",unpack=True)
	plt.plot(x, y, linewidth=2.0)
	plt.title('Popularity of Name')
	plt.ylabel('Name Frequency')
	plt.xlabel('Year')
	plt.show()
	
def graph_1():							#Graph Input
	entr=Tk()
	GENDER=["Male","Female"]
	Label(entr,text='Enter Name').grid(row=0)
	Label(entr,text='Select Year').grid(row=1)
	Label(entr,text='Select Gender').grid(row=2)
	entr.wm_title("Graph")
	global e1
	e1=Entry(entr)
	global e2
	e2=StringVar(entr)
	e2.set(OPTIONS[0]) # default value
	w = apply(OptionMenu, (entr, e2) + tuple(OPTIONS))
	global e3
	e3=StringVar(entr)
	e3.set(GENDER[0]) # default value
	w1 = apply(OptionMenu, (entr, e3) + tuple(GENDER))
	e1.grid(row=0,column=1)
	w.grid(row=1,column=1)
	w1.grid(row=2,column=1)
	Button(entr,height=2,width=20,text='Exit',command=entr.destroy).grid(row=3,column=0,sticky=W,pady=4)
	Button(entr,height=2,width=20,text='Show',command=bridge1).grid(row=3,column=1,sticky=W,pady=4)
	entr.mainloop()
def Both():							#both case
	root = Tk()
	root.wm_title("Top")
	T = Text(root, width=40, height=40)
	S = Scrollbar(root)
	S.pack(side=RIGHT, fill=Y)
	T.pack(side=LEFT, fill=Y)
	S.config(command=T.yview)
	T.config(yscrollcommand=S.set)
	str1 = 'female'
	str2 = e2.get()
	x=(str1) + '_cy' + (str2) + '_top.csv'
	print x 
	f=open(x)
	csv_f=csv.reader(f)
	f1 = open('data1.txt','w')
	s = '\n--FEMALE--\n'
	f1.write(s)
	x=e1.get()
	for row in csv_f:
		y=row[2]
	 	y=y.replace("=","")
	 	if(y == "Position"):
	 		print "Shashank"
		else:
			if(int (y) <= int (x)):
				s = str(row[2])
				s = s.replace("=","")	
				f1.write(s)
				f1.write('  ')
				s = str(row[1])	
				f1.write(s)
				f1.write('  ')
				s = str(row[0])	
				f1.write(s)
				f1.write('\n')	
	#f1.close()
	s = '\n--MALE--\n'	
	f1.write(s)
	str1 = 'male'
	#global str2
	str2 = e2.get()
	x=(str1) + '_cy' + (str2) + '_top.csv'
	print x 
	f=open(x)
	csv_f=csv.reader(f)
	#f1 = open('data1.txt','w')
	x=e1.get()
	for row in csv_f:
		y=row[2]
	 	y=y.replace("=","")
	 	if(y == "Position"):
	 		print "Shashank"
		else:
			if(int (y) <= int (x)):
				s = str(row[2])
				s = s.replace("=","")	
				f1.write(s)
				f1.write('  ')
				s = str(row[1])	
				f1.write(s)
				f1.write('  ')
				s = str(row[0])	
				f1.write(s)
				f1.write('\n')	
	f1.close()	
	f2 = open("data1.txt","r")
	T.insert(END, f2.read())
	root.mainloop()	
def bridge():						#both helper
	str1 = e3.get()
	str1 = str1.lower()
	str2 = 'both'
	if(str1 == str2):	
		Both()
	else:
		top_1()	
def bridge1():
	str2=e3.get()
	year = e2.get()
	x=str2.lower() + '_cy' + str(year) + '_top.csv'
	f=open(x)
	str1 = e1.get()
	csv_f=csv.reader(f)
	header=next(csv_f)
	for row in csv_f:
		if(row[0] == str1.upper()):
			Graph()
			return()
	f.close()
	str1 = e3.get()
	NAMES = [30]
	NAMES[0]=""
	x=(str1.lower()) + '_cy' + (e2.get()) + '_top.csv'
	print x 
	f=open(x)
	csv_f=csv.reader(f)
	root = Tk()
	x=e1.get()
	for row in csv_f:
	 	y=row[2]
	 	y=y.replace("=","")
	 	if(y == "Position"):
	 		print "Shashank"
		else:
			s = str(row[0])
			s1 = str(e1.get())
			if (s.startswith(s1.upper())==True):	
				s = str(row[0])	
				NAMES.append(s)
	Label(root,text='Select Name').grid(row=0)	
	global rx	
	rx = StringVar(root)
	rx.set(NAMES[1]) # default value
	w = apply(OptionMenu, (root, rx) + tuple(NAMES))	
	Button(root,height=2,width=20,text='Exit',command=root.destroy).grid(row=3,column=0,sticky=W,pady=4)
	Button(root,height=2,width=20,text='Plot',command=Graphps).grid(row=3,column=1,sticky=W,pady=4)		
	w.grid(row=0,column=1)
	root.wm_title("Bridge")				
	root.mainloop()		
def about():						#about function
	root = Tk()
	root.wm_title("About")
	frame= Frame(root,width=400, height=40)
	thelable = Label(root,text = "MADE BY\nShashank Srivastava\nBTech IT V Semester\nRoll No 38")
	button_4 = Button(root,text="Ok", command=root.destroy)
	button_4.config( height = 2, width = 30 )
	thelable.pack()
	button_4.pack()
	frame.pack()
	root.mainloop()	
def top():						#top function
	entr=Tk()
	GENDER=["Male","Female","Both"]
	entr.wm_title("Top")
	Label(entr,text='Enter Top').grid(row=0)
	Label(entr,text='Enter Year').grid(row=1)
	Label(entr,text='Male/Female/Both').grid(row=2)
	global e1
	e1=Entry(entr)
	global e2
	e2=StringVar(entr)
	e2.set(OPTIONS[0]) # default value
	w = apply(OptionMenu, (entr, e2) + tuple(OPTIONS))
	global e3
	e3=StringVar(entr)
	e3.set(GENDER[0]) # default value
	w1 = apply(OptionMenu, (entr, e3) + tuple(GENDER))
	e1.grid(row=0,column=1)
	w.grid(row=1,column=1)
	w1.grid(row=2,column=1)
	Button(entr,height=2,width=20,text='Exit',command=entr.destroy).grid(row=3,column=0,sticky=W,pady=4)
	Button(entr,height=2,width=20,text='Show',command=bridge).grid(row=3,column=1,sticky=W,pady=4)
	entr.mainloop()
def top_1():						#top value input
	str1 = e3.get()
	x=(str1.lower()) + '_cy' + (e2.get()) + '_top.csv'
	print x 
	f=open(x)
	csv_f=csv.reader(f)
	root = Tk()
	T = Text(root, width=40, height=40)
	S = Scrollbar(root)
	S.pack(side=RIGHT, fill=Y)
	T.pack(side=LEFT, fill=Y)
	S.config(command=T.yview)
	T.config(yscrollcommand=S.set)
	x=e1.get()
	for row in csv_f:
	 	y=row[2]
	 	y=y.replace("=","")
	 	if(y == "Position"):
	 		print "Shashank"
		else:
			if(int (y) <= int (x)):	
				s = str(row[2])
				s = s.replace("=","")	
				T.insert(END,s)
				T.insert(END,'  ')	
				s = str(row[1])	
				T.insert(END,s)
				T.insert(END,'  ')
				s = str(row[0])	
				T.insert(END,s)
				T.insert(END,'\n')
	root.wm_title("Top")			
	root.mainloop()	
'''def ps():							#partial Search Beta
	str1 = e3.get()
	x=(str1.lower()) + '_cy' + (e2.get()) + '_top.csv'
	print x 
	f=open(x)
	csv_f=csv.reader(f)
	root = Tk()
	T = Text(root, width=40, height=60)
	S = Scrollbar(root)
	S.pack(side=RIGHT, fill=Y)
	T.pack(side=LEFT, fill=Y)
	S.config(command=T.yview)
	T.config(yscrollcommand=S.set)
	x=e1.get()
	for row in csv_f:
	 	y=row[2]
	 	y=y.replace("=","")
	 	if(y == "Position"):
	 		print "Shashank"
		else:
			s = str(row[0])
			s1 = str(e1.get())
			if (s.find(s1.upper())!=-1):	
				s = str(row[0])	
				T.insert(END,s)
				T.insert(END,'\n')	
	root.wm_title("Top")				
	root.mainloop()'''
'''def ps_1():
	entr=Tk()
	Label(entr,text='Enter Name').grid(row=0)
	Label(entr,text='Enter Year').grid(row=1)
	Label(entr,text='Male/Female').grid(row=2)
	global e1
	e1=Entry(entr)
	global e2
	e2=Entry(entr)
	global e3
	e3=Entry(entr)
	e1.grid(row=0,column=1)
	e2.grid(row=1,column=1)
	e3.grid(row=2,column=1)
	Button(entr,height=2,width=20,text='Exit',command=entr.destroy).grid(row=3,column=0,sticky=W,pady=4)
	Button(entr,height=2,width=20,text='Show',command=ps).grid(row=3,column=1,sticky=W,pady=4)
	entr.mainloop()	'''
def mini():						#main window
	root = Tk()
	global OPTIONS
	OPTIONS=[70]
	OPTIONS[0] = '1945'
	global OPTIONS
	for i in range(1946,2014):
		OPTIONS.append(i)
	frame= Frame(root,width=240, height=30)
	root.wm_title("Mini Project")
	thelable = Label(root,text = "Mini Project Final Phase 1")  #creates label window
	button_1 = Button(root,text="Top Names", command=top)
	button_2 = Button(root,text="Graph", command=graph_1)
	button_3 = Button(root,text="About", command=about)
	button_4 = Button(root,text="Exit", command=root.destroy)
	thelable.pack()
	button_1.config( height = 5, width = 40 )
	button_2.config( height = 5, width = 40 )
	button_3.config( height = 5, width = 40 )
	button_4.config( height = 5, width = 40 )
	button_1.pack()
	button_2.pack()
	button_3.pack()
	button_4.pack()
	frame.pack()
	root.mainloop()

if __name__ == "__main__":
	mini()
