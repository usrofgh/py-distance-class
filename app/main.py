from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, another_distance: Distance | int | float) -> Distance:
        another_distance = Distance.detect_type_and_get_value(another_distance)
        return Distance(self.km + another_distance)

    def __iadd__(self, another_distance: Distance | int | float) -> Distance:
        another_distance = Distance.detect_type_and_get_value(another_distance)
        self.km += another_distance
        return self

    def __mul__(self, number: int) -> Distance:
        return Distance(self.km * number)

    def __truediv__(self, number: int) -> Distance:
        calculated = round(self.km / number, 2)
        return Distance(calculated)

    def __lt__(self, another_distance: Distance | int | float) -> bool:
        another_distance = Distance.detect_type_and_get_value(another_distance)
        return self.km < another_distance

    def __gt__(self, another_distance: Distance | int | float) -> bool:
        another_distance = Distance.detect_type_and_get_value(another_distance)
        return self.km > another_distance

    def __eq__(self, another_distance: Distance | int | float) -> bool:
        another_distance = Distance.detect_type_and_get_value(another_distance)
        return self.km == another_distance

    def __le__(self, another_distance: Distance | int | float) -> bool:
        another_distance = Distance.detect_type_and_get_value(another_distance)
        return self.km <= another_distance

    def __ge__(self, another_distance: Distance | int | float) -> bool:
        another_distance = Distance.detect_type_and_get_value(another_distance)
        return self.km >= another_distance

    def __len__(self) -> int:
        return self.km

    @staticmethod
    def detect_type_and_get_value(
            another_distance: Distance | int | float
    ) -> Distance | int | float:

        if isinstance(another_distance, Distance):
            return another_distance.km
        return another_distance
