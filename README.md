# Controller VDS
Данная утилита помогает работать с большим количеством серверов.  

## Возможности 

Можно передавать список серверов файлом txt или csv вместе с командой, которую нужно выполнить на всех серверах. Обязательно указать {server} как переменную
```sh
python3 controller.py --command server.txt 'ssh root@{server} "ls" &'
```
Вот так может выглядеть работа утилиты  
![img](https://raw.githubusercontent.com/rickert156/ControllerVDS/main/img/1.png)  

### Работа с серварами для рассылки
Утилита решает проблемы автоматизации серверов для рассылки, совместимых с рассыльщиком [https://github.com/Rickert155/Mailing](https://github.com/Rickert155/Mailing).  
Так как рассыльщик [Rickert155/Mailing](https://github.com/Rickert155/Mailing) является свободной модификацией закрытой версии, для корректной работы(со свободной версией) необходимо поправить значение переменной в modules/mailer/config.py
```sh
mail_dir = "Mailing" # Или на имя директории, которая у вас является корневой для рассылки
```
**Проверка количества имейлов в базе/количество отправленных писем**
```sh
python3 controller.py --check-count server.txt
```
Таким будет вывод:  
![img](https://raw.githubusercontent.com/rickert156/ControllerVDS/main/img/2.png)

