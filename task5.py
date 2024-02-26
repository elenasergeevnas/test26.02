import csv
def gen_hash(s: str):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    d = {n: i for i, n in enumerate(alphabet, 1)}
    p = 67
    m = 10**9 + 9
    hash_value = 0
    p_pow = 1
    for c in s:
        hash_value = (hash_value + d[c] *p_pow) % m
        p_pow = (p_pow * p) % m
    return int(hash_value)


students_with_hash = []
with open('students.csv', encoding = 'utf8') as f:
    reader = list(csv.reader(f, delimiter = ','))[1:]
    for row in reader:
        row[0] = gen_hash(row[1])
        students_with_hash.append(row)

with open ('students_with_hash.csv', 'w', newline='', encoding = 'utf8') as file:
    w = csv.writer(file)
    w.writerow('id,Name,titleProject_id,class,score')
    w.writerows(students_with_hash)

