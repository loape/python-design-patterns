# -*- coding: utf-8 -*-
# __author__ = "shizhiwei"
# @Time    : 2020/10/28 14:25
# Email    : shizhiwei@canway.net
# instruciton : 设计模式之观察者模式

# 抽象方法模块 用于抽象类
import abc


# 双向耦合的代码
# 炒股同事类
class stock_mate(object):

    def __init__(self, name, secretry):
        self.name = name
        self.secretary = secretry

    # 更新动作
    def update_action(self):
        print("%s,%s,关闭股票行情 继续工作" % (self.secretary.action, self.name))


# 秘书类
class secretary(object):
    # 参与炒股的同事
    workmate_list = []

    def __init__(self, action):
        self.action = action

    # 添加新的同事
    def add_workmate(self, workmate):
        self.workmate_list.append(workmate)

    # 通知同事
    def notify(self):
        for item in self.workmate_list:
            print("%s,%s请回去工作！" % (item.name, self.action))

    def set_action(self, action):
        self.action = action


# 解耦实践
class interface(object):
    """
    interface 一个抽象接口,用于抽象“通知人-前台” 对象

    @func add_mate 添加对象到通知列表
    @func del_mate 删除通知列表中对象
    @func notify 通知列表中对象
    @func setting_state 通知者状态setget方法
    """

    def add_mate(self, worker):
        pass

    def del_mate(self, worker):
        pass

    def notify_all(self, worker):
        pass

    def setting_state(self, action):
        pass

    def getting_state(self):
        pass
    pass


class boss(interface):
    """
    boss 继承通知者接口
    """
    work_list = []

    def add_mate(self, worker):
        self.work_list.append(worker)

    def del_mate(self, worker):
        self.work_list = [item for item in self.work_list if item != worker]

    def notify(self):
        for item in self.work_list:
            item.update()

    def setting_state(self, action):
        self.action = action

    def getting_state(self):
        return self.action


class observer(metaclass=abc.ABCMeta):
    """
    observer 抽象类 将观察者实例抽象出来
    """

    def __init__(self, name, worker):
        '''
        :param name: 同事的名字
        :param worker: 原来是前台 现在改成抽象观察者
        '''
        self.name = name
        self.worker = worker

    @abc.abstractmethod
    def update(self):
        pass


class stock_observer(observer):
    """
    stock_observer 炒股的同事
    """
    def update(self):
        print("%s %s关闭股票行情，继续工作！"%(self.worker.getting_state(), self.name))


if __name__ == "__main__":

    shizhiwei = boss()  # 老板史志伟
    tongshi_first = stock_observer("李华", shizhiwei)
    tongshi_second = stock_observer("韩梅梅", shizhiwei)

    shizhiwei.add_mate(tongshi_first)
    shizhiwei.add_mate(tongshi_second)

    shizhiwei.del_mate(tongshi_second)

    shizhiwei.setting_state("不好啦不好啦，老师来了")


    shizhiwei.notify()

    pass
