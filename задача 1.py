import csv

# открыть
with open('students.csv', encoding='utf8') as file:
    reader = list(csv.reader(file, delimiter=','))[1:]

    sum_class = {}
    count_class = {}

    for id, name, titleProject_id, _class, score in reader:
        if 'Хадаров Владимир' in name:
            print(f"Ты получил: {score}, за проект - {titleProject_id}")
            break
    # считаем среднее значение по классу (None считаем как 0)
    for elem in reader:
        if elem[-1] != 'None':
            sum_class[elem[-2]] = sum_class.get(elem[-2], 0) + int(elem[-1])
        count_class[elem[-2]] = count_class.get(elem[-2], 0) + 1
    # заменяем None на средние значения по классу
    for elem in reader:
        if elem[-1] == 'None':
            elem[-1] = round(sum_class[elem[-2]] / count_class[elem[-2]], 3)

# запишем новый файл
with open('students1.csv', 'w', encoding='utf8', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['id', 'Name', 'titleProject_id', 'class', 'score'])
    writer.writerows(reader)
