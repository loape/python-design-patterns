# -*- coding: utf-8 -*-
# __author__ = "shizhiwei"
# @Time    : 2020/10/28 10:17
# Email    : shizhiwei@canway.net
# instruction : 设计模式之建造者模式
import abc


class person_builder(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def build_head(self):
        pass

    @abc.abstractmethod
    def build_body(self):
        pass

    @abc.abstractmethod
    def build_armleft(self):
        pass

    @abc.abstractmethod
    def build_armright(self):
        pass

    @abc.abstractmethod
    def build_legleft(self):
        pass

    @abc.abstractmethod
    def build_legright(self):
        pass


class person_thin_builder(person_builder):
    def build_head(self):
        print("头部")

    def build_body(self):
        print("身体")

    def build_armleft(self):
        print("左手")

    def build_armright(self):
        print("右手")

    def build_legleft(self):
        print("左腿")

    def build_legright(self):
        print("右腿")


class person_director(object):
    def __init__(self, person):
        self.person = person

    def create_person(self):
        self.person.build_head()
        self.person.build_body()
        self.person.build_armleft()
        self.person.build_armright()
        self.person.build_legleft()
        self.person.build_legright()


if __name__ == '__main__':
    thin_person = person_thin_builder()
    dir_person = person_director(thin_person)
    dir_person.create_person()
