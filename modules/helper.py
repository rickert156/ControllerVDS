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
    
    --check-count           Параметр применяется к серверам для рассылки.
                            Отображает количество имейлов в базе и количество
                            отправленных писем. Более подробная информация в
                            ControllerVDS/README.md. Вторым параметром передать
                            файл csv или txt с серверами. Пример:
                            {GREEN}python3 controller.py --check-count server.txt{RESET}
    """
    return text
