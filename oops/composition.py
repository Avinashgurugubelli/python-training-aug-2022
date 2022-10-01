"""
Composition (HAS- A relationship)

Key words: contains, HAS-A

The composition relationship is just another form of the aggregation relationship, but the child class’s instance lifecycle is dependent on the parent class’s instance lifecycle.

In other words, It is also a WHOLE PART relationship where

Whole is responsible for creation and destruction of the parts.
Part will not function independently
Whole will not function without part.

Examples:

WHOLE	        PART
Car	            Engine
Human	        Emotions
School	        ClassRoom
Book	        Pages
House	        Rooms

"""


class Engine:
    def __init__(self, make, year, horsePower) -> None:
        self.make = make
        self.year = year
        self.horsePower = horsePower


class MusicPlayer:
    def __init__(self, make, year, price) -> None:
        # Public members
        self.make = make
        self.year = year
        self.price = price


class Car:
    def __init__(self, engine) -> None:
        # Protected
        self._engine = engine


class MaruthiCar(Car):
    def __init__(self) -> None:
        self.music_player = None

        # Composition -> when ever the car is destroyed engined will be deconstructed automatically from memory
        super().__init__(Engine("Maruthi", 2022, "600 HP"))

    def get_engine_spec(self):
        print(
            f'Engine specifications, Make: {self._engine.make}, year: {self._engine.year}, horsePower: {self.engine.horsePower}')

    # Aggregation/ Association
    def add_music_player(self, music_player):
        self.music_player = music_player


# Calling point
c = MaruthiCar()
c.get_engine_spec()

print(c._engine.make)

m1 = MusicPlayer("Sony", 2022, 10000)
c.add_music_player(m1)
