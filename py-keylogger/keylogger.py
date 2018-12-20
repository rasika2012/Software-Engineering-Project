import pyxhook
import os
import treeNew
import unicodeWords as uni


root = data.Tree('*')
root = uni.add_unicode(root)
wordList = []

counter = 0
# fob=open(log_file,'w')
# log_file = '/media/rochana/University/Acadamic/Sem 6/Project/CO328/Software-Engineering-Project-master/py-keylogger/Key.log'       #this should be change according to user preference.
# fob=open(log_file,'w')

def printWord():
	global counter

	wordList.pop(counter)
	counter-=1
	to_convert = ''.join(wordList)
	uni.get_unicode(root,wordList)
	# treeNew.find(to_convert)
	
	# treeNew.find("".join([str(x) for x in wordList] ))
	print "\n"
	# print "".join([str(x) for x in wordList] )
	# word = unicodeWords.identifyWorks(word)
	# fob.write("".join([str(x) for x in wordList] ))
	counter =0
	del wordList[:]

def OnKeyPress(event):
	global counter
	wordList.append(event.Key)
  	
  		
  	if event.Ascii == 8 :
  		if len(wordList)==0:
  			pass
  		
  		else:
  			wordList.pop(counter)
	  		
	  		if len(wordList)!=0:
		  			  		
		  		counter-=1
	  			wordList.pop(counter)
		  		
	  			# wordList.pop(counter)
  			

	
	
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
