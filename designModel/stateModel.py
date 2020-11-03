# -*- coding: utf-8 -*-
# __author__ = "shizhiwei"
# @Time    : 2020/11/3 9:28
# Email    : shizhiwei@canway.net
# instruction : 设计模式之状态模式

import abc


class state(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def write_program(self, work):
        pass


class forenoon_state(state):  # 上午工作状态
    def write_program(self, work):
        if (work.hour < 12):
            print("当前时间：%s 上午工作，精神百倍" % work.hour)
        else:
            work.set_state(noon_state())
            work.write_program()


class noon_state(state):  # 中午工作状态
    def write_program(self, work):
        if (work.hour < 13):
            print("当前时间： %s, 饿了，午饭。犯困，午休" % work.hour)
        else:
            work.set_state(afternoon_state())
            work.write_program()


class afternoon_state(state):  # 下午工作状态
    def write_program(self, work):
        if (work.hour < 17):
            print("当前时间： %s, 下午状态不错，继续努力" % work.hour)
        else:
            work.set_state(evening_state())
            work.write_program()


class evening_state(state):  # 晚上工作状态
    def write_program(self, work):
        if (work.finish):
            work.set_state(rest_state())
            work.write_program()
        else:
            if (work.hour < 21):
                print("当前时间： %s, 加班，累了" % work.hour)
            else:
                work.set_state(sleep_state())
                work.write_program()


class sleep_state(state):  # 睡眠状态
    def write_program(self, work):
        print("当前时间： %s, 爷睡了" % work.hour)


class rest_state(state):  # 休息状态
    def write_program(self, work):
        print("当前时间： %s, 下班回家了" % work.hour)


class work(object):

    def __init__(self, state, hour):
        '''
        :param state: 当前状态，初始化的时候初始化为早晨
        :param hour: 当前时间，状态转换的依据
        '''
        self.current = state
        self.hour = hour
        self.finish = False  # 任务是否完成

    def set_state(self, state):
        self.current = state

    def write_program(self):
        self.current.write_program(self)


if __name__ == '__main__':
    emergency = work(forenoon_state(), 9)
    emergency.write_program()
    emergency.hour = 10
    emergency.write_program()
    emergency.hour = 12
    emergency.write_program()
    emergency.hour = 13
    emergency.write_program()
    emergency.hour = 14
    emergency.write_program()
    emergency.hour = 17
    emergency.finish = True
    emergency.write_program()
    emergency.hour = 19
    emergency.write_program()
    emergency.hour = 22
    emergency.write_program()
