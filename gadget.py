class Smartphone:
    def __init__(self, name, characteristic, price):
        self.name = name
        self.characteristic = characteristic
        self.price = price

    def __str__(self):
        return f'смартфон: {self.name}, {self.characteristic}, {self.price} руб.'

    @classmethod
    def import_from_file(cls, gadget):
        items_source = open(gadget, 'r', encoding='utf-8').readlines()
        items_source = list(map(lambda x: x.replace('\n', '').split(', '), items_source))
        items_schema = items_source.pop(0)
        items_source_as_dict = list(map(lambda x: dict(zip(items_schema, x)), items_source))
        items = []
        for item_dict in items_source_as_dict:
            _item = cls(**item_dict)
            items.append(_item)
        return items

class Consolys(Smartphone):

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
            return f'консоли: {self.name}, {self.price} руб.'

class Compudahters(Smartphone):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'компьютеры: {self.name}, {self.price} руб.'