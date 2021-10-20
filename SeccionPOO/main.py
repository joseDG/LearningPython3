import csv


class Item:
    ...


class Phone(Item):
    pass


phone1 = Item("jscPhonev10", 500, 2)
phone1.broken_phones = 1
phone2 = Item("jscPhonev20", 700, 5)
phone2.broken_phones = 1
