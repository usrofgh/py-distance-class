from __future__ import annotations


class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        return Distance(self.km + self.get_instances_value_or_number(other))

    def __iadd__(self, other: Distance | int | float) -> Distance:
        self.km += self.get_instances_value_or_number(other)
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Distance | int | float) -> bool:
        return True \
            if self.km < self.get_instances_value_or_number(other) \
            else False

    def __gt__(self, other: Distance | int | float) -> bool:
        return True \
            if self.km > self.get_instances_value_or_number(other) \
            else False

    def __eq__(self, other: Distance | int | float) -> bool:
        return True \
            if self.km == self.get_instances_value_or_number(other) \
            else False

    def __le__(self, other: Distance | int | float) -> bool:
        return True \
            if self.km <= self.get_instances_value_or_number(other) \
            else False

    def __ge__(self, other: Distance | int | float) -> bool:
        return True \
            if self.km >= self.get_instances_value_or_number(other) \
            else False

    @staticmethod
    def get_instances_value_or_number(arg: Distance | int | float)\
            -> Distance | int | float:
        return arg.km if isinstance(arg, Distance) else arg
