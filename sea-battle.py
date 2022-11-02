class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Dot({self.x}, {self.y})"

class BoardException(Exception)
    pass

class BoardOutException(BoardException)
    def __str__(self):
        return "Стреляете мимо поля!"

class BoardUserException(BoardException)
    def __str__(self):
        return "Уже стреляли в эту клетку"

class BoardWrongsShipException(BoardException)
    pass