class Clock:
    def __init__(self, hour: int = 0, minute: int = 0, second: int = 0):
        Clock._check_values(hour, minute, second)
        self._hour = hour
        self._minute = minute
        self._second = second

    def advance(self, h_delta: int = 0, min_delta: int = 0, s_delta: int = 0) -> None:
        Clock._check_values(h_delta, min_delta, s_delta)
        self._hour += h_delta
        self._minute += min_delta
        self._second += s_delta

        self._second, minute = divmod(self._second, 60)
        self._minute+=minute
        self._minute, hour = divmod(self._minute, 60)
        if self._hour>=24:
            self._hour-=24
            Calendar.advance(d_delta=1)

    def __str__(self) -> str:
        return f"{self._hour:02d}:{self._minute:02d}:{self._second:02d}"

    @staticmethod
    def _check_values(hour: int = 0, minute: int = 0, second: int = 0) -> None:
        if not isinstance(hour, int): raise TypeError("Wrong type of hour, have to be an int")
        if not isinstance(minute, int): raise TypeError("Wrong type of minute, have to be an int")
        if not isinstance(second, int): raise TypeError("Wrong type of second, have to be an int")

        if not 0 <= hour < 24: raise ValueError("Hour must be in range [0, 23]")
        if not 0 <= minute < 60: raise ValueError("Minute must be in range [0, 59]")
        if not 0 <= second < 60: raise ValueError("Second must be in range [0, 59]")


class Calendar:
    def __init__(self, year: int = 0, month: int = 0, day: int = 0):
        Calendar._check_values(year, month, day)
        self._year = year
        self._month = month
        self._day = day

    def advance(self, y_delta: int = 0, m_delta: int = 0, d_delta: int = 0) -> None:
        Calendar._check_values(y_delta, m_delta, d_delta)
        self._year += y_delta
        self._month += m_delta
        self._day += d_delta

        self._day, month = divmod(self._day, 31)
        self._month+=month
        self._month, year = divmod(self._month, 12)
        self._year+=year

    def __str__(self):
        return f"{self._year:04d}-{self._month:02d}-{self._day:02d}"

    @staticmethod
    def _check_values(year: int, month: int, day: int) -> None:
        if not isinstance(year, int): raise TypeError("Wrong type of year, have to be an int")
        if not isinstance(year, int): raise TypeError("Wrong type of year, have to be an int")
        if not isinstance(year, int): raise TypeError("Wrong type of year, have to be an int")

        if year<0: raise ValueError("Year has to be nonnegative")
        if not 0 <= month <= 12: raise ValueError("Month has to be in range [0, 12]")
        if not 0 <= day <= 31: raise ValueError("Day has to be in range [0, 31]")


class ClockCalendar(Calendar, Clock):
    def __init__(self, year, month, day, hour, minute, second):
        Calendar.__init__(self,year, month, day)
        Clock.__init__(self, hour, minute, second)


    def advance(self, y_delta: int = 0, m_delta: int = 0, d_delta: int = 0, h_delta: int = 0, min_delta: int = 0, s_delta: int = 0) -> None:
        Calendar.advance(self, y_delta, m_delta, d_delta)
        Clock.advance(self, h_delta, min_delta, s_delta)

    def __str__(self):
        return f"{self._year:04d}-{self._month:02d}-{self._day:02d} {self._hour:02d}:{self._minute:02d}:{self._second:02d}"


if __name__ == '__main__':
    datetime = ClockCalendar(2021, 11, 6, 17, 31, 45)
    datetime.advance(min_delta=30, y_delta=10)
    print(datetime)
