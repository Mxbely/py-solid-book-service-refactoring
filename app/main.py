from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as ET


class Book:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content


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


class Print(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class PrintBookConsole(Print):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class PrintBookReverse(Print):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class SerializeBook(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class SerializeBookJson(SerializeBook):
    def serialize(self, book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class SerializeBookXml(SerializeBook):
    def serialize(self, book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")


def get_printer(cmd):
    commands = {
        "console": PrintBookConsole(),
        "reverse": PrintBookReverse(),
    }
    return commands[cmd]


def get_display(cmd):
    commands = {
        "console": DisplayBookConsole(),
        "reverse": DisplayBookReverse(),
    }
    return commands[cmd]


def get_serializer(cmd):
    commands = {
        "json": SerializeBookJson(),
        "xml": SerializeBookXml(),
    }
    return commands[cmd]


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            display = get_display(method_type)
            display.display(book)
        elif cmd == "print":
            printer = get_printer(method_type)
            printer.print_book(book)
        elif cmd == "serialize":
            serializer = get_serializer(method_type)
            return serializer.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
