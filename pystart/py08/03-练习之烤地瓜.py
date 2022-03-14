"""
烤地瓜规则：
• 1.地瓜有自己的状态，默认是生的，地瓜可以进行烧烤
• 2.地瓜有自己烧烤的总时间，由每次烧烤的时间累加得出
• 3.地瓜烧烤时，需要提供本次烧烤的时间
• 4.地瓜烧烤时，地瓜状态随着烧烤总时间的变化而改变：［ 0,3） 生的、［ 3, 6） 半生不熟、［ 6, 8） 熟
了、＞=8 烤糊了
• 5.输出地瓜信息时，可以显示地瓜的状态和烧烤的总时间
"""


class Potato(object):

    def __init__(self, num):
        self.num = num
        self.time = 0
        self.status = '生的'
        self.seasoning = []

    def cook(self, time):
        self.time += time
        if self.time < 3:
            self.status = '是生的'
        elif self.time < 6:
            self.status = '是半生不熟的'
        elif self.time < 8:
            self.status = '熟了'
        else:
            self.status = '烤糊了'

    def add(self, name):
        self.seasoning.append(name)

    def __str__(self):
        if self.seasoning:
            seasoning = ', '.join(self.seasoning)
            return f'{self.num}号地瓜{self.status}, 烤制总时长为{self.time}, 调料有{seasoning}'
        else:
            return f'{self.num}号地瓜{self.status}, 烤制总时长为{self.time}, 还没有添加调料'


potato1 = Potato(1)
potato1.cook(2)
print(potato1)
potato1.cook(3)
print(potato1)
potato1.cook(1)
print(potato1)
potato1.add('辣椒')
potato1.add('蜂蜜')
print(potato1)
potato1.cook(12)
print(potato1)