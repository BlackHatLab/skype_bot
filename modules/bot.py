from sys import path
import os
from random import randint
from time import sleep

path.append (os.path.realpath (os.path.dirname (__file__)) + '../')
path.append (os.path.realpath (os.path.dirname (__file__)))

from Skype4Py import call
import Skype4Py

from skype_bot import opt
from output import *

class BotM:
	
	def __init__ (self, client):
	        self.client = client

	def start_message_flood (self, login, mes, delay):
    		mes = mes
    		while True:
		   if mes == '':
			 for i in range (11): mes += str (randint (0, 1000000))*i
        	   try:
             			if login != 'all': 
 			     		self.client.SendMessage (login, mes)
			     		sleep (delay)
		             		print YES + 'Message Sent to ' + login
				else: 
			     		for i in self.client.Friends: self.client.SendMessage (i.Handle, mes)
			     		sleep (delay)
	    	             		print YES + 'Message Sent to ' + i.Handle
                   except KeyboardInterrupt:
            		opt (self.client)

	def start_call_flood (self, login, delay):
    			while True:
			     try:
				 if login != 'all':
            		    		 call = self.client.PlaceCall (login)
			    		 sleep (delay)
			    		 call.Finish ()
			    		 print YES + 'Called to ' + login
				 else:
			    		 for i in self.client.Friends:
					      call = self.client.PlaceCall (i.Handle)
					      sleep (delay)
					      call.Finish ()
	    	        		      print YES + 'Called to ' + i.Handle
         		     except Exception as e:
			  	  if e == KeyboardInterrupt:
					 opt (self.client)
			  	  else: pass

	def show_friend_list (self):
		print INFO + 'Found ' + str (len (self.client.Friends)) + ' friends! Friend List: '
		for i in self.client.Friends:
	     		print YES + 'Name: ' + i.FullName + '\n' + YES + 'Login: ' + i.Handle + '\n\n'
  		opt (self.client)

	def start_auto_answering_machine (self, wav_file):
		self.wf = wav_file
		self.client.OnCallStatus = self.OnCall
		while True:
		   pass	
	

	# Dont touch this function!
	def OnCall(self, call, status):
     		if status == Skype4Py.clsRinging and call.Type.startswith('INCOMING'):
      			print INFO + 'Incoming call from: ' +  call.PartnerHandle 
      			sleep(1)
        		try:
          			call.Answer()
        		except:
          		 	pass

     		if status == Skype4Py.clsInProgress:
      			print INFO + 'Playing: ' + self.wf
      			call.InputDevice(Skype4Py.callIoDeviceTypeFile, self.wf)
	
	
	
	def show_chats (self):
		print INFO + 'Found ' + str (len (self.client.Chats)) + ' chats! Chat List: '
		for i in range (len (self.client.Chats)):
			print 'Chat ' + str (i)
			for i in self.client.Chats [i].Members: print '    ' + i.Handle
		opt (self.client)

	def find_users (self, text):
		print INFO + 'Found ' + str (len (users)) + ' users! User list: '
		for i in users:
			print '	   ' + YES + 'User Login: ' + i.Handle
			try: 
                    		if text.split (' ')[1] == 'add': 
					c = Skype4Py.client.Client (self.client)
					c.OpenAddContactDialog (i.Handle)
					print INFO + 'Opening contact dialog...'
			except:
				pass
		opt (self.client) 	

	def start_auto_stop_call (self, mes):
		self.client.OnCallStatus = self.discall
		print INFO + 'Auto Discalling Started'
		if mes != '': self.discall_message = mes
		end = False
		try:
			while not end:
		    		pass
		except KeyboardInterrupt:
			end = True 
			opt (self.client)

	# Don't touch this function!
	def discall (self, call, status):
		if status == Skype4Py.clsRinging and call.Type.startswith ('INCOMING'):
			try:
				call.Answer ()
				call.Finish ()
				if self.discall_message != '': self.client.SendMessage (call.PartnerHandle, self.discall_message)
				print YES + 'Discalled call from ' + call.PartnerHandle
			except:
				pass
