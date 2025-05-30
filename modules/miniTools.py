import csv, subprocess
from modules.colors import RED, RESET, GREEN
import __init__

def divide_block():
    divide = "-"*80
    return divide

def greet():
    text = (
            f"{GREEN}Author:\t\t{__init__.__author__}\n"
            f"Version:\t{__init__.__version__}\n{RESET}"
            )
    print(text)

def ListServersCSV(doc:str):
    list_servers = []
    with open(doc, 'r') as file:
        for row in csv.DictReader(file):
            if 'IP' in row:
                ip = row['IP']
                if ip not in list_servers:
                    list_servers.append(ip)
            else:
                print(f"{RED}Нет колонки 'IP'!{RESET}")
                return

    return list_servers
            

def ListServersTXT(doc:str):
    list_servers = []
    with open(doc, 'r') as file:
        for line in file.readlines():
            server = line.strip()
            if server not in list_servers:
                list_servers.append(server)

    return list_servers

def run_command(command:str, number:int=None):
    print(f"{GREEN}[{number}] {command}{RESET}")
    subprocess.run(command, shell=True)
