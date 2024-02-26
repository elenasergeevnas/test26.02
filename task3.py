import csv

with open ('students.csv', 'r',  encoding = 'utf8') as file:
    reader = csv.reader(file, delimiter = ',')

    id_project = input()
    while id_project != "СТОП":
        for id, name, titleProject_id, _class, score in reader:
            if id_project == titleProject_id:
                famil, nam, otch = name.split()
                print(f"Проект №: {titleProject_id} делал {nam[0]}. {famil} он(а) получил(а) оценку - {score}.")
                break
        else:
            print("Ничего не найдено")

        id_project = input()

