import re


def start():
    '''Функция выдает пользователю опции работы с данным файлом и в зависимости от его выбора вызывает
    другую функцию, выплняющую соответствующие действия'''
    print('Выберете вариант:')
    print('1.Вывести в понятном виде иерархию команд, т.е. департамент и все команды, которые входят в него')
    print(
        '2.Вывести сводный отчёт по департаментам: название, численность, "вилка" зарплат в виде мин – макс, среднюю зарплату')
    print(
        '3.Сохранить сводный отчёт из предыдущего пункта в виде csv-файла. При этом необязательно вызывать сначала команду из п.2')
    option = ''
    options = {'1': 1, '2': 2, '3': 3}
    while option not in options:
        print('Выберите: {}/{}/{}'.format(*options))
        option = input()

    if options[option] == 1:
        return show_hierarchy()
    elif options[option] == 2:
        return show_report()
    else:
        return save_report()


def from_csv_to_list_of_dictionaries():
    '''Функция переводит исходный файл в список словарей'''
    csv = open('Corp_Summary.csv')
    list_csv = csv.readlines()
    list_of_dictionaries = []
    keys_csv = re.split(';|\n', list_csv[0])
    for i in range(1, len(list_csv)):
        one_line = re.split(';|\n', list_csv[i])
        dictionary = dict()
        dictionary[keys_csv[0]] = one_line[0]
        dictionary[keys_csv[1]] = one_line[1]
        dictionary[keys_csv[2]] = one_line[2]
        dictionary[keys_csv[3]] = one_line[3]
        dictionary[keys_csv[4]] = one_line[4]
        dictionary[keys_csv[5]] = one_line[5]
        list_of_dictionaries.append(dictionary)
    return list_of_dictionaries


def make_list_of_departments():
    '''Функция делает список департаментов'''
    list_of_dictionaries = from_csv_to_list_of_dictionaries()
    departments_set = set()
    for dicts in list_of_dictionaries:
        departments_set.add(dicts['Департамент'])
    return departments_set


def show_hierarchy():
    '''Если пользователь выбирает 1, то выводит в понятном виде иерархию команд, т.е. департамент
    и все команды, которые входят в него'''
    list_of_dictionaries = from_csv_to_list_of_dictionaries()
    departments_set = make_list_of_departments()
    teams = []
    for dicts in list_of_dictionaries:
        dictionary2 = dict()
        dictionary2[dicts['Департамент']] = dicts['Отдел']
        teams.append(dictionary2)
    for department in departments_set:
        set_teams = set()
        for i in teams:
            set_teams.add(i.get(department, 0))
        set_teams.remove(0)
        print(f'Команды, которые входят в департамент {department}:', end='\n')
        print(*set_teams, sep='\n')


def show_report():
    '''Если пользователь выбирает 2, то выводит сводный отчёт по департаментам: название, численность,
    "вилка" зарплат в виде мин – макс, среднюю зарплату'''
    list_of_dictionaries = from_csv_to_list_of_dictionaries()
    report = dict()
    report_file = []
    departments_set = make_list_of_departments()
    for dicts in list_of_dictionaries:
        if dicts['Департамент'] in report.keys():
            report[dicts['Департамент']][0] += 1
        else:
            report[dicts['Департамент']] = [0, [], 0, 0, 0]
        report[dicts['Департамент']][1].append(int(dicts['Оклад']))
    for department in departments_set:
        report[department][2] = min(report[department][1])
        report[department][3] = max(report[department][1])
        report[department][4] = sum(report[department][1]) / report[department][0]
        del report[department][1]
    for department in departments_set:
        report_file.append(f'Отчет по департаменту {department}:')
        report_file.append(f'Количество человек: {report[department][0]}')
        report_file.append(f'Вилка зарплат: {report[department][1]}-{report[department][2]}')
        report_file.append(f'Средняя зарплата: {report[department][3]}')
    print(*report_file, sep='\n')
    return report_file


def save_report():
    '''Если пользователь выбирает 3, то функция сохраняет сводный отчёт из предыдущего пункта в виде csv-файла'''
    report = show_report()
    departments_set = list(make_list_of_departments())
    with open('report.csv', 'w+') as f:
        f.write('Отчет по департаменту:')
        f.write(';')
        f.write('\n')
        for i in range(len(departments_set)):
            f.write(departments_set[i])
            f.write(';')
        f.write('\n')
        for i in range(1, len(report), 4):
            f.write(report[i])
            f.write(';')
        f.write('\n')
        for i in range(2, len(report), 4):
            f.write(report[i])
            f.write(';')
        f.write('\n')
        for i in range(3, len(report), 4):
            f.write(report[i])
            f.write(';')


if __name__ == '__main__':
    start()
