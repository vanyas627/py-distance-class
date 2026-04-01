from typing import Self


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Self | int | float) -> Self:
        if isinstance(other, int):
            return Distance(self.km + other)
        elif isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, float):
            return Distance(self.km + other)
        else:
            raise TypeError

    def __iadd__(self, other: Self | int | float) -> None:
        if isinstance(other, int):
            self.km += other
            return self
        elif isinstance(other, Distance):
            self.km += other.km
            return self
        elif isinstance(other, float):
            self.km += other
            return self
        else:
            raise TypeError

    def __mul__(self, other: int) -> Self:
        return Distance(self.km * other)

    def __truediv__(self, other: int) -> Self:
        return Distance(round(self.km / other, 2))

    def __ge__(self, other: Self | int | float) -> bool:
        if isinstance(other, int):
            return self.km >= other
        elif isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, float):
            return self.km >= other
        else:
            raise TypeError

    def __gt__(self, other: Self | int | float) -> bool:
        if isinstance(other, int):
            return self.km > other
        elif isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, float):
            return self.km > other
        else:
            raise TypeError

    def __le__(self, other: Self | int | float) -> bool:
        if isinstance(other, int):
            return self.km <= other
        elif isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, float):
            return self.km <= other
        else:
            raise TypeError

    def __lt__(self, other: Self | int | float) -> bool:
        if isinstance(other, int):
            return self.km < other
        elif isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, float):
            return self.km < other
        else:
            raise TypeError

    def __eq__(self, other: Self | int | float) -> bool:
        if isinstance(other, int):
            return self.km == other
        elif isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, float):
            return self.km == other
        else:
            raise TypeError
