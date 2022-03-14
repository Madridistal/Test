class People(object):
    country = 'china'

    # 类方法，用classmethod来进行修饰
    @classmethod
    def get_country(cls):
        return cls.country

    @classmethod
    def set_country(cls, country):
        cls.country = country


p = People()
print(p.get_country())  # 可以用过实例对象访问
print(People.get_country())  # 可以通过类访问

p.set_country('japan')

print(p.get_country())
print(People.get_country())
