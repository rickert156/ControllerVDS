from modules.colors import RED, RESET, GREEN
from modules.miniTools import (
               ListServersCSV,
               ListServersTXT
               )
import sys

def ControllerVDS():
    params = sys.argv
    if len(params) == 4 and params[1] == "--command":
        if '.csv' in params[2] or '.txt' in params[2]:
            servers = params[2]
            command = params[3]
            print(command)
            if '.csv' in servers:
                list_servers = ListServersCSV(doc=servers)
            if '.txt' in servers:
                list_servers = ListServersTXT(doc=servers)
    
    elif len(params) == 3 and params[1] == "--command":
        print(
                f"{RED}Необходимо добавить файл и ввести "
                f"команду с переменной в скобках {{server}} !{RESET}")

ControllerVDS()


