from Rectangle_class import Rectangle

class Repository:
    def __init__(self):
        self.items = []  # Инициализация пустого списка

    def add_item(self, strings):
        item = Rectangle(width=int(strings[0]), height=int(strings[1]), id=len(self.items) + 1)
        print("Элемент добавлен")
        self.items.append(item)

    def remove_item(self, id):
        for item in self.items:
            if item.id == id:
                self.items.remove(item)
                print("Элемент удалён.")
        print("Элемент не найден.")

    def get_all_items(self):
        return self.items      
    
    def find_item(self, id):
        for item in self.items:
            if item.id == id:
                return item
        return "Элемент не найден."
    
    def get_perimeter(self, id):
        for item in self.items:
            if item.id == id:
                return item.perimeter()
        return "Элемент не найден."
    
    def get_area(self, id):
        for item in self.items:
            if item.id == id:
                return item.area()
        return "Элемент не найден."
    
    
