#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

class User(object):
    name1 = 'zjw'
    def __init__(self, name, age):
        self.name = name
        self.age = age
        x = 1
    def get_name(self):
        return self.name
    def get_addr(self, addr:str):
        if addr:
            self.addr = addr
        return self.addr*2

if __name__ == '__main__':
    print(User.name1)
    user = User('两点水', 23)
    print(user.name1)
    print(user.name)
    print(user.age)
    user.addr = 'beijing'
    print(user.get_addr(''))
    user.category = 'obj'
    user.id = 123
    print(user.category)
    print(user.id)
    print(getattr(User,'get_addr1',"mm")) #加上参数"mm",如果没有找到User的属性值get_addr1则会默认输出"mm",如果不加参数，找不到User的属性值程序则会报错
    #print(getattr(User,'get_addr1')) 
    get_addr2 = getattr(user, 'get_addr')
    print(get_addr2('nn'))