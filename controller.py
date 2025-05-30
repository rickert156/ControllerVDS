from modules.colors import RED, RESET, GREEN
from modules.helper import helper
from modules.request import initRequest
from modules.miniTools import (
               ListServersCSV,
               ListServersTXT,
               greet
               )
from modules.mailer.check import checkCount
from modules.mailer.divide import DivideBase
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
                if '.csv' in servers:list_servers = ListServersCSV(doc=servers)
                if '.txt' in servers:list_servers = ListServersTXT(doc=servers)

                initRequest(list_servers=list_servers, command=command)
        
        elif len(params) == 3 and params[1] == "--command":
            """
            Если пытаемся использовать произвольную команду,
            но делаем это через одно место!
            """
            print(helper())

            ############################################################ 
            # Ниже идут модули, решающие задачи серверов для рассылки.
            # Совместимо c инструментом для рассылки из этого репозитория:
            # https://github.com/Rickert155/Mailing за небольшим 
            # исключеним - для свободной версии стоит поправить основную
            # директорию на c Mailing на CustomMailing
            ############################################################ 
            

        elif len(params) == 3 and params[1] == "--check-count":
            """Проверка количества имейлов в базе/количество отправленных писем"""
            servers = params[2]
            if '.csv' in servers:list_servers = ListServersCSV(doc=servers)
            if '.txt' in servers:list_servers = ListServersTXT(doc=servers)
            checkCount(list_servers=list_servers)

        elif len(params) == 2 and params[1] == "--check-count":
            print(helper())


        elif len(params) == 4 and params[1] == "--divide-base":
            """Разделение базы(CSV) на несколько равных частей"""
            base = params[2]
            try:
                count_base = int(params[3])
                """Принимаем только CSV базы"""
                if '.csv' in base:
                    DivideBase(base=base, count_base=count_base)

            except ValueError:
                print(
                        f"{RED}Последним параметром необходимо передать "
                        f"количество файлов, на которое будет разделена "
                        f"исходная база!{RESET}")
                print(helper())

        elif "--divide-base" in params and len(params) != 4:
            print(helper())


        elif len(params) == 1:
            print(helper())
    
    except KeyboardInterrupt:
        print(f"{RED}\nExit...{RESET}")

ControllerVDS()


