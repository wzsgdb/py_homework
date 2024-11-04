books ={
    "wzsgdb的书":"wzsgdb",
    "2024":"2",
    "python入门":"python1",
    "python高手":"python2", 
}
#查询书籍：根据书名查询对应的作者。
def get_book_code(book_name):
    if book_name in books:
        print(books[book_name])
    else:
       print("书名不存在")
       
       
       
#添加书籍：将书名和作者添加到字典中
def add_book(book_name,book_code):
    if book_name not in books:
        books[book_name] = book_code
        print( "添加成功")
    else:
        print( "书ming已存在")
        
        
        
#删除书籍：根据书名从字典中删除书籍。
def delete_book(book_name):
    if book_name in books:
        del books[book_name]
        print( "删除成功")
    else:
        print( "书名不存在")
    
    
    
#列出所有书籍：打印出字典中的所有书籍和作者。
def print_books():
    print("所有书籍")
    for book_name,book_code in books.items():
        
        print(book_name,book_code)
        print("-")
        
        
        
#test测试
switch = {
    "1":get_book_code,
    "2":add_book,
    "3":delete_book,
    "4":print_books,
}
while True:
    print("1.查询书籍")
    print("2.添加书籍")
    print("3.删除书籍")
    print("4.列出所有书籍")
    print("5.退出程序")
    choice = input("请输入选项：")
    if choice == "5":
        break
    if choice in switch:
        switch[choice]()
    else:
        print("输入错误，请重新输入")