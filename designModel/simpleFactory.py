# -*- coding: utf-8 -*-
# __author__ = "shizhiwei"
# @Time    : 2020/10/14 14:27
# Email    : shizhiwei@canway.net
# instruction：设计模式的理解

# 面向过程开发
def face_process():
    # 输入
    try:
        number_first = int(input("请输入第一个数字: "))
        number_second = int(input("请输入第二个数字: "))
        operate = input("请输入运算符号（+-/*）： ")

        # 运算处理
        '''
        这里补充一点 python 不支持 switch 的原因
        实现Switch Case 需要被判断的变量是可哈希的和可比较的，这与python倡导的灵活性有冲突，在实现上，优化不好做
        '''

        if operate == '+':
            return number_first + number_second
        elif operate == '-':
            return number_first - number_second
        elif operate == '*':
            return number_first * number_second
        else:
            if number_second == 0:
                return "分母不能为0"
            else:
                return number_first / number_second
    except ValueError:
        print("输入有误，请重新输入")


# 面向对象开发

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


###简单工厂模式
class operation_factory(object):
    oper = operation()

    def create_operate(self, operate):
        if operate == '+':
            oper = operation_add()
        elif operate == '-':
            oper = operation_sub()
        elif operate == '*':
            oper = operation_mul()
        else:
            oper = operation_div()
        return oper


if __name__ == '__main__':
    # result_operate = face_process()
    # print(result_operate)
    oper = operation_factory().create_operate("+")


    oper.first_number = 1
    oper.second_number = 2

    result = oper.get_result()
    print(result)
