class Person:
    def __init__(self, fist_name, last_name, gender) -> None:
        self.__first_name = fist_name
        self.__last_name = last_name
        self.__gender = gender
        self.__name = ""

    def print_details(self):
        print(
            f'first_name: {self.__first_name}, last_name: {self.__last_name}, gender: {self.__gender}')

    # Getter -> to access the __name private property
    @property
    def name(self):
        if(self.__gender == "M"):
            return f'Mr. {self.__first_name}, {self.__last_name}'
        elif(self.__gender == "F"):
            return f'Ms. {self.__first_name}, {self.__last_name}'
        else:
            return f'{self.__first_name}, {self.__last_name}'


p = Person("Avinash", "G", "M")
print(p.name)
p.print_details()


p2 = Person("Jasmine", "L", "F")
print(p2.name)

p2.print_details()
