from modules.mailer.config import (
        done_dir, 
        base_dir,
        mail_dir
        )
from modules.miniTools import run_command
import os, shutil

def ListBase():
    list_base = []
    for base in os.listdir(base_dir):
        if '.csv' in base:
            base = f"{base_dir}/{base}"
            if base not in list_base:list_base.append(base)
    return list_base 

def moveBase(path_base:str):
    if not os.path.exists(done_dir):os.makedirs(done_dir)
    base = path_base.split('/')[1]
    move_base_path = f"{done_dir}/{base}"
    shutil.move(path_base, move_base_path)


def CopyBase(servers:str):
    list_base = ListBase()

    number_base = 0
    for base, server in zip(list_base, servers):
        number_base+=1
        command = f"scp {base} root@{server}:~/{mail_dir}/{base_dir}/"
        print(f"[{number_base}] {server}\t{base}")
        run_command(command=command, number=number_base)
        moveBase(path_base=base)
