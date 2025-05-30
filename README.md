# Controller VDS
Данная утилита помогает работать с большим количеством серверов.  

## Возможности 

Можно передавать список серверов файлом txt или csv вместе с командой, которую нужно выполнить на всех серверах. Обязательно указать {server} как переменную
```sh
python3 controller.py --command server.txt 'ssh root@{server} "ls" &'
```
Вот так может выглядеть работа утилиты
![img](http:/github.com/rickert156/ControllerVDS/blob/main/img/1.png)
