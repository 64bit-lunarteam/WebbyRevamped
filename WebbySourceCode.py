import pystyle
import colorama
import os
import requests
import subprocess
import ctypes
import random
import time
import sys
from tqdm import tqdm
from colorama import Fore, Style
from pystyle import Write, Colors

# Fix for PyInstaller windowed mode (stdout/stderr issue)
if sys.stdout is None:
    sys.stdout = open("output.log", "w")
if sys.stderr is None:
    sys.stderr = open("error.log", "w")

colorama.init()

username = os.getlogin()
version = "0.1.0"
webhook_url = ""

def loading_screen():
    time.sleep(1)
    for _ in tqdm(range(100), desc="Loading", ncols=100, bar_format="{l_bar}{bar}|", leave=False):
        time.sleep(0.05)

def WebhookUse(webhook):
    global webhook_url
    webhook_url = webhook
    print(f"{Fore.GREEN}[INFO] Webhook URL set to: {webhook_url}{Style.RESET_ALL}")

def Sendmsg(message):
    if webhook_url:
        data = {"content": message}
        response = requests.post(webhook_url, json=data)
        if response.status_code == 204:
            print(f"{Fore.GREEN}[SUCCESS] Message sent successfully!{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[ERROR] Failed to send message. Status code: {response.status_code}{Style.RESET_ALL}")
    else:
        print(f"{Fore.YELLOW}[WARNING] Please set a webhook URL first using 'WebhookUse'.{Style.RESET_ALL}")

def Sendembed(args):
    if webhook_url:
        embed_data = {
            "author": {"name": args[0], "url": args[1], "icon_url": args[2]} if args[0] != "nil" else None,
            "title": args[3] if args[3] != "nil" else "Untitled Embed",
            "description": args[4] if args[4] != "nil" else "No description provided.",
            "url": args[5] if args[5] != "nil" else None,
            "color": int(args[6]) if args[6] != "nil" else random.randint(0, 16777215),
            "image": {"url": args[7]} if args[7] != "nil" else None,
            "thumbnail": {"url": args[8]} if args[8] != "nil" else None,
            "footer": {"text": args[9], "icon_url": args[10]} if args[9] != "nil" else None,
            "timestamp": args[11] if args[11] != "nil" else None,
        }

        response = requests.post(webhook_url, json={"embeds": [embed_data]})
        if response.status_code == 204:
            print(f"{Fore.GREEN}[SUCCESS] Embed sent successfully! Title: {args[3]}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[ERROR] Failed to send embed. Status code: {response.status_code}{Style.RESET_ALL}")
    else:
        print(f"{Fore.YELLOW}[WARNING] Set a webhook URL first using 'WebhookUse'.{Style.RESET_ALL}")

def Commands():
    while True:
        command = input(f"{Fore.LIGHTBLUE_EX}{username}{Fore.MAGENTA}@webby{Fore.CYAN}$ {Style.RESET_ALL}").strip()
        if command == "WebhookUse":
            WebhookUse(input(f"{Fore.MAGENTA}Enter the webhook URL: {Style.RESET_ALL}").strip())
        elif command == "Sendmsg":
            Sendmsg(input(f"{Fore.MAGENTA}Enter the message: {Style.RESET_ALL}").strip())
        elif command.startswith("Sendembed"):
            args = command.split()[1:]
            if len(args) == 12:
                Sendembed(args)
            else:
                print(f"{Fore.RED}Incorrect usage of 'Sendembed'. Check syntax.{Style.RESET_ALL}")
        elif command == "help":
            Write.Print('''
                            COMMANDS
            ╔══════════════════════════════════════════╗
            ║ WebhookUse - Set the Webhook URL.        ║
            ║ Sendmsg - Send a message to the webhook. ║
            ║ Sendembed - Send an embed to the webhook.║
            ║ exit - Exit Webby.                       ║
            ╚══════════════════════════════════════════╝
            ''', Colors.blue_to_purple, interval=0.000)
        elif command == "exit":
            print(f"{Fore.RED}[INFO] Exiting...{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}[ERROR] Unknown command. Type 'help' for a list of commands.{Style.RESET_ALL}")

def Main():

    # Prevent errors in `--windowed` mode
    if sys.stdout:
        subprocess.run('cls', shell=True)

    # Set console title (only if running in a console)
    try:
        ctypes.windll.kernel32.SetConsoleTitleW(f"Webby {version} || REVAMP")
    except:
        pass  # Ignore errors in windowed mode

    # Prevent crash in `--windowed` mode
    if sys.stdout:
        Write.Print(f'''
        ██╗    ██╗███████╗██████╗ ██████╗ ██╗   ██╗
        ██║    ██║██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝
    ╔═══██║ █╗ ██║█████╗  ██████╔╝██████╔╝ ╚████╔╝════════════════════════════════════════════╗ 
    ║   ██║███╗██║██╔══╝  ██╔══██╗██╔══██╗  ╚██╔╝                                            ╔╝
    ║   ╚███╔███╔╝███████╗██████╔╝██████╔╝   ██║                                            ╔╝ 
    ║    ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═════╝    ╚═╝ Discord Webhook Controller | REVAMPED     ╔╝
    ╚══════════════════════════════════════════════════════════════════════════════════════╝                                    
        ╔═════════════════════════════════════════════════╗
        ║  For help, use the command 'help'.              ║
        ╚═════════════════════════════════════════════════╝
        ''', Colors.blue_to_purple, interval=0.000)

    Commands()

if __name__ == "__main__":
    Main()
