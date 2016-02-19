import Skype4Py
from sys import path
import os

path.append (os.path.realpath (os.path.dirname (__file__)) + '/modules/')

import bot
from output import *

options = {
   'Skype Message Flood' : 1,
   'Skype Call Flood' : 2,
   'Show Friend List' : 3
}

def show_banner (cl=None):
    print '*'*70
    print ' '*15 + 'Your Name: ' + cl.CurrentUser.FullName + ' '*15
    print ' '*15 + 'Your Status: ' + cl.CurrentUserStatus + ' '*15
    print ' '*15 + 'Your Login: ' + cl.CurrentUser.Handle + ' '*15
    print '*'*70


def opt (cl=None):
	

    print
    for i in options: print i + ' ' +  str (options [i])

    client = bot.BotM (cl)

    cmd = raw_input ( '\n' + INFO + 'Select option (0 to exit): ')
    if cmd == '0':
        exit ()
    elif cmd == '1':
        client.start_message_flood (raw_input (INFO + 'Target\'s login: '), int (raw_input (INFO + 'Delay: ')))
    elif cmd == '2':
        client.start_call_flood (raw_input (INFO + 'Target\'s login: '), int (raw_input (INFO + 'Delay: ')))
    elif cmd == '3':
        client.show_friend_list ()
    else:
        print ERR + 'Option not found!'
	opt (cl=cl)

def main ():

    #global cl
    cl = Skype4Py.Skype ()

    if not cl.Client.IsRunning:
        cl.Client.Start ()


    cl.Attach ()
    show_banner (cl=cl)
    opt (cl=cl)

if __name__ == '__main__': main ()
