from modules.miniTools import (
        run_command,
        divide_block
        )

def initRequest(list_servers:list, command:str):
    base_commamd = command
    for server in list_servers:
        if "{server}" in command:command = command.replace("{server}", server)
        run_command(command=command)
        print(divide_block())

        """Возвращаем изначальное значение команды"""
        command = base_commamd
        



