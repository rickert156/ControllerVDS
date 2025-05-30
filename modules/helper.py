from modules.colors import GREEN, RESET

def helper():
    text = f"""\
    --command               Передача произвольной команды. Первыми параметром
                            необходимо передать файл txt или csv. Вторым 
                            параметром в кавычках передать команду. В фигурных
                            скобках {{}} необходимо указать server, как
                            переменную. Пример:
                            {GREEN}python3 controller.py --command server.txt "ls -l"
                            {RESET}
    """
    return text
