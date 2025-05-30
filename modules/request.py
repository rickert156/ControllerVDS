from modules.miniTools import (
        run_command,
        divide_block
        )

def initRequest(list_servers:list, command:str):
    base_commamd = command
    number_server = 0
    for server in list_servers:
        number_server+=1
        if "{server}" in command:command = command.replace("{server}", server)
        print(command)
        #run_command(command=command, number=number_server)
        print(divide_block())

        """Возвращаем изначальное значение команды"""
        command = base_commamd
        



