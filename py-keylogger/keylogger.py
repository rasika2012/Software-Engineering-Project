import pyxhook
import os
import tree
# import unicodeWords

wordList = []

counter = 0
# fob=open(log_file,'w')
log_file = '/media/rochana/University/Acadamic/Sem 6/Project/CO328/Software-Engineering-Project-master/py-keylogger/Key.log'       #this should be change according to user preference.
fob=open(log_file,'w')

def printWord():
	global counter

	

	wordList.pop(counter)
	counter-=1
	tree.find("".join([str(x) for x in wordList] ))
	print "".join([str(x) for x in wordList] )
	# word = unicodeWords.identifyWorks(word)
	# fob.write("".join([str(x) for x in wordList] ))
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
		# print(u'\u0DDD\u0D9A')
		# print(u'\u0D85\u0DB1')
		counter += 1


new_hook=pyxhook.HookManager()											#instantiate HookManager class
new_hook.KeyDown=OnKeyPress												#listen to all keystrokes
new_hook.HookKeyboard()													#hook the keyboard
new_hook.start()														#start the session
