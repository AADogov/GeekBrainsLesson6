# 6. Реализовать простую систему хранения данных о суммах продаж булочной. Должно быть два скрипта с интерфейсом
# командной строки: для записи данных и для вывода на экран записанных данных. При записи передавать из командной
# строки значение суммы продаж. Для чтения данных реализовать в командной строке следующую логику:

# просто запуск скрипта — выводить все записи; запуск скрипта с одним параметром-числом — выводить все записи с
# номера, равного этому числу, до конца; запуск скрипта с двумя числами — выводить записи, начиная с номера,
# равного первому числу, по номер, равный второму числу, включительно.

# 7. * (вместо 6) Добавить возможность
# редактирования данных при помощи отдельного скрипта: передаём ему номер записи и новое значение. При этом файл не
# должен читаться целиком — обязательное требование. Предусмотреть ситуацию, когда пользователь вводит номер записи,
# которой не существует.

# ----------Решение-------------
# Задачи 6_6 и 6_7 решаются совместно

import sys


# реализуем функцию read  котоарая выводит список данных с параметрами  записи, начиная с номера  первого числа - start
# и по номер, равный второму числу, включительно - end
def read(start, end):
    # Создаем список result
    result = []
    with open('bakery.csv', 'r', encoding='utf8') as f1:
        # открываем файл bakery.csv
        # данные в файл я записал по следуюшему формату "{:010.2f}\n".format(data), одно число в строке
        # а это значит что в строке 12 символов 10 на число и 2 на начало и конец строки
        # переносим курсор на позицию по формуле (start - 1) * 12 , -1 для того чтобы номер можно было начинать с 1
        f1.seek((start - 1) * 12)
        # запускаем цикл по i от 0 до end - start + 1
        for i in range(0, end - start + 1):
            # заносим во временную переменную temp 11 символов строки и вызываем метод .strip() для того чтобы
            # срезать "хвосты"
            temp = f1.read(11).strip()
            if temp != '':
                # если переменная temp не пустая строка конвертируем ее во float и добавляем в result
                result.append(float(temp))
    # Возвращаем result
    return result


# реализуем функцию read_to_end  котоарая выводит список данных из всех записей с номера, равного этому числу, до конца
# с параметром  start- номер позиции
# далее как в функции read
def read_to_end(start):
    result = []
    with open('bakery.csv', 'r', encoding='utf8') as f1:
        f1.seek((start - 1) * 12)
        temp = f1.readline()
        while temp != '':
            # цикл будет выполнятся пока temp не пустая строка
            result.append(float(temp))
            temp = f1.readline()
    return result


# реализуем функцию read_all котоарая выводит список всех данных
def read_all():
    # вызвываем функцию read_to_end с параметром 1
    return read_to_end(1)


# реализуем функцию read_one котоарая выводит одно число по конкретному номеру
def read_one(start):
    return read(start, start)


# реализуем функцию write котоарая заменяет одно число по конкретному номеру на новое число задача 6_7
# параметры position номер числа ктороый нужно изменить и data - число на которое необходимо сделать замену
# по условию файл не должен читаться целиком — обязательное требование
def write(position, data):
    with open('bakery.csv', 'r', encoding='utf8') as f1:
        # откроем файл на чтение и ститаем в нем все символы
        # от начала до (position - 1) * 11 во вреенную переменную temp
        # файл не читается целиком а читается только до нужной позиции
        temp = f1.read((position - 1) * 11)
        # добавляем к пременной temp новое число по нужному формату
        temp += "{:010.2f}\n".format(data)

    with open('bakery.csv', 'r+') as f1:
        # открываем файл на запись и записываем в него пременную temp, данные запишутся по верх страрых данных если
        # пользователь вводит номер записи, которой не существует данные запишутся в конец файла
        f1.write(temp)
    # возвращаем код 0 если все прошло нормально
    return 0


# реализуем функцию вывода списка
def list_to_string(list_float):
    if len(list_float) > 0:
        return "\n".join(str(x) for x in list_float)
    else:
        return "There is no data"


# реализуем интерфейс
if len(sys.argv) >= 4 and sys.argv[1] == 'write':
    # если у нас в строке 4 аргумента и первый мз них 'write'
    if write(int(sys.argv[2]), float(sys.argv[3])) == 0:
        # если функция write вернула 0 то все прошло успешно
        # выводим сообщение о записи
        print(f'data {float(sys.argv[3])} has been written in to position {sys.argv[2]}')
    else:
        # в противном случае выводим предупреждение
        print('something went wrong, pleas chek the file bakery.csv')
elif len(sys.argv) == 3:
    # если у нас в строке 3 аргумента
    if int(sys.argv[2]) >= int(sys.argv[1]):
        # и второй аргумеент больше первого
        # вызываем функцию list_to_string в которую передаем параметром функцию
        # read в котороую передаем параметрами аргументы 1 и 2
        print(list_to_string(read(int(sys.argv[1]), int(sys.argv[2]))))
    else:
        # в противном случае выводим предупреждение
        print("The second argument must be equal to or greater than the first")
elif len(sys.argv) == 2:
    # если у нас в строке 2 аргумента
    # вызываем функцию list_to_string в которую передаем параметром функцию
    # read_to_end в котороую передаем параметрами аргумент 1
    print(list_to_string(read_to_end(int(sys.argv[1]))))
elif len(sys.argv) < 2:
    # если у нас в строке меньше 2 аргументов
    # вызываем функцию read_all в которую передаем параметром функцию
    # read_to_end в котороую передаем параметрами аргумент 1
    print(list_to_string(read_all()))
