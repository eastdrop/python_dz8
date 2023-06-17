def get_info():
    info = []
    last_name = input('Введите фамилию: ')
    info.append(last_name)
    first_name = input('Введите имя: ')
    info.append(first_name)
    phone_number = ''
    valid = False
    while not valid:
        try:
            phone_number = input('Введите номер телефона: ')
            if len(phone_number) != 11:
                print('В номере телефона должно быть 11 цифр.')
            else:
                phone_number = int(phone_number)
                valid = True
        except:
            print('Номер телефона должен состоять только из цифр.')
    info.append(phone_number)
    description = input('Введите описание: ')
    info.append(description)
    return info

def writing_txt(info):
    file = 'Phonebook.txt'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(
            f'Фамилия: {info[0]}\n\nИмя: {info[1]}\n\nНомер телефона: {info[2]}\n\nОписание: {info[3]}\n\n\n')

def from_file(file):
    with open(file, 'r', encoding='utf-8') as data:
        dictionary = data.read()
    return dictionary

def creating():
    file = 'Phonebook.csv'
    with open(file, 'w', encoding='utf-8') as data:
        data.write(f'Фамилия;Имя;Номер телефона;Описание\n')

from os.path import exists

def choice():
    flag = input(
        'Для продолжения работы нажмите \'да\', или любой символ для завершения работы... ')
    while (flag.lower() == 'да'):
        path = 'Phonebook.txt'
        valid = exists(path)
        if not valid:
            creating()
        choice_action = input(
            'Введите \'да\', если хотите записать новые данные, и любой другой символ, если хотите просмотреть справочник в консоли: ')
        if choice_action.lower() == 'да':
            record_info()
        else:
            view()
        flag = input(
            'Для продолжения работы нажмите \'да\', или любой символ для завершения работы... ')
    print('Программа завершена.')

def view():
    print(from_file('Phonebook.txt'))

def record_info():
    info = get_info()
    writing_txt(info)



import os

os.system('cls')


def main():
    choice()


if __name__ == '__main__':
    main()