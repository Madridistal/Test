def line():
    """
    输出一条横线
    """
    print('*' * 30)


def num(n):
    for i in range(n):
        line()


n = eval(input('输出横线的行数为：'))
num(n)
help(line)
