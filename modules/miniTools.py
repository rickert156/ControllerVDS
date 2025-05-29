import csv
from modules.colors import RED, RESET

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


