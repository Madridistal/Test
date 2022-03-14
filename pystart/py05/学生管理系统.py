import os


def show_menu():
    print('-' * 30)
    print('1. 添加学生信息')
    print('2. 删除学生信息')
    print('3. 修改学生信息')
    print('4. 查询单个学生信息')
    print('5. 查询所有学生信息')
    print('6. 退出系统')
    print('-' * 30)


def add_stu():
    """添加学生信息"""
    global info_list

    name = input('请输入学生姓名：')

    for i in info_list:
        if i['name'] == name:
            print('学生已在库中，请重新输入')
            return

    gender = input('请输入学生性别：')
    age = input('请输入学生年龄：')
    info = {'name': name, 'gender': gender, 'age': age}   # 用于储存单个学生信息的字典
    info_list.append(info)
    print('=======学生信息成功添加=======')


def del_stu():
    """删除学生信息"""
    global info_list

    name = input('请输入需要删除的学生姓名：')
    for i in info_list:
        if i['name'] == name:
            info_list.remove(i)
            print('该学生信息已删除')
            return
    else:
        print('该学生不在库中')


def cha_stu():
    """修改学生信息"""
    global info_list

    name = input('请输入需要修改信息的学生姓名：')

    for i in info_list:
        if i['name'] == name:
            i['gender'] = input('请修改学生性别：')
            i['age'] = input('请修改学生年龄：')
            return
    else:
        print('该学生不在库中')


def show_1():
    """查询单个学生信息"""
    name = input('请输入需要查询的学生姓名：')

    for stu in info_list:
        if stu['name'] == name:
            print('该学生信息如下：')
            print(f"学生姓名：{stu['name']}, 性别：{stu['gender']}, 年龄：{stu['age']}")
            return
    else:
        print('该学生不在库中')


def show_all():
    """查询所有学生信息"""
    print('库中的学生信息如下：')

    for stu in info_list:
        print(f"学生姓名：{stu['name']}, 性别：{stu['gender']}, 年龄：{stu['age']};")


def load():
    """读取文件信息"""
    global info_list

    if os.path.exists('student.txt'):
        f = open('student.txt', 'r', encoding='utf-8')
        info = f.read()
        if info:
            info_list = eval(info)
        f.close()


def save():
    """保存信息"""
    f = open('student.txt', 'w', encoding='utf-8')
    f.write(str(info_list))
    f.close()


def main():
    load()
    print('欢迎进入学生管理系统')
    while True:
        show_menu()
        num = eval(input('请按数字选择需要的服务：'))
        if num == 1:
            # print('1 添加学生信息')
            add_stu()
        elif num == 2:
            # print('2 删除学生信息')
            del_stu()
        elif num == 3:
            # print('3 修改学生信息')
            cha_stu()
        elif num == 4:
            # print('4 查询单个学生信息')
            show_1()
        elif num == 5:
            # print('5 查询所有学生信息')
            show_all()
        elif num == 6:
            save()
            print('欢迎下次使用！')
            break
        else:
            print('您的输入有误，请重新选择！')
            continue

        input('-------请按回车键继续使用-------')


info_list = []  # 储存信息的列表
main()
