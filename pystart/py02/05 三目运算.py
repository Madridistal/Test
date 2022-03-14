a = eval(input("please input a number"))
b = eval(input("please input another number"))

result = a - b if a >= b else b - a  # 扁平化代码

print(result)