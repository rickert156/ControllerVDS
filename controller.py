from modules.colors import RED, RESET, GREEN
from modules.helper import helper
from modules.request import initRequest
from modules.miniTools import (
               ListServersCSV,
               ListServersTXT,
               greet
               )
import sys

def ControllerVDS():
    try:
        greet()
        params = sys.argv
        """Произвольная команда"""
        if len(params) == 4 and params[1] == "--command":
            if '.csv' in params[2] or '.txt' in params[2]:
                servers = params[2]
                command = params[3]
                if '.csv' in servers:
                    list_servers = ListServersCSV(doc=servers)
                if '.txt' in servers:
                    list_servers = ListServersTXT(doc=servers)

                initRequest(list_servers=list_servers, command=command)
    
        elif len(params) == 3 and params[1] == "--command":
            print(
                    f"{RED}Необходимо добавить файл и ввести "
                    f"команду с переменной в скобках {{server}} !{RESET}")
            print(helper())

        elif len(params) == 1:
            print(helper())
    
    except KeyboardInterrupt:
        print(f"{RED}\nExit...{RESET}")

ControllerVDS()


