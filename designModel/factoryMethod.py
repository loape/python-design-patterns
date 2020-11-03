# -*- coding: utf-8 -*-
__author__ = "shizhiwei"


# @Time    : 2020/10/20 19:36
# Email    : shizhiwei@canway.net
# Instruction : 设计模式之工厂方法模式
class operation(object):
    first_number = 0
    second_number = 0

    def get_result(self):
        result = 0
        return result


class operation_add(operation):

    def get_result(self):
        result = self.first_number + self.second_number
        return result


class operation_sub(operation):
    def get_result(self):
        result = self.first_number - self.second_number
        return result


class operation_mul(operation):
    def get_result(self):
        result = self.first_number * self.second_number
        return result


class operation_div(operation):
    def get_result(self):
        if self.second_number == 0:
            return "分母不能为0"
        else:
            result = self.first_number / self.second_number
            return result


class interface_ifactory(object):
    oper = operation()

    def create_operation(self):
        return self.oper


class add_factory(interface_ifactory):
    def create_operation(self):
        self.oper = operation_add()
        return self.oper


class sub_factory(interface_ifactory):
    def create_operation(self):
        self.oper = operation_sub()
        return self.oper


class mul_factory(interface_ifactory):
    def create_operation(self):
        self.oper = operation_mul()
        return self.oper


class div_factory(interface_ifactory):
    def create_operation(self):
        self.oper = operation_div()
        return self.oper

class leifeng(object):
    def sweep(self):
        print("扫地")

    def wash(self):
        print("洗衣服")


class student(leifeng):
    pass


class volunteer(leifeng):
    pass


class simple_factory(object):
    lei = leifeng()

    def create_leifeng(self, type):
        if type == '学生':
            lei = student()
        else:
            lei = volunteer()
        return lei


class interface_leifeng(object):
    lei = leifeng

    def create_leifeng(self):
        return self.lei


class factory_student(interface_leifeng):
    def create_leifeng(self):
        self.lei = student()
        return self.lei


class factory_volunteer(interface_leifeng):
    def create_leifeng(self):
        self.lei = volunteer()
        return self.lei


if __name__ == '__main__':
    # lei = student()
    # lei.sweep()
    # lei.wash()

    inter_leifeng = factory_student()
    stud = inter_leifeng.create_leifeng()

    stud.sweep()

    # inter_fact = div_factory()
    # oper = inter_fact.create_operation()
    # oper.first_number = 4
    # oper.second_number = 2
    # result = oper.get_result()
    # print(result)

    pass
