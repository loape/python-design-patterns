# -*- coding: utf-8 -*-
# __author__ = "shizhiwei"
# @Time    : 2020/10/16 13:51
# Email    : shizhiwei@canway.net
# instruction : 设计模式之简单策略模式  实现商场收银软件
import abc


## 面向过程实现
def face_process():
    item_price = int(input("请输入商品单价: "))
    item_number = float(input("请输入商品数量: "))

    print("商品总价是： %s" % (item_price * item_number))


## 简单工厂函数
class cash_super(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def accept_cash(self, money):
        pass


class cash_normal(cash_super):
    def accept_cash(self, money):
        return money


class cash_rebate(cash_super):
    def __init__(self, decount):
        self.decount = decount

    def accept_cash(self, money):
        return money * self.decount


class cash_return(cash_super):
    def __init__(self, money_condition, money_return):
        self.money_condition = money_condition
        self.money_return = money_return

    def accept_cash(self, money):
        if money >= self.money_condition:
            return money - (int(money / self.money_condition) * self.money_return)


class cash_factory(object):

    def create_cash_accept(self, type):

        if type == "正常收费":
            cash = cash_normal()
        elif type == "满减":
            cash = cash_return(300, 100)
        else:
            cash = cash_rebate(0.8)
        return cash


# 策略模式实现 添加了一个维护的类
class cash_context(object):
    def __init__(self, csuper):
        self.csuper = csuper

    def get_result(self, money):
        return self.csuper.accept_cash(money)

# 策略模式与简单工厂的结合
class cash_context_factory(object):

    def __init__(self, type):
        if type == "正常收费":
            self.cash = cash_normal()
        elif type == "满减":
            self.cash = cash_return(300, 100)
        else:
            self.cash = cash_rebate(0.8)

    def get_result(self, money):
        return self.cash.accept_cash(money)


if __name__ == '__main__':
    # face_process()
    # csuper = cash_factory().create_cash_accept("打折")
    # total_price = csuper.accept_cash(400)
    # print(total_price)
    total_price = cash_context_factory("满减").get_result(400)
    print(total_price)
    pass
