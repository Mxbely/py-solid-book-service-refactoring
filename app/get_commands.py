from displays import DisplayBookConsole, DisplayBookReverse
from prints import PrintBookConsole, PrintBookReverse
from serializers import SerializeBookJson, SerializeBookXml


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
