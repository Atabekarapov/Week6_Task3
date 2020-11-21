# TASK3, HOMEWOR, ATABEK
# 1)
'''Создайте класс ContactList, который должен наследоваться от
встроенного класса list. В нем должен быть реализован метод
search_by_name, который должен принимать имя, и возвращать список
всех совпадений. Создайте экземпляр класса all_contacts и передайте список
ваших контактов:
all_contacts = ContactList(list_of_your_contacts).
Используйте метод search_by_name для поиска.'''
# 1)
# class ContactList(list):
#     def search_by_name(self, name):
#         all_list = []
#         for n in self:
#             if n == name:
#                 all_list.append(n)
#             else:
#                 continue 
#             return all_list

# all_contacts = ContactList(['Kylym', 'Aktilek', 'Marlen'])
# a = all_contacts.search_by_name('Marlen')
# print(a)

# 2)
'''Создайте класс с именем User. Создайте два атрибута first_name и last_
name, а затем еще несколько атрибутов, которые обычно хранятся в профиле пользователя.
Напишите метод describe_user(), который выводит сводку с информацией о пользователе. Создайте
еще один метод greet_user() для вывода персонального приветствия для пользователя.
Напишите класс с именем Admin, наследующий от класса User из. Добавьте атрибут privileges для
хранения списка строк вида «разрешено добавлять сообщения», «разрешено удалять
пользователей», «разрешено банить пользователей» и т. д. Напишите метод show_privileges() для
вывода набора привилегий администратора. Создайте экземпляр Admin и вызовите все методы.'''

# class User:
#     name = 'Marsel'
#     last_name = "Akylbekov"
#     age = "15"
#     password = "qwerty"
#     img = "some_image"
    
#     def describe_user(self):
#         self.name
#         self.last_name
#         self.age
#         self.password
#         self.img

#     def greet_user(self):
#         print(f'Hello mister {self.name} {self.last_name}')

# class Admin(User):
#     privileges = ["разрешено добавлять сообщения", "разрешено удалятьпользователей", "разрешено банить пользователей"]

#     def show_privileges(self):
#         print(Admin.__dict__)

# a1 = User()
# a1.describe_user()
# a1.greet_user()
# admin = Admin()
# admin.show_privileges()
# admin.name = 'Admin'
# admin.describe_user()
# admin.greet_user()

# 3)
'''Мебель
1. class House: тип дома, общая площадь, оставшаяся площадь и список мебели.
2. Мебель имеет название и площадь, например, кровать: 4 м2, шкаф-купе: 2 м2, стол: 1,5 квадратных
метров.
3. Добавьте вышеуказанную мебель в дом.
4. При печати информации о доме требуется вывод: тип дома, общая площадь, оставшаяся площадь,
список мебели.'''
# class House:
#     type_house = 'Дома 2 этажный'
#     house_are = 120
#     remaining_area = 0
#     furniture_list = {"кровать": 4, "шкаф-купе": 2, "стол": 1.5}

#     area = 0
#     for a in furniture_list.values():
#         area += a
        
#     remaining_area = house_are - area

#     def info_hause(self):
#         print(f"Тип {self.type_house}"  )
#         print(f"Общая площадь дома {self.house_are} км2")
#         print(f"Оставщая площадь дома {self.remaining_area} ")
#         print(f"Мебель в доме {self.furniture_list} ")

# house1 = House()
# house1.info_hause()

# 4)

# def funnyString(s):
#     r = s[::-1]
    
#     for i in range(0, len(s)):
#         if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(r[i]) - ord(r[i-1])):
#             return "Not Funny"
    
#     return "Funny"
# print(funnyString("qwerty"))




















