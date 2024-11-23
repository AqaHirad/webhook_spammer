from requests import post
from time import sleep
import threading
from os import system, name
from colorama import Fore

system('cls' if name == 'nt' else 'clear')

banner = f""" {Fore.RED}

┓ ┏  ┓ ┓     ┓   ┏┓              
┃┃┃┏┓┣┓┣┓┏┓┏┓┃┏  ┗┓┏┓┏┓┏┳┓┏┳┓┏┓┏┓
┗┻┛┗ ┗┛┛┗┗┛┗┛┛┗  ┗┛┣┛┗┻┛┗┗┛┗┗┗ ┛ 
                   ┛             
         By AqaHirad
 {Fore.WHITE} """
print(banner)

webhook = input(f'Webhook {Fore.RED}>{Fore.WHITE} ')
username = input(f'Username {Fore.RED}>{Fore.WHITE} ')
avatar_url = input(f'Avatar {Fore.RED}>{Fore.WHITE} ')
message = input(f'Message {Fore.RED}>{Fore.WHITE} ')
thread = int(input(f'thread {Fore.RED}>{Fore.WHITE} '))
sleep = int(input(f"Sleep {Fore.RED}>{Fore.WHITE} "))

def sendMass():
    while True:
        try:
            dataa = {
    "content":message,
    "username": username,
    "avatar_url": avatar_url
}
            data = post(url=webhook, json=dataa)
            if data.status_code == 204:
                print(f"({data.status_code}){Fore.GREEN} Message sent successFully {Fore.WHITE} ")
        except:
            print(f"({data.status_code}){Fore.RED} Failed to send message {Fore.WHITE}")
        sleep(sleep)
    
for x in range(thread):
    send = threading.Thread(target = sendMass)
    send.start()