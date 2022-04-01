class Person:
    def __init__(self, first_name, second_name):
        self.first_name = Person.fix_name(first_name)
        self.second_name = self.fix_name(second_name)

    @staticmethod
    def fix_name(name: str) -> str:
        return name[0].upper()+name[1:].lower()

    @classmethod
    def from_email(cls, email):
        left = email.split('@', 1)[0]
        first_name, second_name = left.split('.', 1)
        return cls(first_name, second_name)

    def __str__(self):
        return self.first_name + ' ' + self.second_name



if __name__ == '__main__':
    jan_kowalski = Person('jan', 'kowalski')
    print(jan_kowalski)
    tomasz_kot = Person.from_email('tomasz.kot@gamil.com')
    print(tomasz_kot)