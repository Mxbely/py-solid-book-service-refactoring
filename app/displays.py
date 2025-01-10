from abc import ABC, abstractmethod

from app.main import Book


class Display(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class DisplayBookConsole(Display):
    def display(self, book: Book) -> None:
        print(book.content)


class DisplayBookReverse(Display):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
