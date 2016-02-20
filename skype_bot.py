# coding: utf8

import Skype4Py
from sys import path
import os

path.append (os.path.realpath (os.path.dirname (__file__)) + '/modules/')

import bot
from output import *
import webbrowser

options = [
   'Skype Message Flood',
   'Skype Call Flood',
   'Show Friend List',
   'Start Auto Answering Machine'
]

def show_banner (cl=None):

    print Fore.CYAN + '''
    ╔══╦╗╔══╦╗╔╦═══╦═══╗
    ║╔═╣║║╔═╣║║║╔═╗║╔══╝
    ║╚═╣╚╝║─║╚╝║╚═╝║╚══╗
    ╚═╗║╔╗║─╚═╗║╔══╣╔══╝
    ╔═╝║║║╚═╗╔╝║║──║╚══╗
    ╚══╩╝╚══╝╚═╩╝──╚═══╝
    ╔══╗╔══╦════╗
    ║╔╗║║╔╗╠═╗╔═╝
    ║╚╝╚╣║║║─║║
    ║╔═╗║║║║─║║
    ║╚═╝║╚╝║─║║
    ╚═══╩══╝─╚╝
    ''' + Fore.RESET
    print Fore.RED + '[DEVELOPER]' + Fore.RESET + ' DOCTOR_RABB'
    print Fore.CYAN + '[VERSION]' + Fore.RESET + ' 0.15f'

    print INFO + 'EVIL-HACK.US' + INFO
    
    if raw_input ('Do you want to visit evil-hack.us? (y/n): ') == 'y': webbrowser.open ('http://evil-hack.us/')

    print '*'*70
    print ' '*15 + 'Your Name: ' + cl.CurrentUser.FullName + ' '*15
    print ' '*15 + 'Your Status: ' + cl.CurrentUserStatus + ' '*15
    print ' '*15 + 'Your Login: ' + cl.CurrentUser.Handle + ' '*15
    print '*'*70


def opt (cl=None):
	

    print
    for i in range (len (options)): print options [i] + ' ' +  str (i)

    client = bot.BotM (cl)

    cmd = raw_input ( '\n' + INFO + 'Select option (99 to exit): ')
    if cmd == '99':
        exit ()
    elif cmd == '0':
        client.start_message_flood (raw_input (INFO + 'Target\'s login ("all" to circulate by friend list): '), raw_input (INFO + 'Message (null to random messages): '), int (raw_input (INFO + 'Delay: ')))
    elif cmd == '1':
        client.start_call_flood (raw_input (INFO + 'Target\'s login ("all" to circulate by friend list): '), int (raw_input (INFO + 'Delay: ')))
    elif cmd == '2':
        client.show_friend_list ()
    elif cmd == '3':
	client.start_auto_answering_machine (raw_input (INFO + 'Wav File for playing: '))
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
