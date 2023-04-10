# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны 
# находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной



def read_file():
    with open(path_file,'r',encoding='UTF-8') as f:
        print('Список контактов:\n'+f.read()+'\n')


def app_in_file(): 
    with open(path_file,'a',encoding='UTF-8') as f:
        f.writelines('\n'+input('Введите новый контакт: '))


def find_file():
    find_info = input('Укажите имя, фамилию или номер(часть номера) контакта: ')
    with open(path_file,'r',encoding='UTF-8') as f:
        print('Результат поиска:')
        for line in f:
            if find_info.casefold() in line.casefold():
                print(line.strip())
    print()


def read_file_into_list():
    with open(path_file,'r',encoding='UTF-8') as f:
        phone_book =[]
        for   line in f:
            if line.strip() !="": phone_book.append(line.strip())        
    return phone_book


def write_list_into_file(phone_book):
    with open(path_file,'w',encoding='UTF-8') as f:
        phone_book.sort()
        for item in phone_book:
            f.write ('\n'+item)


def find_in_list_and_change(phone_book):
    find_info = input("Укажите имя, фамилию или номер(часть номера) контакта: ")
    for item in phone_book:
        if find_info.casefold() in item.casefold():
            print(item.strip())
            if input("Редактируем эту запись да/нет: ") == "да".casefold(): 
                while True:
                    request = input('1 - изменить или 2 - удалить запись: ')
                    if  request == '2':
                        phone_book.remove(item)
                        write_list_into_file(phone_book)
                        return
                    elif request == '1':
                        new_item =input('Введите исправленный контакт: ')
                        phone_book.remove(item)
                        phone_book.append(new_item)
                        write_list_into_file(phone_book)
                        return
        else: 
            continue
    print('Ничего не найдено')
            

def consol_menu():
    while True:
        print('Меню команд:')
        text = input("1 - показать весь справочник\n2 - найти контакт\n3 - добавить новый контакт\n4 - редактировать контакт\n5 - выход из меню\n Сделайте ваш выбор: ")
        if text == '1':
            read_file()
        elif text == '2':
            find_file()
        elif text == '3':
            app_in_file()
        elif text == '4':
            find_in_list_and_change(read_file_into_list())            
        elif text == '5':
            print('Завершено успешно')
            return   
        else: 
            print("Ошибка ввода")


path_file = r'Tel_book.txt'
consol_menu()