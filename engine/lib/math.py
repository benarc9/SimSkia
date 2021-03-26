class Vector:
    def __init__(self, x:int=0, y:int=0):
        self.x = x
        self.y = y

    def translate(self, vect: 'Vector'):
        self.x += vect.x
        self.y += vect.y

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, value:int):
        self._x = value

    @x.setter
    def x(self, value:float):
        self._x = int(value)

    @property
    def y(self) -> int:
        return int(self._y)

    @y.setter
    def y(self, value: int):
        self._y = value

    @y.setter
    def y(self, value: float):
        self._y = int(value)


class Translation:
    def __init__(self, vect: Vector):
        self.translation_vector = vect

    @property
    def translation_vector(self) -> Vector:
        return self._translation_vector

    @translation_vector.setter
    def translation_vector(self, value: Vector):
        self._translation_vector = value

