"""CSC148 in-class exercise: Super Duper Manager

=== Module description ===
This module contains starter code for an in-class exercise.
"""
from math import sqrt, ceil
import random  # used to generate random numbers


class Vehicle:
    """An abstract class for a vehicle in the Super Duper system.

    === Attributes ===
    position:
        The coordinates of this vehicle on a grid.
    fuel:
        The amount of fuel remaining for this vehicle.

    === Representation invariants ===
    - fuel >= 0
    """
    position: tuple[int, int]
    fuel: int
    abc: str

    def __init__(self, initial_fuel: int,
                 initial_position: tuple[int, int]) -> None:
        """Initialize a new Vehicle with the given fuel and position.

        Precondition: initial_fuel >= 0
        """
        self.fuel = initial_fuel
        self.position = initial_position

    def fuel_needed(self, new_x: int, new_y: int) -> int:
        """Return how much fuel would be needed to move to the given position.

        Note: the amount returned may be larger than self.fuel,
        indicating that this vehicle may not move to the given position.
        """
        raise NotImplementedError

    def move(self, new_x: int, new_y: int) -> None:
        """Move this vehicle to a new position.

        Do nothing if this vehicle does not have enough fuel to move to the
        specified position.
        """
        needed = self.fuel_needed(new_x, new_y)
        if needed <= self.fuel:
            self.position = (new_x, new_y)
            self.fuel -= needed


# TODO Q5 of worksheet: Write code for the Car, Helicopter, and
#         UnreliableMagicCarpet classes, which are subclasses of Vehicle

class Car(Vehicle):
    """A subclass of Vehicle that is a Car

    === Sample Usage ===
    >>> c = Car(100)
    >>> c.fuel
    100

    >>> c.fuel_needed(5, 5)
    10

    >>> c.move(5,5)
    >>> c.position
    (5, 5)
    >>> c.fuel
    90
    """

    def __init__(self, initial_fuel: int)-> None:
        """Create a Car

        A car starts at position (0, 0), can not go diagonally and use 1 unit
        of fuel per unit distance.
        """

        Vehicle.__init__(self, initial_fuel, (0, 0))

    def fuel_needed(self, new_x: int, new_y: int) -> int:
        """Return how much fuel would be needed to move to the given position.

        Note: the amount returned may be larger than self.fuel, indicating that
        this vehicle may not move to the given position.
        """

        return abs(new_x - self.position[0]) + abs(new_y - self.position[1])

    pass


class Helicopter(Vehicle):
    """A subclass of Vehicle that is a Car

    === Sample Usage ===


    """

    def __init__(self, initial_fuel: int)-> None:
        """Create a Helicopter

        A car starts at position (3, 5) or the position of the launchpad,
        it can go diagonally and use 1 unit of fuel per unit distance.
        """

        Vehicle.__init__(self, initial_fuel)
        self.

    def fuel_needed(self, new_x: int, new_y: int) -> int:
        """Return how much fuel would be needed to move to the given position.

        Note: the amount returned may be larger than self.fuel, indicating that
        this vehicle may not move to the given position.
        """

        return (new_x - self.position[0]) + (new_y - self.position[1])


    pass


class UnreliableMagicCarpet(Vehicle):
    pass


class SuperDuperManager:
    """
    A class responsible for keeping track of all vehicles
     in the system.

    ==== Sample Usage ====
    >>> v = SuperDuperManager()
    >>> v.add_vehicle('Car', 'car1', 100)
    >>> v.vehicle_type
    'Car'
    >>> v.id_
    'car1'
    >>> v.fuel
    100
    >>> v.get_vehicle_position()
    (0, 0)

    >>> v.move_vehicle('car1', 5, 6)
    >>> v.get_vehicle_position('car1')
    (5, 5)
    >>> v.get_vehicle_fuel('car1')
    90
    """
    # === Private Attributes ===
    # _vehicles:
    #     Maps a string that uniquely identifies a vehicle to the corresponding
    #     Vehicle object.
    #     For example, _vehicles['car1'] would be a Vehicle object with the id_
    #     'car1'.
    _vehicles: dict[str, Vehicle]

    def __init__(self) -> None:
        """Initialize a new SuperDuperManager.

        There are no vehicles in the system when first created.
        """
        self._vehicles = {}

    def add_vehicle(self, vehicle_type: str, id_: str, fuel: int) -> None:
        """Add a new vehicle with the given type, id_, and fuel to the system.

        Do nothing if there is already a vehicle with the given id.

        Preconditions:
          - <vehicle_type> is one of 'Car', 'Helicopter', or
          'UnreliableMagicCarpet'.
          - fuel >= 0
        """
        # Check to make sure the identifier isn't already used.
        if id_ not in self._vehicles:
            if vehicle_type == 'Car':
                self._vehicles[id_] = Car(fuel)
            elif vehicle_type == 'Helicopter':
                self._vehicles[id_] = Helicopter(fuel)
            elif vehicle_type == 'UnreliableMagicCarpet':
                self._vehicles[id_] = UnreliableMagicCarpet(fuel)

    def move_vehicle(self, id_: str, new_x: int, new_y: int) -> None:
        """Move the vehicle with the given id.

        The vehicle called <id_> should be moved to position (<new_x>, <new_y>).
        Do nothing if there is no vehicle with the given id,
        or if the corresponding vehicle does not have enough fuel to move.
        """
        if id_ in self._vehicles:
            self._vehicles[id_].move(new_x, new_y)

    def get_vehicle_position(self, id_: str) -> None | tuple[int, int]:
        """Return the position of the vehicle with the given id.

        Return a tuple of the (x, y) position of the vehicle.
        Return None if there is no vehicle with the given id.
        """
        if id_ in self._vehicles:
            return self._vehicles[id_].position

    def get_vehicle_fuel(self, id_: str) -> None | int:
        """Return the amount of fuel of the vehicle with the given id.

        Return None if there is no vehicle with the given id.
        """
        if id_ in self._vehicles:
            return self._vehicles[id_].fuel


#if __name__ == '__main__':
