# -*- coding: utf-8 -*-
__author__ = "shizhiwei"

# @Time    : 2020/11/4 14:44
# Email    : shizhiwei@canway.net
# instruction : 设计模式之组合模式
import abc


class company(metaclass=abc.ABCMeta):
    """
    company : 抽象类接口
    """

    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def add(self, company):
        pass

    @abc.abstractmethod
    def remove(self, company):
        pass

    @abc.abstractmethod
    def display(self, depth):
        pass

    @abc.abstractmethod
    def line_of_duty(self):
        pass


class concrete_company(company):
    """
    concrete_company : 具体公司类，树枝节点
    """
    def __init__(self, name):
        super().__init__(name)
        self.children_list = []

    def add(self, company):
        self.children_list.append(company)

    def remove(self, company):
        self.children_list.remove(company)

    def display(self, depth):
        print('-' * depth + self.name)
        for item in self.children_list:
            item.display(depth + 2)

    def line_of_duty(self):
        for item in self.children_list:
            item.line_of_duty()


class hr_department(company):
    """
    hr_department : 人力资源部 叶节点
    """

    def add(self, company):
        pass

    def remove(self, company):
        pass

    def display(self, depth):
        print('-' * depth + self.name)

    def line_of_duty(self):
        print("%s员工配训管理" % self.name)


class finance_department(company):
    """
    finance_department : 财政部
    """
    def add(self, company):
        pass

    def remove(self, company):
        pass

    def display(self, depth):
        print('-' * depth + self.name)

    def line_of_duty(self):
        print("%s公司财务收支管理" % self.name)


if __name__ == "__main__":

    root_company = concrete_company("北京总公司")
    root_company.add(hr_department("总公司人力资源部"))
    root_company.add(finance_department("总公司财务部"))

    comp_company = concrete_company("上海华东分公司")
    comp_company.add(hr_department("华东分公司人力资源部"))
    comp_company.add(finance_department("华东分公司财务部"))
    root_company.add(comp_company)

    comp_company_first = concrete_company("南京办事处")
    comp_company_first.add(hr_department("南京办事处人力资源部"))
    comp_company_first.add(finance_department("南京办事处财务部"))
    comp_company.add(comp_company_first)

    comp_company_second = concrete_company("杭州办事处")
    comp_company_second.add(hr_department("杭州办事处人力资源部"))
    comp_company_second.add(finance_department("杭州办事处财务部"))
    comp_company.add(comp_company_second)


    root_company.display(1)
    root_company.line_of_duty()

    pass
