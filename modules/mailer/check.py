from modules.miniTools import (
        run_command,
        divide_block
        )
from modules.mailer.config import mail_dir

def checkCount(list_servers:list):
    number_server = 0
    for server in list_servers:
        number_server+=1
        command = (
                   f'ssh root@{server} "cd CustomMailing && '
                   f'cat Done/* | wc && cat Base/* | wc"'
                   )
        run_command(command=command, number=number_server)

