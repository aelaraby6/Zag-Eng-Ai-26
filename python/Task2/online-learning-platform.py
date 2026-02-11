class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self._password = password

    def show_info(self):
        print(f"Name: {self.name}, Email: {self.email}")

    def set_password(self, password):
        self._password = password

    def check_password(self, password):
        return self._password == password


class Instructor(User):
    def __init__(self, name, email, password, specialty):
        super().__init__(name, email, password)
        self.specialty = specialty

    def show_info(self):
        super().show_info()
        print(f"Specialty: {self.specialty}")


class Student(User):
    def __init__(self, name, email, password, level):
        super().__init__(name, email, password)
        self.level = level

    def show_info(self):
        super().show_info()
        print(f"Level: {self.level}")


s = Student("Ali", "ali@email.com", "1234", "Beginner")
i = Instructor("Mona", "mona@email.com", "abcd", "Machine Learning")

s.show_info()
i.show_info()
print(s.check_password("1234"))
