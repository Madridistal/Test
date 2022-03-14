# old_file = open('test.txt', 'rb')
# new_file = open('test备份.txt', 'wb')
# for i in old_file.readlines():
#     new_file.write(i)
# old_file.close()
# new_file.close()

# 提示输入文件
old_file_name = input("请输入要拷贝的文件名字:")

# 以读的方式打开文件
old_file = open(old_file_name, 'rb')

# 提取文件的后缀
file_flag_num = old_file_name.rfind('.')
if file_flag_num > 0:
    file_flag = old_file_name[file_flag_num:]

# 组织新的文件名字
new_file_name = old_file_name[:file_flag_num] + '[复件]' + file_flag

# 创建新文件
new_file = open(new_file_name, 'wb')

# 把旧文件中的数据，一行一行的进行复制到新文件中
for live_content in old_file.readlines():
    new_file.write(live_content)

# 关闭文件
old_file.close()
new_file.close()
