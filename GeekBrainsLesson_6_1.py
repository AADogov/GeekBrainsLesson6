# 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера
# nginx_logs.txt
## (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список
# кортежей вида: (<remote_addr>, <request_type>, <requested_resource>)
# Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
# ----------Решение-------------

with open("nginx_logs[1].txt", 'r') as f:
    # открываем файл nginx_logs[1].txt с помощью with
    for line in f:
        # построчно читаем файл nginx_logs[1].txt. Заменяем в строке все интересующие нас разделитили:' - - ','"',
        # ' ', на набор символов который не может встретиться в файле '++++', и по этому же набору проводим
        # разделение. полученый список записываем в line_list
        line_list = line.replace(' - - ', '++++').replace('"', '++++').replace(' ', '++++').split('++++')
        # в переменную remote_addr заносим нулевой элемент списка line_list
        remote_addr = line_list[0]
        # в переменную request_type заносим 4 элемент списка line_list
        request_type = line_list[4]
        # в переменную requested_resource заносим 5 элемент списка line_list
        requested_resource = line_list[5]
        # Создаем кортеж result
        result=(remote_addr, request_type, requested_resource)
        # Если файл не помешается в оперативную память то и список кортежей не поместится в память тоже
        # можно реализовать зпись в файл построчно, но я просто вывожу на экран так же построчно.
        print(result)
