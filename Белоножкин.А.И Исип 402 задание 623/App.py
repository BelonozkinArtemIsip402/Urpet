from Repository import Repository

def main():
    repo = Repository()

    while True:
        print("\nВыберите действие:")
        print("1. Добавить элемент")
        print("2. Удалить элемент")
        print("3. Найти элемент")
        print("4. Показать все элементы")
        print("5. Показать периметр элемента")
        print("6. Показать площадь элемента")
        print("7. Выйти")
        
        choice = input("Введите номер действия: ")

        if choice == '1':
            parametrs = input("Для добавления, введите через пробел, параметры в этом порядке - ширина, длина: ")
            parametrs = parametrs.split(' ')
            repo.add_item(parametrs)
        
        elif choice == '2':
            id = int(input("Введите id элемента для удаления: "))
            repo.remove_item(id)
        
        elif choice == '3':
            id = int(input("Введите id элемента для поиска: "))
            exists = repo.find_item(id)
            if type(exists) is str:
                print(exists)
            else:
                print(f"Id - '{exists.id}' ширина - '{exists.width}' высота - '{exists.height}'")
        
        elif choice == '4':
            items = repo.get_all_items()
            if items:
                for item in items:
                    print(f"Id - '{item.id}' ширина - '{item.width}' высота - '{item.height}'")
            else:
                print("Репозиторий пуст.")
        
        elif choice == '5':
            id = int(input("Введите id элемента: "))
            print(repo.get_perimeter(id))

        elif choice == '6':
            id = int(input("Введите id элемента: "))
            print(repo.get_area(id))

        elif choice == '7':
            print("Выход из программы.")
            break

        else:
            print("Некорректный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()