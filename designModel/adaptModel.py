# -*- coding: utf-8 -*-
__author__ = "shizhiwei"

# @Time    : 2020/11/3 11:13
# Email    : shizhiwei@canway.net
# instruction : 设计模式之适配器模式
import abc


# 篮球翻译适配器

class player(metaclass=abc.ABCMeta):  # 球员抽象类
    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def attack(self):  # 进攻
        pass

    @abc.abstractmethod
    def defense(self):  # 防守
        pass


class forwards(player):  # 前锋
    def attack(self):
        print("前锋%s进攻" % self.name)

    def defense(self):
        print("前锋%s防守" % self.name)


class foreign_forwards(object):  # 中国国籍前锋
    def __init__(self, name):
        self.name = name

    def chinese_attack(self):
        print("中国国籍前锋%s给爷杀"%self.name)

    def chinese_defense(self):
        print("中国国籍前锋%s给爷守住"%self.name)


class translate(player):  # 适配器

    def __init__(self, name):
        self.ford = foreign_forwards
        self.ford.name = name
    def attack(self):
        self.ford.chinese_attack(self.ford)

    def defense(self):
        self.ford.chinese_defense(self.ford)
        pass


if __name__ == "__main__":
    player_a = forwards("麦克")
    player_a.attack()

    player_b = translate("姚明")
    player_b.attack()
    player_b.defense()
