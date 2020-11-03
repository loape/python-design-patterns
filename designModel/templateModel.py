# -*- coding: utf-8 -*-
# __author__ = "shizhiwei"
# @Time    : 2020/10/22 16:26
# Email    : shizhiwei@canway.net
# Instruction : 设计模式之模板方法模式
import abc


# 两个人的试卷
class test_paper_a(object):
    def test_question_one(self):
        print("第一题")
        print("答案是:A")

    def test_question_second(self):
        print("第二题")
        print("答案是:B")


class test_paper_b(object):
    def test_question_one(self):
        print("第一题")
        print("答案是:A")

    def test_question_second(self):
        print("第二题")
        print("答案是:B")


# 提炼以上代码
class test_paper(object):
    def test_question_a(self):
        print("第一题")

    def test_question_b(self):
        print("第二题")


class test_paper_c(test_paper):
    def test_question_a(self):
        test_paper.test_question_a(self)
        print("答案：A")

    def test_question_b(self):
        test_paper.test_question_b(self)
        print("答案： B")


class test_paper_d(test_paper):
    def test_question_a(self):
        test_paper.test_question_a(self)
        print("答案：C")

    def test_question_b(self):
        test_paper.test_question_b(self)
        print("答案： C")


# 模板方法

class test_paper_base(metaclass=abc.ABCMeta):
    def test_question_one(self):
        print("第一题")
        print("答案：" + self.answer_one())

    def test_question_two(self):
        print("第二题")
        print("答案：" + self.answer_two())

    @abc.abstractmethod
    def answer_one(self):
        return ""

    @abc.abstractmethod
    def answer_two(self):
        return ""


class test_paper_e(test_paper_base):
    def answer_one(self):
        return "A"

    def answer_two(self):
        return "B"


class test_paper_f(test_paper_base):
    def answer_one(self):
        return "A"

    def answer_two(self):
        return "B"


if __name__ == '__main__':
    test_one = test_paper_e()
    test_one.test_question_one()
    test_one.test_question_two()

    test_two = test_paper_f()
    test_two.test_question_one()
    test_two.test_question_two()
