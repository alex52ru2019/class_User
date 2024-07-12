list_users = [] # {id: name: access}

class User:
   def __init__(self, id_user, name, access = 'user'): # при создании пользователя по умолчанию доступ USER
        list_users.append([id_user, name, access]) # автоматически добавляем пользователя в список

class Admin(User):
    def __init__(self, id_user, name, access = 'admin'): # наследуем всё из User
        super().__init__(id_user, name, access)

    def add_user(self, id_user, name): #добавляет пользователя
        User(id_user, name, 'user') # при создании пользователя он сразу добавиться в список

    def remove_user(self, id_user): # удаляет пользователя
        for i in list_users:
            if i[0] == id_user:
                print(f'Пользователь {i} удален')
                list_users.remove(i)


admin1 = Admin(1, 'Андрей', 'admin') # создаем админа

admin1.add_user(2, 'Вася') # админ добавляет пользователя
admin1.add_user(3, 'Маша') # админ добавляет пользователя
admin1.add_user(4, 'Даша') # админ добавляет пользователя
print(list_users) # печатаем список пользователей

admin1.remove_user(2) # админ удаляет пользователя по id
print(list_users) # печатаем список пользователей

