from colorama import *
import os
import requests
import random
import string
import time

init(convert=True)

# Constantes
plus = f'{Fore.MAGENTA}[{Fore.RESET}+{Fore.MAGENTA}]{Fore.RESET}'
minus = f'{Fore.MAGENTA}[{Fore.RESET}-{Fore.MAGENTA}]{Fore.RESET}'
wait = f'{Fore.GREEN}[{Fore.RESET}/{Fore.GREEN}]{Fore.RESET}'
error = f'{Fore.LIGHTRED_EX}[{Fore.RESET}!{Fore.LIGHTRED_EX}]{Fore.RESET}'

# Functions


def leave():
    clear()
    banner()
    print("")
    print(f'{plus} Made by Zack aka Silence, thanks.')


def clear():
    if (os.name == "nt"):
        os.system('cls')
    else:
        os.system('clear')


def error(failed):
    print(f'{error} {failed}. Intentalo de nuevo.')
    time.sleep(2)
    menu()


def forceExit():
    print("")
    print("")
    print(
        f'{Fore.LIGHTBLUE_EX}[{Fore.WHITE}!{Fore.LIGHTBLUE_EX}] Adios y gracias por usar Extasis Spammer')
    time.sleep(2)
    leave()


def banner():
    _banner = """
▄▄ .▐▄• ▄ ▄▄▄▄▄ ▄▄▄· .▄▄ · ▪  .▄▄ ·     .▄▄ ·  ▄▄▄· ▄▄▄· • ▌ ▄ ·. 
▀▄.▀· █▌█▌▪•██  ▐█ ▀█ ▐█ ▀. ██ ▐█ ▀.     ▐█ ▀. ▐█ ▄█▐█ ▀█ ·██ ▐███▪
▐▀▀▪▄ ·██·  ▐█.▪▄█▀▀█ ▄▀▀▀█▄▐█·▄▀▀▀█▄    ▄▀▀▀█▄ ██▀·▄█▀▀█ ▐█ ▌▐▌▐█·
▐█▄▄▌▪▐█·█▌ ▐█▌·▐█ ▪▐▌▐█▄▪▐█▐█▌▐█▄▪▐█    ▐█▄▪▐█▐█▪·•▐█ ▪▐▌██ ██▌▐█▌
 ▀▀▀ •▀▀ ▀▀ ▀▀▀  ▀  ▀  ▀▀▀▀ ▀▀▀ ▀▀▀▀      ▀▀▀▀ .▀    ▀  ▀ ▀▀  █▪▀▀▀
    """
    print(f"{Fore.MAGENTA}")
    print(_banner)
    print(
        f"{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}</>{Fore.LIGHTMAGENTA_EX}] Developed by Zack AKA Silence")


def menu():
    clear()
    banner()
    os.system("@title [-] Extasis Webhook Spammer #Loyalty")
    print('')
    print('')
    print(f'{plus} Ingrese la webhook: ', end=f'{Fore.RESET}')
    hook = input()
    print(f'{plus} Ingrese el nombre de la webhook: ', end=f'{Fore.RESET}')
    nameHook = input() or "Loyalty"
    print(f'{plus} Ingrese el mensaje a enviar: ', end=f'{Fore.RESET}')
    message = input()
    print(F'{plus} Cantidad de mensajes a enviar: ', end=f'{Fore.RESET}')
    numHook = int(input())
    print(f'{plus} Ingrese el nombre de la avatar de la webhook (opcional): ',
          end=f'{Fore.RESET}')
    avWebhook = input()
    data = {}
    if avWebhook == "":
        data = {
            'content': message,
            'avatar_url':  "https://cdn.discordapp.com/icons/1078819884252807168/753a3c18b20128efb026e7133eca4d86.png?size=2048",
            'username': nameHook
        }
    else:
        data = {
            'content': message,
            'avatar_url': avWebhook,
            'username': nameHook
        }
    try:
        cant = 0
        while cant < numHook:
            req = requests.post(hook, json=data)
            cant += 1
            if req.status_code == 204:
                print(f'{plus} Sended message: {message}')
            elif req.status_code == 401:
                print(f'{error} Hubo un error.')
        print(f'{plus} SPAM Terminado.')
        input()
        menu()

    except KeyboardInterrupt:
        forceExit()
    except:
        print(f'{error} Hubo un error')


try:
    menu()
except KeyboardInterrupt:
    forceExit()
