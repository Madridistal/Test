# # 键盘录入苹果的价格重量，求总价
# price = input('苹果的价格是：')
# weight = input('苹果的重量是：')
# result = float(price) * float(weight)
# print('苹果单价位%s元，买了%s斤苹果，共%f元' % (price, weight, result))
# print(f'苹果单价位{price}元，买了{weight}斤苹果，共{result}元')

# eval()，还原原本数据类型，效果等同于去除''
num1 = '10'
num2 = 12
num3 = 'num2'
num11 = eval(num1)
num31 = eval(num3)
print(type(num11), type(num31))
print(num11, num31)
a = 12.12
b = 12.63
a1 = int(a)
b1 = int(b)
print(a1, b1)