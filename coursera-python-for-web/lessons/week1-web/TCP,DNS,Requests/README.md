# Vagrant и VirtualBox

## Конфиг VM с предустановленным софтом - см Vagrantfile в этом каталоге

```
$ sudo apt install vagrant virtualbox
$ vagrant up
$ vagrant ssh
```

# TCP\IP

## Cлушаем канал связи

```
$ sudo tcpdump -i lo port 3000 -v -A -n -e -K	# слушает
```

## Устанавливаем серверную часть

```
$ nc -l 127.0.0.1 3000					        # слушает, выводит принятое, можно писать ответы
```

## Три варианта клиента

```
$ telnet 127.0.0.1 3000					        # (TCP) пишем текст, Enter отправка, Ctrl+] выход
$ nc 127.0.0.1 3000						        # (TCP) пишем текст, Enter отправка
$ nc -u 127.0.0.1 3000					        # (UDP) пишем текст, Enter отправка, сам выйдет
```

# DNS

```
$ dig mail.ru                                   # А-записи
$ dig mx mail.ru                                # MX-запись
$ dig +trace mail.ru                            # трейс, но если есть dnsmasq - выдает только локалхост...
$ dig -x 202.12.27.33                           # узнаем DNS-имя по IP-адресу
```

# Requests

## Создаем внутри виртуалки ~/request.txt (мб можно и через Vagrantfile скопировать...)

```
GET / HTTP/1.1
Host: example.com
Connection: keep-alive
Cache-Control: max-age=0
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36
Upgrade-Insecure-Requests: 1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
```

## Открываем телнет, коннектимся и вставляем из файла запрос

```
$ telnet example.com 80
> Копируем и вставляем запрос из файла          # Правильный запрос, сервер ответит 200 OK и вернет HTML
```
