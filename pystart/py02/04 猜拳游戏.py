# import random
#
# player = eval(input("请输入：剪刀（0）石头（1）布（2）"))
# com = random.randint(0, 2)  # 产生0到2的随机数
# print(com)
# if ((player == 0) and (com == 2)) or ((player == 1) and (com == 0)) or ((player == 2) and (com == 1)):
#     print("you win")
# elif player == com:
#     print("draw")
# else:
#     print("you lose")

# 循环猜拳
import random

while True:
    player = eval(input("请输入：剪刀（0）石头（1）布（2）"))
    com = random.randint(0, 2)  # 产生0到2的随机数
    print(com)
    if ((player == 0) and (com == 2)) or ((player == 1) and (com == 0)) or ((player == 2) and (com == 1)):
        print("you win")
    elif player == com:
        print("draw")
    else:
        print("you lose")
