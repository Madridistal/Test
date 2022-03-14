# # 过7游戏
# i = 1
# while i < 100:
#     if (i % 7 == 0) or (i % 10 == 7) or (i // 10 == 7):
#         print('pass')
#     else:
#         print(i)
#     i += 1

# # 编写登录，要求用户名python密码为123456，输入正确打印欢迎光临，输入错误提示重新输入
# name = 'python'
# password = '123456'
# while 1:
#     user_nam = input('请输入用户名：')
#     user_pass = input('请输入密码：')
#     if (user_nam == name) and (user_pass == password):
#         print('欢迎光临')
#         break
#     else:
#         print('用户名或密码错误，请重新输入！')