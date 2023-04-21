from abc import ABC, abstractmethod


class Museum_showpiece(ABC):
    def __init__(self):
        self.type = None
        self.__title = None
        self.__author = None

    @abstractmethod
    def show_artwork(self):
        pass


class Framed_artwork(Museum_showpiece):
    def __init__(self, type, title, author):
        super().__init__()
        self.type = type
        self.__title = title
        self.__author = author

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @title.setter
    def title(self, new_title):
        self.__title = new_title

    @author.setter
    def author(self, new_author):
        self.__author = new_author

    def show_artwork(self):
        return f'This is {self.__author}'


class Photography(Framed_artwork):
    def __init__(self, type, title, author, evaluation):
        super().__init__(type, title, author)
        self.evaluation = evaluation

    def show_artwork(self):
        return f'This famous photo - {self.title}!'

    def __strict_instructions_1(self):
        return 'The artwork needs to be removed from the viewing room!'

    def __strict_instructions_2(self):
        return 'Keep the artwork in the warehouse until further notice!'

    def strict_instruction(self):
        return self.__strict_instructions_1(), self.__strict_instructions_2()


artwork1 = Framed_artwork('painting', 'Acrobate a la boule', 'Picasso')

print(artwork1.title)
artwork1.title = 'Crying woman'
print(artwork1.title)
print(artwork1.show_artwork())

print()
artwork2 = Photography('photography', 'selfy', 'Robert Cornelius', 5000000)
print(artwork2.show_artwork())
print(artwork2.strict_instruction())
