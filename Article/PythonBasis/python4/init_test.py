#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

class User(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        x = 1
    def get_name(self):
        return self.name
    def get_addr(self, addr:str):
        if addr:
            self.addr = addr
        return self.addr

if __name__ == '__main__':
    user = User('两点水', 23)
    print(user.name)
    print(user.age)
    user.addr = 'beijing'
    print(user.get_addr(''))
    user.category = 'obj'
    user.id = 123
    print(user.category)
    print(user.id)
    print(getattr(User,'get_addr',2))
    get_addr2 = getattr(user, 'get_addr')
    print(get_addr2('nn'))