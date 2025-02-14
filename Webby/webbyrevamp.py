import pystyle
import colorama
import os
import requests
import subprocess
import ctypes
import random
import time
from tqdm import tqdm

from colorama import *
from pystyle import *

colorama.init()

username = os.getlogin()
version = "0.1.0"

webhook_url = ""

def loading_screen():
    # Set the total to 100 to simulate a full 100% progress
    Write.Print("Loading Webby...", Colors.blue_to_purple, interval=0.001)
    time.sleep(1)  # Simulating a brief delay before showing the progress bar
    for _ in tqdm(range(100), desc="Loading", ncols=100, bar_format="{l_bar}{bar}|", leave=False):
        time.sleep(0.05)  # Simulating a task that takes time

def WebhookUse(webhook):
    global webhook_url
    webhook_url = webhook
    print(f"{Fore.GREEN}[INFO] Webhook URL set to: {webhook_url}{Style.RESET_ALL}")

def Sendmsg(message):
    if webhook_url:
        data = {
            "content": message
        }
        response = requests.post(webhook_url, json=data)
        if response.status_code == 204:
            print(f"{Fore.GREEN}[SUCCESS] Message sent successfully!{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[ERROR] Failed to send message. Status code: {response.status_code}{Style.RESET_ALL}")
    else:
        print(f"{Fore.YELLOW}[WARNING] Please set a webhook URL first using the 'WebhookUse' command.{Style.RESET_ALL}")

def Sendembed(args):
    if webhook_url:
        author = args[0] if args[0] != "nil" else None
        author_url = args[1] if args[1] != "nil" else None
        author_icon_url = args[2] if args[2] != "nil" else None
        title = args[3] if args[3] != "nil" else "Untitled Embed"
        description = args[4] if args[4] != "nil" else "No description provided."
        url = args[5] if args[5] != "nil" else None
        color = int(args[6]) if args[6] != "nil" else random.randint(0, 16777215)
        image_url = args[7] if args[7] != "nil" else None
        thumbnail_url = args[8] if args[8] != "nil" else None
        footer = args[9] if args[9] != "nil" else None
        footer_icon_url = args[10] if args[10] != "nil" else None
        timestamp = args[11] if args[11] != "nil" else None

        embed_data = {
            "author": {
                "name": author,
                "url": author_url,
                "icon_url": author_icon_url
            } if author else None,
            "title": title,
            "description": description,
            "url": url,
            "color": color,
            "image": {
                "url": image_url
            } if image_url else None,
            "thumbnail": {
                "url": thumbnail_url
            } if thumbnail_url else None,
            "footer": {
                "text": footer,
                "icon_url": footer_icon_url
            } if footer else None,
            "timestamp": timestamp
        }

        data = {
            "embeds": [embed_data]
        }

        response = requests.post(webhook_url, json=data)
        if response.status_code == 204:
            print(f"{Fore.GREEN}[SUCCESS] Embed sent successfully! Title: {title}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[ERROR] Failed to send embed. Status code: {response.status_code}{Style.RESET_ALL}")
    else:
        print(f"{Fore.YELLOW}[WARNING] Please set a webhook URL first using the 'WebhookUse' command.{Style.RESET_ALL}")

def Commands():
    while True:
        command = input(f"{Fore.LIGHTBLUE_EX}{username}{Fore.MAGENTA}@webby{Fore.CYAN}$ {Style.RESET_ALL}").strip()

        if command == "WebhookUse":
            webhook = input(f"{Fore.MAGENTA}Enter the webhook URL: {Style.RESET_ALL}").strip()
            WebhookUse(webhook)

        elif command == "Sendmsg":
            message = input(f"{Fore.MAGENTA}Enter the message: {Style.RESET_ALL}").strip()
            Sendmsg(message)

        elif command.startswith("Sendembed"):
            args = command.split()[1:]
            if len(args) == 12:
                Sendembed(args)
            else:
                print(f"{Fore.RED}Sendembed used incorrectly. Correct usage:{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}Sendembed <Author> <AuthorURL> <AuthorIconURL> <Title> <Description> <URL> <Color> <ImageURL> <ThumbnailURL> <Footer> <FOOTERICONURL> <TimeStamp>{Style.RESET_ALL}")

        elif command == "help":
            Write.Print('''
                            COMMANDS
            ╔══════════════════════════════════════════╗
            ║ WebhookUse - Set the Webhook URL.        ║
            ║ SendMsg - Send a message to the webhook. ║
            ║ Sendembed - Send an embed to the webhook.║
            ║ exit - Exit Webby.                       ║
            ╚══════════════════════════════════════════╝
            
            '''
            ,Colors.blue_to_purple, interval=0.001)

        elif command == "exit":
            print(f"{Fore.RED}[INFO] Exiting...{Style.RESET_ALL}")
            break

        else:
            print(f"{Fore.RED}[ERROR] Unknown command. Type 'help' for a list of commands.{Style.RESET_ALL}")

def Main():
    subprocess.run('cls', shell=True)
    ctypes.windll.kernel32.SetConsoleTitleW(f"Webby {version} || REVAMP")

    Write.Print(f'''
    ██╗    ██╗███████╗██████╗ ██████╗ ██╗   ██╗
    ██║    ██║██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝
    ██║ █╗ ██║█████╗  ██████╔╝██████╔╝ ╚████╔╝ 
    ██║███╗██║██╔══╝  ██╔══██╗██╔══██╗  ╚██╔╝  
    ╚███╔███╔╝███████╗██████╔╝██████╔╝   ██║   
     ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═════╝    ╚═╝ Discord Webhook Controller | REVAMPED
════════════════════════════════════════════════════════════════════════════════                                           
    ╔═════════════════════════════════════════════════╗
    ║  For help, use the command 'help'.              ║
    ╚═════════════════════════════════════════════════╝
    '''
    ,Colors.blue_to_purple, interval=0.000)

    Commands()

if __name__ == "__main__":
    Main()
