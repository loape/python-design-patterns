# -*- coding: utf-8 -*-
__author__ = "shizhiwei"


# @Time    : 2020/11/4 10:14
# Email    : shizhiwei@canway.net
# instruction : 设计模式之备忘录模式

class game_role(object):
    """
    game_role : 游戏角色类，用来存储角色的攻击力，生命力，防御力的数据
    """

    def __init__(self, vitality=100, attack=100, defense=100):
        self.vitality = vitality
        self.attack = attack
        self.defense = defense

    def shwo_state(self):
        print("角色当前状态：")
        print("生命力：%s" % self.vitality)
        print("攻击力：%s" % self.attack)
        print("防御力：%s" % self.defense)

    def boss_fight(self):
        self.defense = 0
        self.vitality = 0
        self.attack = 0

    def save_state(self):
        return role_state_memento(self.vitality, self.attack, self.defense)

    def recovery_state(self, memento):
        self.vitality = memento.vit
        self.attack = memento.atk
        self.defense = memento.defense


class role_state_memento(object):
    """
    role_state_memento : 角色状态存储箱
    """

    def __init__(self, vit, atk, defense):
        self.vit = vit
        self.atk = atk
        self.defense = defense


class role_state_caretaker(object):
    """
    role_state_caretaker ： 角色状态管理者
    """

    def set_role_caretaker(self, memento):
        self.__memento = memento

    def get_role_caretaker(self):
        return self.__memento


if __name__ == "__main__":
    # 大战boss前
    role = game_role()
    role.shwo_state()

    # 保存进度
    caretaker = role_state_caretaker()
    caretaker.set_role_caretaker(role.save_state())

    # 大战boss
    role.boss_fight()
    role.shwo_state()

    # 恢复状态
    role.recovery_state(caretaker.get_role_caretaker())
    role.shwo_state()

    pass
