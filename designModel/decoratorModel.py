# -*- coding: utf-8 -*-
# __author__ = "shizhiwei"
# @Time    : 2020/10/19 10:56
# Email    : shizhiwei@canway.net
# Instruction : 设计模式 装饰模式实现
import abc


# 违背开放封闭 原则的写法 最简单的写法
class person(object):
    def __init__(self, name):
        self.name = name

    def wear_thirts(self):
        print("穿T恤")

    def wear_trouser(self):
        print("穿垮裤")

    def wear_sneakers(self):
        print("破球鞋")

    def show(self):
        print("%s 的 装扮是：" % self.name)


# 可扩展的代码
class person_second(object):
    def __init__(self, name):
        self.name = name

    def show(self):
        print("%s 的装扮是：" % self.name)


class Finery(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def show(self):
        pass


class wear_shirts(Finery):
    def show(self):
        print("穿T恤")


class wear_trouser(Finery):
    def show(self):
        print("穿垮裤")


class wear_sneakers(Finery):
    def show(self):
        print("穿球鞋")


# 装饰模式
class person_third(object):

    def __init__(self, name):
        self.name = name

    def show(self):
        print("%s的装扮是：" % self.name)


class Finery_third(person_third):

    def decorate(self, person):
        self.person = person

    def show(self):
        if (self.person != None):
            self.person.show()


class Tshirts(Finery_third):

    def __init__(self):
        pass

    def show(self):
        print("大T恤")
        self.person.show()


class BigTrouser(Finery_third):

    def __init__(self):
        pass

    def show(self):
        print("垮裤")
        self.person.show()


if __name__ == '__main__':
    component = person_third("李华")

    dtx = Tshirts()
    dtx.decorate(component)

    kk = BigTrouser()
    kk.decorate(dtx)

    kk.show()

    # person_first = person("小明")
    # person_first.show()
    # dtx = wear_shirts()
    # kk = wear_trouser()
    # pqx = wear_sneakers()
    #
    # person = person_second("小红")
    # person.show()
    # dtx.show()
    # kk.show()
    # pqx.show()
    # person_first.wear_thirts()
    # person_first.wear_sneakers()
    # person_first.wear_trouser()
    pass
