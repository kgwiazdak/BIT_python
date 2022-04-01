class Number:
    def __init__(self, initialisation):
        self.initialisation = initialisation

    def add(self, num):
        self.initialisation += num
        return self
    def sub(self, num):
        self.initialisation -= num
        return self

    def get(self):
        return self.initialisation

    def __int__(self):
        return self.initialisation

if __name__ == '__main__':
    number = Number(1)
    number.add(3).sub(5)
    print(number.get())