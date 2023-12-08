#1. Прочитать в виде списков набор данных titanic.csv, взятый из открытых источников:
#https://tproger.ru/translations/the-best-datasets-for-machine-learning-and-data-science/
#https://vc.ru/ml/150241-15-proektov-dlya-razvitiya-navykov-raboty-s-mashinnym-obucheniem
#https://archive.ics.uci.edu/ml/index.php
#https://habr.com/ru/company/edison/blog/480408/
#https://www.kaggle.com/datasets/
#2. Для прочитанного набора выполнить обработку в соответствии со своим вариантом. Библиотекой pandas пользоваться нельзя.
#Определить количество мужчин и женщин на борту и сколько из них выжило.


import csv

def read_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        data = [row for row in reader]
    return header, data

def count_gender_and_survival(data, header):
    gender_index = header.index('Sex')
    survived_index = header.index('Survived')

    male_count = 0
    female_count = 0
    male_survived = 0
    female_survived = 0

    for row in data:
        if row[gender_index].lower() == 'male':
            male_count += 1
            if row[survived_index] == '1':
                male_survived += 1
        elif row[gender_index].lower() == 'female':
            female_count += 1
            if row[survived_index] == '1':
                female_survived += 1

    return male_count, female_count, male_survived, female_survived

file_path = 'titanic.csv'
header, data = read_csv(file_path)
male_count, female_count, male_survived, female_survived = count_gender_and_survival(data, header)

print("Количество мужчин на борту:", male_count)
print("Количество женщин на борту:", female_count)
print("Общее количество людей на борту:", male_count+female_count)
print()
print("Количество выживших мужчин:", male_survived)
print("Количество выживших женщин:", female_survived)
print("Общее количество выживших людей:", male_survived+female_survived)