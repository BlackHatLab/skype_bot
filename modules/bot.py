from sys import path
import os
from random import randint
from time import sleep

path.append (os.path.realpath (os.path.dirname (__file__)) + '../')
path.append (os.path.realpath (os.path.dirname (__file__)))

from Skype4Py import call

from skype_bot import opt
from output import *

class BotM:
	
	def __init__ (self, client):
	        self.client = client

	def start_message_flood (self, login):
    		mes = ''
    		for i in range (11): mes += str (randint (0, 1000000))*i
    		while True:
        	   try:
             		if login is not 'all': 
 			     self.client.SendMessage (login, mes)
			else: 
			     for i in self.client.Friends: self.client.SendMessage (i.Handle)
	    		print YES + 'Flood Sent'
                   except KeyboardInterrupt:
            		opt (self.client)
             		break

	def start_call_flood (self, login, delay):
    		while True:
        	    try:
            		call = self.client.PlaceCall (login)
			sleep (delay)
			call.Finish ()
	    		print YES + 'Flood Sent'
        	    except Exception as e:
            		if e == KeyboardInterrupt:
				 opt (self.client)
            			 break
			else:
 				 print ERR + 'Calling Error! Retrying!'

	def show_friend_list (self):
		print INFO + 'Found ' + str (len (self.client.Friends)) + ' friends! Friend List: '
		for i in self.client.Friends:
	     		print YES + 'Name: ' + i.FullName + '\n' + YES + 'Login: ' + i.Handle + '\n\n'
  		opt (self.client)
