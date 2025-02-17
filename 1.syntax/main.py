"""
import sys

print(sys.version)
"""

#1. Python syntax
"""
print('hellow')

if 2 > 1:
    print('hjhee')

x = 4
y = 'heheheh'
"""
#2. Python variable
"""
x = 5
y = "hieuld02"
print(x)
print(y)

##Variables do not need to be declared with any particular type, and can even change type after they have been set.
number = 4
number = 'four'
print(number)

##Casting
x = str(3)
y = int(3)
z = float(3)
print(x, y, z)

##Get the Type
print(type(x))
print(type(y))
print(type(z))

##Assign Multiple Values
###Many Values to Multiple Variables
x, y, z = "hieu",'hehe', 'jhe'
print(x, y, z)

###One Value to Multiple Variables
x = y = z = "heheh"
print(x, y, z)

###Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x, y, z)

##Global Variables
x = "awesome"

def printData():
    print("print " + x)

printData()

def printData():
    x = 'new version'
    print('ss ' + x)

printData()

def printData():
    global x
    x = 'new assign global variable'
    print('ss ' + x)

printData()
"""

# #3.Python Data Types
# """"""
# ##3.1 Python number
# ### int
# ### float
# ### complex
# ### string 
# #### string literals
# print("hello")
# print('hello')
# #### multiline string
# x = """dawdaw
# dwadaw
# dawdawdwa"""
# print(x)
# #### Get a charactor in string
# x = "hello hieuld02"
# print(x[2])

# ##3.2 Python boolean
# ### Allway value is true
# """
# all string is true except empty string
# all number is true except 0
# all list, tuple, set, dictionary is true, except empty
# """

# ##3.3 Python Lists
# """
# List là một tập hợp được sắp xếp và có thể thay đổi. Trong Python, list được viết bằng dấu ngoặc vuông.
# """
# # Tạo list bằng dấu []
# my_list = [1, 2, 3, 4, 5]
# print(my_list)
# # List có nhiều kiểu dữ liệu khác nhau
# mixed_list = [1, "hello", 3.14, True]
# print(mixed_list)

# # List rỗng
# empty_list = []
# print(empty_list) 


# # Truy cập theo chỉ mục (index bắt đầu từ 0)
# numbers = [10, 20, 30, 40, 50]
# print(numbers[1])
# print(numbers[-1])

# # Các thao tác trên list
# my_list = [1, 2, 3]

# # Thêm phần tử vào cuối danh sách
# my_list.append(4)

# # Thêm nhiều phần tử vào danh sách
# my_list.extend([2,3,4])
# new_list = [2,3,4]
# my_list.extend(new_list)
# print(my_list)

# # Chèn phần tử vào vị trí cụ thể
# my_list.insert(1, 2000)
# print(my_list)

# # Xóa phần tử theo giá trị
# my_list.remove(2)
# print(my_list)

# # Xóa phần tử theo chỉ mục

# del my_list[1]
# print(my_list)

# # Lấy phần tử cuối cùng ra khỏi list (và trả về nó)
# last_item = numbers.pop()
# print(last_item) 
# print(numbers)  

# #  Cắt danh sách (List Slicing)
# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(my_list[2:5])
# print(my_list[:5])

# # Lấy các phần tử cách nhau 2 bước
# print(my_list[::2])

# # Đảo ngược danh sách
# print(my_list[::-1])

# # Các thao tác hữu ích trên list
# numbers = [3, 1, 4, 1, 5, 9]
# #  count 
# print(numbers.count(1))

# # index 
# print(numbers.index(1))

# # sort
# numbers.sort()
# print(numbers)

# numbers.sort(reverse=True)
# print(numbers)

# # reverse
# numbers.reverse()
# print(numbers)





# ##3.4. Python tuples
# """
# Trong Python, tuple là một cấu trúc dữ liệu bất biến (immutable), có thể lưu trữ nhiều phần tử giống như list, nhưng một khi đã tạo, không thể thay đổi nội dung của nó.
# """

# tuple = ('hieu', 'ld', '02')
# print(tuple)
# print(tuple[1])

# # tuple with , charactor
# thistuple = ("apple",)
# print(type(thistuple))

# #NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))

# thistuple = tuple(("apple", "banana", "cherry")) # lưu ý 2 cặp dấu ngoặc tròn
# print(thistuple)

