from modules.miniTools import run_command

def addKey(servers:list, key:str):
    number_server = 0
    for server in servers:
        number_server+=1

        send_key = (
                f"echo '{key} auto' | ssh root@{server} "
                f"'mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys "
                f"&& chmod 600 ~/.ssh/authorized_keys'"
                )
        run_command(command=send_key, number=number_server)
