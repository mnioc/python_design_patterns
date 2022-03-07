# !/usr/bin/env python 
# -*- coding: utf-8 -*-

# ------------------#
# 组合模式(对象树): 是一种结构型设计模式， 以使用它将对象组合成树状结构， 并且能像使用独立对象一样使用它们。
# 如果应用的核心模型能用树状结构表示， 在应用中使用组合模式才有价值。
# ------------------#

# 最常见的场景就是企业的部门管理系统了，部门管理系统是具备树型结构的


from abc import ABC, abstractmethod
from typing import List


class Component(ABC):

    @property
    def parent(self) -> 'Component':
        return self._parent
    
    @parent.setter
    def parent(self, parent: 'Component'):
        self._parent = parent

    def add(self, component: 'Component') -> None:
        pass
    
    def remove(self, component: 'Component') -> None:
        pass

    @abstractmethod
    def operation(self) -> str:
        """
        The base Component may implement some default behavior or leave it to
        concrete classes (by declaring the method containing the behavior as
        "abstract").
        """

        pass


class Node(Component):

    def __init__(self, name):
        self.name = name
    
    def operation(self) -> str:
        return self.name
    

class Composite(Component):

    def __init__(self) -> None:
        self._children: List[Component] = []
    
    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self
    
    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None
    
    @property
    def tree(self):
        return self.operation()
    
    def operation(self) -> str:
        """
        The Composite executes its primary logic in a particular way. It
        traverses recursively through all its children, collecting and summing
        their results. Since the composite's children pass these calls to their
        children and so forth, the whole object tree is traversed as a result.
        """

        results = []
        for child in self._children:
            results.append(child.operation())
        
        return results


class Application:

    def run(self):

        depart = Composite()

        branch1 = Composite()
        branch1.add(Node("技术研发部"))
        branch1.add(Node("算法部门"))
        branch1.add(Node("mnio"))

        depart.add(branch1)

        branch2 = Composite()
        branch2.add(Node("行政管理"))
        branch2.add(Node("人力资源"))
        branch2.add(Node("li"))

        depart.add(branch2)

        print(depart.tree)

Application().run()

# output
"""
[
    ['技术研发部', '算法部门', 'mnio'], 
    ['行政管理', '人力资源', 'li']
]
"""