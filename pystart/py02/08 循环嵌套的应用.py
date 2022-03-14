# sq = eval(input('please input 边长'))
# # i = 0
# # while i < sq:
# #     j = 0
# #     while j < sq:
# #         print('*', end=' ')
# #         j += 1
# #     print()
# #     i += 1

# for i in range(sq):
#     for j in range(sq):
#         print('*', end=' ')
#     print()
# 以上为打印正方形

tr = eval(input('please input 边长'))
i = 1
while i <= tr:
    j = 1
    while j <= i:
        print('*', end=' ')
        j += 1
    print()
    i += 1

for i in range(tr):
    for j in range(i+1):
        print('*', end=' ')
    print()