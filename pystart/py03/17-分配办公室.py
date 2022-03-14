# 八个老师随机分配到三个办公室
import random

school = [[], [], []]
teacher = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
for i in teacher:
    j = random.randint(0, 2)
    school[j].append(i)
print(school)
print(type(school))
print('=' * 30)

for i in enumerate('hello world'):
    print(i)
print('=' * 30)

my_tuple = (1,)
print(my_tuple, type(my_tuple))
