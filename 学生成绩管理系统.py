students={
    "张三":100,
    "李四":1002,
    "王五":1003,
}
#添加学生函数
def add_student(name,num):
    if name in students:
        print("学生已存在")
    else:
        students[name]=num
    
    
#删除学生函数
def delete_student(name):
    del students[name]
    
    
#修改学生函数
def modify_student(name,new_num):
    students[name]=new_num
    
    
#查询学生函数
def search_student(name):
    if name in students:
        print(name,"的成绩是",students[name])
    else:
        print("没有找到",name,"的成绩")
        
        
#显示所有学生函数
def show_all_students():
    for name in students:
        print(name,"的成绩是",students[name])
        
        
# 测试
delete_student("张三")
modify_student("王五","1004")
search_student("王五")
show_all_students()

while True:
    print("1.添加学生")
    print("2.删除学生")
    print("3.修改学生")
    print("4.查询学生")
    print("5.显示所有学生")
    print("6.退出系统")
    choice=input("请输入你的选择:")
    if choice=="1":
        name=input("请输入学生姓名:")
        num=input("请输入学生成绩:")
        add_student(name,num)
    elif choice=="2":
        name=input("请输入学生姓名:")
        delete_student(name)
    elif choice=="3":
        name=input("请输入学生姓名:")
        new_num=input("请输入新的学号:")
        modify_student(name,new_num)
    elif choice=="4":
        name=input("请输入学生姓名:")
        search_student(name)
    elif choice=="5":
        show_all_students()
    elif choice=="6":
        break
    else:
        print("输入错误，请重新输入")
