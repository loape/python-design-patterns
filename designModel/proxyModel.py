# -*- coding: utf-8 -*-
# __author__ = "shizhiwei"
# @Time    : 2020/10/19 16:16
# Email    : shizhiwei@canway.net
# Instruction : 设计模式之代理模式
class school_girl(object):
    def __init__(self, name):
        self.name = name


class interface(object):
    def give_dolls(self):
        pass

    def give_flowers(self):
        pass

    def give_chocolate(self):
        pass


class pursuit(interface):

    def __init__(self, mm):
        self.mm = mm

    def give_chocolate(self):
        print("送巧克力")

    def give_flowers(self):
        print("送鲜花")

    def give_dolls(self):
        print("送洋娃娃")


class proxy(interface):
    def __init__(self, mm):
        self.gg = pursuit(mm)

    def give_dolls(self):
        self.gg.give_dolls()

    def give_chocolate(self):
        self.gg.give_chocolate()

    def give_flowers(self):
        self.gg.give_flowers()


if __name__ == "__main__":
    jiaojiao = school_girl("娇妹")
    dava = proxy(jiaojiao)

    dava.give_chocolate()
    dava.give_flowers()
    dava.give_dolls()

    pass
