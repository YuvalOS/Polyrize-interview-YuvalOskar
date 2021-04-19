from dataclasses import dataclass


@dataclass
class Person:
    age: int = 1


class MagicList:

    def __init__(self, cls_type=None):
        self.magic_list = []
        self.cls_type = cls_type
        self.size = 0

    def __setitem__(self, key, value):
        if key == self.size:
            if self.cls_type and self.cls_type != type(value):
                raise TypeError(f'MagicList with cls_type allows inserting only of type: {self.cls_type}')
            self.magic_list.append(value)
            self.size += 1
        else:
            self.magic_list[key] = value

    def __getitem__(self, item):
        if self.cls_type:
            if item == self.size:
                self.magic_list.append(self.cls_type())
                self.size += 1
        return self.magic_list[item]

    def __getattr__(self, item):
        return item.upper()

    def __str__(self):
        return f'{self.magic_list}'

    def pop(self):
        popped_item = self.magic_list.pop()
        self.size -= 1
        return popped_item

    def remove(self, value):
        self.magic_list.remove(value)
        self.size -= 1

    def clear(self):
        self.magic_list.clear()
        self.size = 0


def main():
    # Native types Example
    print()
    print('Magic list with int type:')
    a = MagicList()
    a[0] = 1
    a[1] = 'hello'
    a[2] = 3
    print('Full:')
    print(a)
    a.clear()
    print('Cleared:')
    print(a)

    # DataClass Types Example
    print('Magic list with dataclass Person type:')
    a = MagicList(cls_type=Person)
    a[0].age = 5
    a[1] = Person(6)
    a[2].age = 10
    print('Full:')
    print(a)
    a.clear()
    print('Cleared:')
    print(a)

    # Wrong use of MagicList of dataclass - 'empty' list item bug
    a = MagicList(cls_type=Person)
    x = a[0]  # a[0] doesn't exist!
    if x is not None:
        raise TypeError('x should have contained a None value!')


if __name__ == '__main__':
    main()
