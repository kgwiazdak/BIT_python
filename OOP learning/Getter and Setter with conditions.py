class Patient:
    def __init__(self, first_name, last_name, temperature):
        self._first_name = first_name
        self._last_name = last_name
        self._temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self,new_temperature):
        if new_temperature<30 or new_temperature>45:
            raise ValueError(f'Dude is propably dead with {new_temperature} degrees')
        self._temperature = new_temperature


if __name__ == '__main__':
    jan_kowalski = Patient('Jan', 'Kowalski', 36)
    cos = jan_kowalski.temperature
    print(cos)
    jan_kowalski.temperature = 2
    print(jan_kowalski.temperature)