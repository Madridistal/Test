# 有一个字符串hello python，判单字符串中有没有字母p，如果有就输出 包含p，没有就输出不包含p

str_1 = 'hello python'
# str_1 = 'hello world'

for i in str_1:
    if i == 'p':
        print('include p')
        break
else:
    print('no p')
