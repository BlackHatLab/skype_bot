# This module contains "color themes" for console output

from colorama import Fore, init

init ()

NO = Fore.RED + '[-] ' + Fore.RESET
INFO = Fore.CYAN + '[*] ' + Fore.RESET
YES = Fore.GREEN + '[+] ' + Fore.RESET
ERR = Fore.RED + '[!] ' + Fore.RESET
