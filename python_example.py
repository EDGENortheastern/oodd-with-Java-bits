class Person:
    def __init__(self, name, age):
        self.__name = name      # double underscore "makes" it private
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age

person = Person("Alice", 25)
print(person.get_name(), "is", person.get_age(), "years old.")

person.set_age(30)
print("After a birthday:", person.get_name(), "is now", person.get_age())

print(person._Person__name)  # name mangling != private, to avoid accidental name clashes
# Without name mangling, the child would accidentally override the parent’s names.