import csv
import random

def generate_login(name):
    '''
    генерирует логин
    :param name: строка вида "Иванов Семен Петрович"
    :return: строка вида "Иванов_СП"
    '''
    sername, nam1, nam2 = name.split()
    return f'{sername}_{nam1[0]}{nam2[0]}'

def generate_password():
    '''
    генерация пароля  из случайных символов строчн и заглавных англ букв и цифр
    :return: пароль длины 8
    '''
    alph = 'qwertyuiopasdfghjklzxcvbnm'
    alph += alph.upper() + '1234567890'
    return ''.join([random.choice(alph) for _ in range(8)])

#создаем список для новой строки
s = []
#открываем файл на чтение
with open('students.csv', encoding='utf8') as f:
    reader = list(csv.reader(f, delimiter = ','))[1:]
#идем по файлу и в каждую строку добавляем в конец логин и пароль
    for row in reader:
        row.append(generate_login(row[1]))
        row.append(generate_password())
        s.append(row)
#записываем новый файл с нужным именем и новыми полями (логин и пароль)
with open('students_password.csv', 'w', newline = '',  encoding='utf8') as nf:
    nf = csv.writer(nf, delimiter=',')
    nf.writerow(['id','Name','titleProject_id','class','score', 'login', 'password'])
    nf.writerows(s)