# ##3.5. Python Sets
# """
# Trong Python, set là một kiểu dữ liệu dùng để lưu trữ một tập hợp các phần tử không trùng lặp và không có thứ tự. Nó rất hữu ích khi bạn cần loại bỏ các phần tử trùng nhau hoặc thực hiện các phép toán tập hợp như giao, hợp, hiệu.
# """
# ### Tạo set
# mySet = {1, 2, 3, 4, 5}
# print(mySet)

# ### Tạo set từ list bằng hàm set
# list_numbers = {1, 2, 3, 4, 5, 1, 2, 3, 4}
# unique_number = set(list_numbers)

# ### set rỗng p tạo bằng set(), vì {} sẽ tạo dictionary
# my_set = {}
# print(type(my_set))

# ### Các phép toán cơ bản với set
# #### Union
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# print(A | B)
# print(A.union(B))

# #### Interset (Giao)
# print(A & B)
# print(A.intersection(B))

# #### Diffirence (Hiệu)
# print(A - B)
# print(A.difference(B))

# #### Symmetric Difference (Phần tử đối xứng)
# print(A ^ B)
# print(A.symmetric_difference(B))

# #Thao tác với set
# my_set = {1, 2, 3}

# # Thêm phần tử
# my_set.add(4)
# print(my_set)

# # Xóa phần tử (nếu tồn tại, tránh lỗi)
# my_set.discard(2)
# print(my_set)

# # Xóa phần tử bằng remove() (lỗi nếu không tồn tại)
# my_set.remove(1)
# print(my_set)

# # Lấy ngẫu nhiên một phần tử (và xóa nó)
# popped_value = my_set.pop()
# print("popped_value " , popped_value)  # Output: 1 (hoặc 4 tùy Python)
# print(my_set)  # Output: {4}

# # Kiểm tra phần tử có trong set không
# print(1 in my_set)
# print(4 in my_set)
# print(my_set)

# # 3.5. Python Dictionary
# """
# rong Python, dictionary (từ điển) là một cấu trúc dữ liệu dạng key-value, cho phép lưu trữ và truy xuất dữ liệu nhanh chóng bằng cách sử dụng key thay vì index như list hoặc tuple.
# """

# # Tạo dictionary bằng dấu {}
# my_dict = {
#     "name": "hieuld02",
#     "age": 23
# }

# print(my_dict)

# # Tạo dictionary bằng hàm dict()
# my_dict = dict(name="hieuld02", age=23)
# print(my_dict)

# # Dictionary rỗng
# empty_dic = {}
# print(empty_dic)
# print(type(empty_dic))

# # Dictionary có key là số hoặc tuple
# data = {
#     1: "hehe",
#     (2,3): "231"
# }

# print(data)

# # Truy cập giá trị trong dict
# data = {
#     1: "hehe",
#     (2,3): "231"
# }

# print(data[(2,3)])
# print(data.get((2,3)))

# #  Thêm, cập nhật và xóa phần tử trong dict
# # Thêm key mới
# data["he"] = "dwa"
# print(data)

# # Cập nhật giá trị của key đã tồn tại
# data["he"] = "hhehehe"
# print(data)

# # Xóa phần tử
# del data["he"]
# print(data)

# # Xóa bằng pop() (trả về giá trị bị xóa)
# del_data = data.pop((2,3))
# print(del_data)
# print(data)

# # Xóa toàn bộ dictionary
# data.clear()
# print(data)

# # Duyệt qua dictionary
# # Duyệt qua key
# person = {"name": "Alice", "age": 25, "city": "New York"}
# for key in person:
#     print(key)

# for value in person.values():
#     print(value)

# # Duyệt qua cả key và value
# for key, value in person.items():
#     print(f"{key} {value}")

# # Kiểm tra key có tồn tại trong dict không?
# print("naame" in  person)

# # 4.Python If ... Else

# a = 200
# b = 300
# c = 599
# if a < b and c > b:
#     print('hehe')

# if (a  > b) or (c > b):
#     print('daw')

# if not a > b:
#     print('dwa')

# if not a > b:
#     if c > b:
#         print('dwawa')

# if (200):
#     pass

# # 5.Python While Loops

# # 6.Python for loops
# list = [1,2,3,4,5]
# for number in list:
#     print(number)
    
# for number in range(0, 4):
#     print(number)
    
# for charactor in 'hieuld02':
#     print(charactor)
    
