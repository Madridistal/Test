name = 'gegou'
intelligence = 250
pi = 3.1415
print('我的名字是%s' % name)
print('我的智商是%d%%' % intelligence)  # ctrl d 快速复制本行代码；输出%需要%%
print('圆周率是%f' % pi)  # %f 默认保存6位小数
print('近似圆周率是%.2f' % pi)  # %.nf 保存n位小数
print('我的名字是%s，我的智商是%d，圆周率是%f' % (name, intelligence, pi))

# f-string如下格式，用{}占位，填充的数据名称直接写在{}里
print(f'我的名字是{name}，我的智商是{intelligence}，圆周率是{pi}')

# f-string如何控制小数位数
print(f'圆周率是{pi:.2f}')

# 一行print执行完会自动换行，不想换行可以用end=来进行连接
print('hello', end='+')
print('world')

# 单个print中需要换行用\n
print('hello\nworld')
print('%d%%' % intelligence)