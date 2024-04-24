"""
Напишите класс User, имеющий следующие свойства и методы:

- __init__(self, name, password): конструктор, принимающий имя пользователя и пароль - name: свойство,
которое возвращает имя пользователя - password: свойство, которое позволяет установить или изменить пароль
пользователя - is_admin: свойство, которое возвращает, является ли пользователь администратором или нет - _is_admin:
свойство-помощник, которое определяет, является ли пользователь администратором или нет - login(self, password):
метод, который проверяет, соответствует ли введенный пароль паролю пользователя - logout(self): метод,
который выходит из аккаунта пользователя (устанавливает значение свойства _is_logged_in в False при условии,
что пользователь залогинен)

Для свойств name и password используйте декораторы @property и @password.setter.
"""


class User:

    def __init__(self, name, password):
        self._name = name
        self._password = password
        self.__is_admin = False

    @property
    def name(self):
        return f"{self._name}"

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def password(self):
        return f"{self._password}"

    @password.setter
    def password(self, new_password):
        self._password = new_password


    @property
    def is_admin(self):
        if self._name:
            return True
        return False

    @is_admin.setter
    def is_admin(self, value):
        self.__is_admin = value

    def login(self, password):
        if self._password == password:
            return True

    def logout(self):
        if self._name is self.__is_admin:
            self.__is_admin = False
        self.__is_admin = True


# код для проверки
user1 = User("Alice", "qwerty")
print(user1.name)  # Alice
print(user1.password)  # qwerty
print(user1.is_admin)  # False

user1.password = "newpassword"
print(user1.password)  # newpassword

user1._is_admin = True
print(user1.is_admin)  # True

user1.login("newpassword")  # True
user1.logout()