# info = {'name': 'hieu', 'nunber': 20}
# for key, value in info.items():
#     print(key, value)
    
# # 7. Python functions    

# def test_function():
#     print('hehe')
#     return 2

# x = test_function()
# print(x)

# ## function with argurment
# def sum(a, b):
#     return a + b

# print(sum(1,2))


# ## function with default argument's value
# def show_info(name, age = 10):
#     print(f'name: {name}, age: {age}')
    
# show_info('hieuld02')

# ## function return many value
# def get_info():
#     return "hieuld02", 10, 'hoai duc'

# name, age, address = get_info()

# print(name, age, address)

# # 8.Python Lambda
# ## lambda arguments : expression

# sum = lambda a,b : a + b
# print(sum(1,2))

# ## lamblda using in map
# numbers = [1,2,3,4,5]
# result = list(map(lambda x: x * x, numbers))
# print(result)

# ## lamblda using in filter
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)

# # # 9. Python Classes and Objects
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def info(self):
#         print(f'{self.name}, {self.age}')
        
# person1 = Person('hieu', 20)
# person1.info()

# ## attrribute and method of class
# ### Add new atrribute
# person1.address = 'ha tay'
# print(person1.address)

# ## chnage attribute
# person1.address = 'hanoi'
# print(person1.address)

# ## remove a attribute
# del person1.address

# ## diffirence class's attribute and object's attribute
# class Student:
#     school = "Hoai Duc B" # Thuộc tính lớp
    
#     def __init__(self, name):
#         self.name = name # Thuộc tính đối tượng
        
# student1 = Student("A")
# student2 = Student("B")

# print(student1.school)
# print(student2.school)

# Student.school = "Hoai Duc A"
# print(student1.school)
# print(student2.school)
# print(student1.name)
# print(student2.name)
        
## Method class and method object

# class Student:
#     school = "Hoai Duc B"
    
#     def __init__(self, name):
#         self.name = name
    
#     def info(self):
#         print(f'hello, {self.name}, {self.school}')
        
#     @classmethod
#     def change_school_name(cls, new_school_name):
#         cls.school = new_school_name
        
#     @staticmethod
#     def anotation():
#         print('hellowowowowo')
        
# student1 = Student('hieuld02')
# student1.info()
# student1.change_school_name('Hoai Duc A')
# student1.info()
# Student.anotation()

# # 10. Python Inheritance
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def info(self):
#         print(f'{self.name} {self.age}')
        
#     def eat(self):
#         print("eating")
        
# class Student(Person):
#     def __init__(self, name, age, school):
#         super().__init__(name, age)
#         self.school = school
    
#     def info(self):
#         print(f'{self.name} {self.age} {self.school}')   
        
#     def eat_lunch(self):
#         super().eat()
#         print('lunch')
    
        
# student = Student('hieu', 20, 'HOD')
# student.info()
# student.eat()
# student.eat_lunch()

# ## Multiple Inheritance - Hỗ trợ đa kế thừa

# # 11. Python Polymorphism
# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand
        
#     def move(self):
#         print('move!')
        
# class Car(Vehicle):
#     def move(self):
#         print('go')
        
# car = Car('ejj')
# car.move()

# # 12. Python Abstraction
# from abc import ABC, abstractmethod

# # Định nghĩa lớp trừu tượng
# class DongVat(ABC):
#     @abstractmethod
#     def keu(self):  # Phương thức trừu tượng
#         pass

# # Lớp con kế thừa và triển khai phương thức keu
# class Meo(DongVat):
#     def keu(self):
#         return "Meo meo"

# class Cho(DongVat):
#     def keu(self):
#         return "Gâu gâu"

# # Tạo đối tượng từ lớp con
# meo = Meo()
# cho = Cho()
# print(meo.keu())  # Meo meo
# print(cho.keu())  # Gâu gâu

# # 13.Python Modules
#  #Module trong Python là một file chứa mã Python (.py) có thể được sử dụng lại trong các chương trình khác.
#  #Module giúp tái sử dụng code, tổ chức chương trình tốt hơn, và tránh trùng lặp.
 
# import math_util
# print(math_util.sum(1,2))

# ## Import toàn bộ module
# import math_util
# ## Import một phần của module
# from math_util import sum
# ## Import với tên khác (alias)
# import math_util as math
# ## Import tất cả các hàm
# from math_util import *


# 14. Python Try Except




    