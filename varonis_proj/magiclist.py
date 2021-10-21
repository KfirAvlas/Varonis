from dataclasses import dataclass


@dataclass()
class Person:
    age: int = 1


@dataclass()
class Computer:
    version: int


class MagicList:
    def __init__(self, cls_type=None):
        self.next_index = 0
        self.lst = []
        self.cls_type = cls_type

    def __len__(self):
        return len(self.lst)

    def __getitem__(self, key):
        if self.cls_type is not None:
            try:
                self.lst[key] = self.lst[key] # exception will be raised by built-in type list
            except IndexError:
                obj = self.cls_type.__new__(self.cls_type)
                self.lst.append(obj)
                self.next_index += 1
        return self.lst[key]

    def __setitem__(self, key, value):
        if self.next_index == key:
            self.lst.append(value)
            self.next_index += 1
        else:
            self.lst[key] = value  # exception will be raised by built-in type list

    def __delitem__(self, key):
        self.lst[key] = None     # if key not exists, exception will be raised by built-in type list
        new_lst = [i for i in self.lst if i is not None]
        self.lst = new_lst
        self.next_index -= 1

    def __str__(self):
        return self.lst.__str__()


t = MagicList(cls_type=Person)
t2 = MagicList(cls_type=Computer)
t3 = MagicList()

t[0].age = 2
t[1].age = 2
t[1].age = 5
t[1].age = 6
t[2].age = 9

t2[0].version = 67
t2[1].version = 6888
t2[0].version = 6999

t3[0] = 1
t3[1] = 2
t3[2] = 33
t3[3] = 44
t3[4] = 55

print(t)
print(t2)
print(t3)
