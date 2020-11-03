# -*- coding: utf-8 -*-
# __author__ = "shizhiwei"


# @Time    : 2020/10/27 20:00
# Email    : shizhiwei@canway.net
# instruction  : 设计模式之外观模式

class sub_system_one(object):
    def method(self):
        print("子系统方法一")


class sub_system_two(object):
    def method(self):
        print("子系统方法二")


class sub_system_three(object):
    def method(self):
        print("子系统方法三")


class sub_system_four(object):
    def method(self):
        print("子系统方法四")


class faced_system(object):
    sub_one = sub_system_one()
    sub_two = sub_system_two()

    def method(self):
        self.sub_one.method()
        self.sub_two.method()


if __name__ == '__main__':
    faced = faced_system()
    faced.method()
