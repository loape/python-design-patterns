# -*- coding: utf-8 -*-
# __author__ = "shizhiwei"
# @Time    : 2020/10/30 19:49
# Email    : shizhiwei@canway.net
# instruction : 设计模式之抽象工厂模式

# 基本的数据访问方式

class user(object):
    def __init__(self, name, id):
        self.name = name
        self.id = id


# 这里增加一个部门表
class department(object):
    def __init__(self, name, id):
        self.depname = name
        self.depid = id


class sql_server(object):
    def get_user(self, id):
        print("从sql-server中得到用户%s" % id)

    def insert(self, user):
        print("向sql数据库中插入一条%s信息" % user)


# 工厂方法的模式实现
class interface_user(object):
    '''
    interface_user: 用于客户端访问，解除与具体数据库访问的耦合
    '''

    def insert(self, user):
        pass

    def get_user(self, id):
        pass


class interface_department(object):
    def insert(self, department):
        pass

    def get_department(self, depid):
        pass


class sql_dep(interface_department):
    def insert(self, department):
        print("在sql中插入一条部门信息")

    def get_department(self, depid):
        print("在sql中查询一共部门信息")


class access_dep(interface_department):
    def insert(self, department):
        print("在access中插入一条部门信息")

    def get_department(self, depid):
        print("在access中查询一条部门信息")


class sql_user(interface_user):
    def insert(self, user):
        print("在sql中插入一条用户信息")

    def get_user(self, id):
        print("从sql中获取一条用户信息")


class access_user(interface_user):
    def insert(self, user):
        print("在access中插入一条用户信息")

    def get_user(self, id):
        print("从access中获取一条用户信息")


class interface_factory(object):
    '''
    interface_factory: 定义一个创建访问user表对象的抽象的工厂接口
    '''

    def create_user(self):
        pass

    def create_department(self):
        pass


class sql_factory(interface_factory):
    def create_user(self):
        return sql_user()

    def create_department(self):
        return sql_dep()


class access_factory(interface_factory):
    def create_user(self):
        return access_user()

    def create_department(self):
        return access_dep()


if __name__ == "__main__":
    user_main = user("小明", 1)
    dep_main = department("法务部", 2)
    factory_link = access_factory()
    user_link = factory_link.create_user()
    dep_link = factory_link.create_department()
    user_link.insert(user_main)
    user_link.get_user(1)
    dep_link.insert(dep_main)
    dep_link.get_department(2)
    pass
    # user_main = user("小明", 1)
    # sql_operate = sql_server()
    # sql_operate.insert(user_main)
    # sql_operate.get_user(user_main.id)
