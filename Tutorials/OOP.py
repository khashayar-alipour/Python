
"""
        ====================================================================
        ===========      Created on Sun Jun 28 10:48:45 2026     ===========
        ===========         Author: Khashayar Alipour            ===========
        ===========                IDE: spyder                   ===========
        ===========                python OOP                    ===========
        ====================================================================
"""

# what is OOP?
# define a class
# dunder methods
# __name__=="main" ??
# inheritance
# polynominal/polymorphism
# encapsulation
# abstract
# Attributes: 1-instance attribute   2-class attribute
# Decorators: @instancemethod  @staticmethod  @classmethod   
# Methods: 1-instance method   2-static method   3-class method 
# @Property:  getter, setter, deleter




'''
=================================
=================================
======     class in OOP    ======
=================================
=================================
'''

# برای تعریف کردن مفهوم کلاس از مثال خون انسان استفاده میکنیم
# class => کل خون یک انسان
# instance => یک نمونه از خون یک انسان که تمام ویژگی های خون اون شخص مثل قند و چربی و همه چیز داخلش هست

s = "a"
print(type(s))   # <class 'str'>
# متغیر s یک نمونه یا instance از دسته بندی یا کلاس string هست
# این متغیر تمام ویژگی‌ها و رفتارهای کلاس string رو داره


# object = در پایتون هرچیزی که ایجاد و تعریف میشه یک شیء میگن
# هر object دوتا چیز داره: 1-رفتار 2-ویژگی           

# تعریف method:
# در کلاس ها رفتارها همون توابع هستند که البته در مبحث OOP به توابع میگن method    
# مثلا str methods در string class که همون رفتارهای تایپ رشته هست: مثلا upper و strip ...    




#=========================
'''   define a class   '''
#=========================

# طبق اصل PEP8 مدل نوشتاری اسم کلاسها باید pascal case باشه

#________________________________
#   class      |  PascalCase     |
#______________|_________________|
#  variables   |  snake_case     |
#______________|_________________|
# func-method  |  snake_case     |
#______________|_________________|
#  constant    |UPPER_SNAKE_CASE |
#______________|_________________|
#  module      |  snake_case     |
#______________|_________________|
#  package     |  snake_case     |
#______________|_________________|



# 2 روش برای ایجاد کلاسها وجود داره:
    # روش اول با استفاده از متود set_var هست که متعارف نیست و روش دوم استفاده از داندر متود __init__

''' ==== first way ==== '''

class Test:
    def set_var(self,a,b):
        self.a=a
        self.b=b
    
    def add(self):
        return self.a+self.b

    def multiply(self):
        return self.a*self.b


t=Test()       #instance (object)

# میتونیم با روش dot notation به همه ویژگی های کلاس Test با استفاده از نمونه ای که ازش ساختیم دسترسی پیدا کنیم
# در روش اول برای تعریف کلاس، مجبوریم بعد از ساخت نمونه بیایم به Set_var مقداردهی کنیم تا بعد بتونیم از متدهای داخل کلاس استفاده کنیم
t.set_var(2,3)   #a=2  b=3

y=t.multiply()
print(y)   #6


# تمام def هایی که توی این کلاس تعریف کردیم میشن method یا رفتارِ کلاس
# تمام متغیرهایی که با self تعریف ردیم میشن ویژگی یا property یا attribute

#self
# متیغرهایی که در هر تابع تعریف میشن local هستن و نمیشه ازشون در یک تابع دیگه استفاده کرد
# با استفاده از Self میشه یه پل ارتباطی بین توابع داخل کلاس ایجاد کرد که از متغیرهای همدیگه استفاده کنن




''' ==== second way ==== '''

class Book:
    def __init__(self, author, book):
        self.author=author
        self.book=book
        
    def __str__(self):      # این متود بعد از ساختن نمونه بدون اینکه نیاز باشه این متود رو صدا بزنیم یک پیام برامون نمایش میده
        return f"{self.book} is written by {self.author}"    
    
    def __repr__(self):     # این داندر متود فقط پیامی مخصوص توسعه دهنده ها داره
        return "this message is for developers only!"       
    

# گرفتن بیش از 1 مقدار با یک input
author,book = input("enter author and book name: ").split(",")

# حالا نمونه خودمون رو ایجاد میکنیم. اینجا __init__ خودش میاد ورودی هارو میگیره و متغیر های مارو میسازه
t=Book(author,book)
print(t)                  # enter author and book name: author1,book1
                          # book1 is written by author1

# متود vars تمام مقادیر و attribute های یک instance (اونهایی که توی __init__ تعریف شدن) رو بصورت dict نشون میده
print(vars(t))     #{'author': 'author1', 'book': 'book1'}









'''
==========================================
==========================================
======     python dunder methods    ======
==========================================
==========================================
'''
# double underscore
# بهشون magic method هم میگن


''' __init__ '''
# مهمترین داندر متود
# مخفف initiate
# کارش اینه که وقتی یک instance از class میسازیم خودش اجرا میشه و متغیرهارو تعریف میکنه



''' __str__ '''
# وقتی نمونه از کلاس ساخته شد، زمانیکه از نمونه print بگیریم این متود مشخص میکنه چه پیامی نمایش داده بشه

class Student:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

s = Student("Ali")
print(s)    # Ali
# خروجی بدون متود __str__ اینجوری میشد:   <__main__.Student object at 0x...>            



''' __len__ '''
# این متود مشخص میکنه تابع چه مقداری رو برگردونه

class Team:
    def __init__(self, members):
        self.members = members
    def __len__(self):
        return len(self.members)

team = Team(["Ali", "Sara", "Reza"])
print(len(team))    #3




''' __getitem__ '''
# این متود اجازه میده از [] به عنوان عدد ایندکس استفاده کنی

class Team:
    def __init__(self, members):
        self.members = members
    def __getitem__(self, index):
        return self.members[index]

team = Team(["Ali", "Sara", "Reza"])
print(team[1])     #Sara



''' __contains__ '''
# این متود برای عملگر in کاربرد داره

class Team:
    def __init__(self, members):
        self.members = members
    def __contains__(self, item):
        return item in self.members

team = Team(["Ali", "Sara"])
print("Ali" in team)



''' __add__ '''
# این متود برای عملگر + کاربرد داره

class Money:
    def __init__(self, amount):
        self.amount = amount
    def __add__(self, other):
        return Money(self.amount + other.amount)

m1 = Money(100)
m2 = Money(200)
print(m1.amount + m2.amount)    #300



''' __eq__ '''
# این متد برای مقایسه با عملگر == کاربرد داره

class Student:
    def __init__(self, name):
        self.name = name
    def __eq__(self, other):
        return self.name == other.name

s1 = Student("Ali")
s2 = Student("Ali")
print(s1 == s2)    #True



''' __iter__ '''
# این متود برای استفاده در حلقه for کاربرد داره

class Team:
    def __init__(self):
        self.members = ["Ali", "Sara"]
    def __iter__(self):
        return iter(self.members)

team = Team()
for member in team:
    print(member)     #Ali  Sara



''' __call__ '''
# این متود اجازه میده شیء رو مثل تابع صدا بزنی

class Greeting:
    def __call__(self):
        print("Hello")

g = Greeting()
g()     #Hello











'''
=========================================
=========================================
======     __name__=="__main__"    ======
=========================================
=========================================
'''

# پایتون برای هر فایل یک متغیر داخلی به نام __name__ می‌سازد
# مقدار این متغیر بستگی دارد به اینکه فایل را مستقیماً اجرا کرده‌ای یا به عنوان ماژول import شده است


''' ===== direct run ======  '''

# فرض کنیم فایل زیر رو مستقیم اجرا کردیم:
# [test.py فایل]
print(__name__)

# بعد از اجرا شدن این میاد:
    # __main__
    # یعنی این فایل، برنامه اصلی است که الان در حال اجراست    



''' ===== importing file ==== '''

# در این حالت فایل test.py رو به عنوان ماژول وارد main.py میکنیم:
import test.py

# حالا فایل main.py رو اجرا میکنیم و اینجوری از داخلش test.py هم اجرا میشه
# در این حالت این میاد:
__name__ = "test"

# این بار مقدار __name__ برابر نام فایل شده است
# چون فایل test.py مستقیماً اجرا نشده و فقط import شده است


''' ================= '''
# نتیجه گیری      

# پس هروقت فایل اصلی اجرا بشه __name__ برابر __main__ میشه
# هروقت فایل بصورت غیر مستقیم اجرا بشه __name__ برابر نام فایلی میشه که توش تعریف شده

if __name__ == "__main__":
    print('...')
# این خط یعنی کدهای این قسمت فقط زمانی اجرا شوند که فایل مستقیماً اجرا شده باشد، نه زمانی که import شده باشد


# معمولا در هر فایل علاوه بر توابع خود فایل، تعدادی تست هم وجود دارد
# با اینکار از وارد شدن ناخواسته تست ها به فایل مقصد جلوگیری میشه
# این الگو تقریباً در تمام پروژه‌های پایتون برای تست، اجرای برنامه و جلوگیری از اجرای ناخواسته کد هنگام import کردن استفاده می‌شود











'''
================================
================================
======     Inheritance    ======
================================
================================
'''

# یعنی فرزند از والد یک سری ویژگی هارو ارث بری میکنه
# در ارث بری علاوه بر ویژگی های کلاس والد (در متد __init__)، به متدهای کلاس والد هم دسترسی داره
# اگر والد و فرزند یک متد یکسان داشته باشن، اولویت با متدهای فرزند هست که به این ویژگی میگن overwrite کردن


#==================
'''   super()   '''
#==================
# این متود بهمون اجازه میده تا به متد کلاس والد دسترسی پیدا کنیم
# اسم متودی که میخوایم از کلاس بالاتر بهش دسترسی پیدا کنیم رو بعد از super میاریم
# ورودی ها به کلاس فرزند داده میشه، ولی مقداردهی در کلاس والد انجام میشه
# همونطوری که Self نماینده object ما هست، superهم نماینده والد هست
# وقتی از super استفاده میشه دیگه نیازی به استفاده از self نیست و خودش با کلاس والد ارتباط میگیره

# استفاده از متود super فقط زمانی امکان پذیره که ما فقط 1 والد داریم
# اگر 2 تا والد باشن نمیشه از super استفاده کرد
#======================================================================



# 4 نوع ارث بری داریم:

''' 1- Single inheritance   '''      #ارث بری یگانه
#     ___________
#     | Class A |  parent
#     -----------
#         |
#         V
#     ___________
#     | Class B |  child
#     -----------

class Product:
    def __init__(self, id_i, name, number, price):
        self.id_i=id_i
        self.name=name
        self.number=number
        self.price=price
    
    def __str__(self):
        return f"ID of product: {self.id_i} \
            Name of product: {self.name} \
                Number of product: {self.number} \
                    Price of product: {self.price}"
                        
    def get_name(self):
        print(f"name of product is {self.name}")
#_____________________________________________________________________________

class Book(Product):
    def __init__(self, id_i, name, number, price, author):
        super().__init__(id_i, name, number, price)    # no need to use self
        self.author=author
    
    def __str__(self):
        return f" {super().__str__()} \
                        Author of product: {self.author}"
                        
b=Book(10, "book1", 10, 200, 'author1') 
print(b)
 
# ID of product: 10
# Name of product: book1
# Number of product: 10
# Price of product: 200
# Author of product: author1
#_____________________________________________________________________________








''' 2- Multilevel inheritance  '''

#     ___________
#     | Class A |  parent
#     -----------
#         |
#         V
#     ___________
#     | Class B |  child
#     -----------
#         |
#         V
#     ___________
#     | Class C |  child
#     ----------- 

# parent
class Product:
    def __init__(self, id_i, name, category):
        self.id_i = id_i
        self.name=name
        self.category = category
        
    def __str__(self):
        return f"product id: {self.id_i} \
            product name: {self.name} \
                product category: {self.category}"
#______________________________________________________________________________               
    
# child
class ElectronicProduct(Product):
    def __init__(self, id_i, name, category, brand):
        super().__init__(id_i, name, category)
        self.brand = brand
    
    def __str__(self):
        return f"{super().__str__()} - product brand: {self.brand}"
#______________________________________________________________________________
    
# child
class Laptop(ElectronicProduct):
    def __init__(self, id_i, name, category, brand, ram):
        super().__init__( id_i, name, category, brand)
        self.ram = ram
    
    def __str__(self):
        return f"{super().__str__()}, ram: {self.ram}"
    
    
l = Laptop((5), 'asus', 'laptop', 'asus2', 2)
print(l)

# product id: 5
# product name: asus
# product category: laptop
# product brand: asus2
# ram: 2
#______________________________________________________________________________








''' 3- Hierarchial inheritance   '''
# ارث بری سلسه مراتبی یا آبشاری - ارث بری بصورت همزمان

#                 ____________
#                 |  Class A |   parent
#                 ------------
#                      |
#        ________________________________
#        |                              | 
#        V                              V
#  ____________                  ____________
#  |  Class B |                  |  Class C |
#  ------------                  ------------


#       Animal
#       /    \
#      Dog    Cat
      
      
# parent
class Animal:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Animal: {self.name}"

    def eat(self):
        print(f"{self.name} is eating")
#______________________________________________________________________________

# child
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # فراخوانی __init__ والد
        self.breed = breed

    def __str__(self):
        return f"Dog(Name={self.name}, Breed={self.breed})"

    def bark(self):
        print("Woof!")
#______________________________________________________________________________

# child
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)   # فراخوانی __init__ والد
        self.color = color

    def __str__(self):
        return f"Cat(Name={self.name}, Color={self.color})"

    def meow(self):
        print("Meow!")
        


dog = Dog("Rex", "German Shepherd")
cat = Cat("Milo", "White")

print(dog)   # Dog(Name=Rex, Breed=German Shepherd)
print(cat)   # Cat(Name=Milo, Color=White)

dog.eat()    # Rex is eating
dog.bark()   # Woof!

cat.eat()    # Milo is eating
cat.meow()   # Meow!

# اینجا Animal ویژگی مشترک name را نگه می‌دارد
# کلاس Dog علاوه بر name، ویژگی breed دارد
# کلاس Cat علاوه بر name، ویژگی color دارد
# با super().__init__(name) متد __init__ کلاس والد اجرا می‌شود و از تکرار کد جلوگیری می‌شود
#______________________________________________________________________________








''' 4- Multiple inheritance '''

#    parent                         parent
#  ____________                  ____________
#  |  Class A |                  |  Class B |
#  ------------                  ------------
#       |_____________________________|
#                     |
#                 ____________
#                 |  Class C |
#                 ------------
#                     child    یک فرزند از 2 والد ارث بری میکنه

# parent
class Product:
    def __init__(self, id_i, name, category):
        self.id_i = id_i
        self.name=name
        self.category = category
        
    def __str__(self):
        return f"product id: {self.id_i} \
            product name: {self.name} \
                product category: {self.category}"
#______________________________________________________________________________

# parent
class ElectronicProduct:
    def __init__(self, brand):
        self.brand = brand
    
    def __str__(self):
        return f"product brand: {self.brand}"
#______________________________________________________________________________

# child
class Laptop(Product, ElectronicProduct):
    def __init__(self, id_i, name, category, brand, ram):
        Product.__init__(self, id_i, name, category)
        ElectronicProduct.__init__(self, brand)
        self.ram = ram
    
    def __str__(self):
        return f"{Product.__str__(self)}, {ElectronicProduct.__str__(self)}, ram: {self.ram}"
    

l = Laptop((5), 'asus', 'laptop', 'asus2', 2)
print(l)

# product id: 5
# product name: asus
# product category: laptop
# product brand: asus2
# ram: 2

# در قسمت __init__ اومدیم از 2 کلاس والد ارث بری کردیم
# نکته‌ی مهمش اینه که اینجا چون 2 تا والد داریم نمیشه دیگه از super استفاده کرد
# مجبوریم در این حالت بطور دقیق از اسم کلاس استفاده کنیم و مشخص کنیم کدوم والد رو میخوایم
# اگر از super اینجا استفاده بشه فقط والدی که به عنوان ورودی اول به فرزند دادیم (Product) رو تشخیص میده
# نکته دیگه اینه که وقتی از super استفاده میشه دیگه نیازی به استفاده از self نیست و خودش با کلاس والد ارتباط میگیره
# ولی اینجا چون از اسم class استفاده کردیم باید حتما Self هم بیاریم
#______________________________________________________________________________






''' List overview practice  '''
 # در این تمرین میخوایم کلاس List در پایتون رو overwrite کنیم و بهش متد جدید اضافه کنیم یا تغییرات ایجاد کنیم.

class MyList(list):
    
    # اینجا میخوایم متد __init__ در لیست رو overwrite کنیم و تغییر بدیم.   
    # ما میخوایم روی لیست کار کنیم برای همین متغیر ورودی یک لیست میدیم که مقدار پیش فرضش [] هست.   
    def __init__(self,data=[]):   
        if self.all_str(data):     # این شرط بررسی میکنه که اگر دیتای ورودی همه ایتم هاش رشته بود بیا یه نمونه لیست بساز 
            super().__init__(data)
        else:
            raise ValueError ('enter only str')
    
    
    # تابع زیر یک تایع مستقل staticmethod هست که میاد ازون بالا ورودی data که یک ایست هست رو میگیره    
    # اگر این دیتا تک تک ایتم هاش رشته نبوددد false برمیگردونه وگرنه true میده.    
    @staticmethod
    def all_str(data):
        for item in data:
            if not isinstance(item, str):
                return False
    
    
    # میخوایم متد append رو overwrite کنیم. میخوایم جوری بشه که فقططط یک تایپ رشته رو append کنه.    
    # مقدار value میشه مقداری که ما میخوایم append کنیم.    
    def append(self, value):
        if isinstance(value, str):      # type(value)==str
            super().append(value)
        else:
            raise ValueError ('I will only append string!')
    
    
    # میخوایم تابع insert رو جوی تغییر بدیم که فقط str به عنوان ورودی قبول کنه.    
    def insert(self, value, index):
        if isinstance(value, str):
            super().insert(index, value)
        else:
            raise ValueError('only str allowed!')
    
    
    # میخوایم این تابع رو جوری تغییر بدیم که فقط رشته به عنوان ورودی بگیره.    
    def extend(self, new_list):
        if all(isinstance(item, str) for item in new_list):    # آیا همه عناصر لیست ورودی تایپ رشته دارند؟
            super().extend(new_list)
        else:
            raise ValueError ('str only!')
    
    
    # این تابع میاد لیست مارو edit میکنه و ما میخوایم تغییرش بدیم.    
    def __setitem__(self, index, value):
        if isinstance(value, str):
            super().__setitem__(index, value)
        else:
            raise ValueError ('str only')
    
    
    
l1=MyList([1,2,3])


#------- append --------
l1.append(4)        # ValueError: I will only append string!
l1.append('hello')  # [1, 2, 3, 'hello']
print(l1)

#------- insert --------
l1.insert(19, 1)        # ValueError: only str allowd!
l1.insert('hello',1)  # [1, 2, 'hello', 3]
print(l1)

#------- __setitem__ --------
print(l1)          #[1, 2, 3]
l1[0]='strrrr'     #['strrrr', 2, 3]   
l1[0]=4            #ValueError: str only













'''
=================================
=================================
======     polymorphism    ======
=================================
=================================
'''
# یعنی یک تابع در کلاس های مختلف، نقش های مختلف داره و هرکدوم رو جدا اجرا میکنن
# یک تابع با اسم ثابت میتونه در کلاسهای مختلف که از هم ارث‌بری میکنن وجود داشته باشه ولی بدنه توابع متفاوته



# تابع discount در هر 3 کلاس با اسم ثابت ولی بدنه تابع متفاوت و کارایی متفاوت.

#       Product
#      /     \
#   Book     Laptop


# parent
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    
    def __str__(self):
        return f"name: {self.name} - price: {self.price} - category: {self.category}"
    
    def discount(self):
        discount = self.price * 0.1
        self.price-= discount
    
    def show_price(self):
        return f"price: {self.price}"
#______________________________________________________________________________

# child
class Book(Product):
    def __init__(self, name, price, category):
        super().__init__(name, price, category)
    
    def discount(self):
        discount = self.price * 0.15
        self.price-=discount
    
    def show_price(self):
        return f"price: {self.price}"
#______________________________________________________________________________

# child
class Laptop(Product):
    def __init__(self, name, price, category):
        super().__init__(name, price, category)
    
    def discount(self):
        discount = self.price * 0.05
        self.price-=discount
    
    def show_price(self):
        return f"price: {self.price}"
#______________________________________________________________________________
  
    
#______________________________________________________
#______________________________________________________
#______________________________________________________
    
if __name__=='__main__':
    p1=Product('pro1', 3000, 'catp')
    b1=Book('book1', 2000, 'catb')
    l1=Laptop('lap1', 1000, 'catl')
    
    print(p1)                 # name: pro1 - price: 3000 - category: catp
    print(p1.show_price())    # price: 3000
    p1.discount()             # اعمال تخفیف
    print(p1.show_price())    # price: 2700.0
    
    print(b1)                 # name: book1 - price: 2000 - category: catb
    print(b1.show_price())    # price: 2000
    b1.discount()             # اعمال تخفیف
    print(b1.show_price())    # price: 1700.0
    
    print(l1)                 # name: lap1 - price: 1000 - category: catl
    print(l1.show_price())    # price: 1000
    l1.discount()             # اعمال تخفیف
    print(l1.show_price())    # price: 950.0


# حتی اگه تابع show_price از دو کلاس فرزند حذف کنیم بازم میشه عملیات زیر رو انجام داد،
# چون این تابع رو از والد (Product) به ارث میبره:

'''
b1.show_price()
l1.show_price()
'''














'''
==================================
==================================
======     encapsulation    ======
==================================
==================================
'''

# وقتی فرزند از والد ارث بری میکنه به تمام متودهاش دسترسی داره
# بعضی وقتا ما نمیخوایم که این اتفاق بیوفته و میخوایم عملیاتی که انجام میشه از دید کاربر مخفی بمونه
# با capsulate کردن کدها دیگه امکان دسترسی بهشون از لایه های پایین تر وجود نداره

# پس بحثی بوجود میاد بنام سطح دسترسی در کدها:
    # 1- Protected level
    # 2- Private level
    # 3- Public level



#========================================
'''  1- Protected attribute | method  '''
#========================================

# با گذاشتن یک underline پشت اسم attribute اون رو protected میکنیم
# تلاش برای دسترسی به متغیر یا متود protected شده منجر به AttributeError میشه

# اگر یک متود یا attribute (متغیر) سطح protected معرفی بشه
# هم توی خود کلاس و هم از داخل فرزند بهش دسترسی داریم
# ولی از داخل main و داخل کلاس‌های دیگه بهش دسترسی نداریم

# درواقع protected در پایتون یک قرارداد (Convention) است
# وقتی برنامه نویس در مرحله Developement یک protected attribute میبینه
# میگه این متغیر برای استفاده داخل کلاس اصلی و کلاس‌های فرزند طراحی شده و بهتره مستقیم از بیرون بهش دست نزنم



class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price         #protected attribute
    
    def _show_price(self):          #protected method
        return f" Price: {self._price}"
    
    
if __name__=='__main__':
    
    p1=Product('pro1', 800)
    print(p1.show_price())          # AttributeError: 'Product' object has no attribute 'show_price'
    print(p1.price)                 # AttributeError: 'Product' object has no attribute 'price'
    print(vars(p1))                 # {'name': 'pro1', '_Product_price': 800}
    print(p1._Product_price)        # 800
    p1._Product_price = 900         # changing value of a protected attribute
    print(p1._Product_price)        # 900 -> value changed
    print(p1._show_price())         # Price: 800   -  no need to type Class name for protected class.
#______________________________________________________________________________________________________

# کلاس فرزند هم به راحتی به protected attribute که در کلاس والد هست دسترسی داره
class Child(Product):
    def show_price(self):
        print(self.price)

obj=Child("name1",200)
print(obj._price)    #200






#=======================================
'''  2- Private attribute | method  '''
#=======================================

# در پروژه های واقعی در مواردی مثل موجودی حساب، رمز عبور، توکن‌ها و اطلاعات داخلی کلاس از مقادیر private استفاده میشه
# مقادیر private نه از داخل child و نه در main بهش دسترسی وجود نداره

# با استفاده از 2 عدد underline مقدار یک متغیر private میشه
# اینم مثل protected غیرقابل دسترسی نیست
# ولی پایتون با استفاده از ویژگی name mangling دسترسی بهش رو کمی سخت تر میکنه
# مثلا در این کلاس نمیشه مثلا protected با underline به متغیر دسترسی پیدا کنیم
# چون ویژگی name mangling میاد اسم متغیر private رو تغییر میده که نشه با __ بهش دسترسی پیدا کرد
# self.__age  =>  self._Person__age

class Person:
    def __init__(self, age):
        self.__age = age

p=Person(20)
print(p.__age)   #AttributeError 
print(p._Person__age)    #20   name mangling
#___________________________________________



class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price           #private attribute
    
    def __show_price(self):            #private method
        return f" Price: {self.__price}"
    

if __name__=='__main__':
    
    p1=Product('pro1', 800)
    print(p1.show_price())             # Price: 800
    print(p1.price)                    # AttributeError: 'Product' object has no attribute 'price'
    print(vars(p1))                    # {'name': 'pro1', '_Product__price': 800}
    print(p1._Product__price)          # 800
    p1._Product__price = 900           # changing value of a private attribute
    print(p1._Product__price)          # 900 -> value changed
    print(p1._Product__show_price())   # Price: 800
#______________________________________________________________________________







#=====================================
'''  1- Public attribute | method  '''
#=====================================

class Person:
    def __init__(self):
        self.name = "Ali"

p = Person()
print(p.name)    #Ali
#______________________________________________________________________________







#====================
'''   Summary    '''
#====================

#____________________________________________________________
#    Access    |   Class   |   Child   |   Outside  |  main  |
#______________|___________|___________|____________|________|
#    Public    |     ✔    |     ✔    |     ✔      |   ✔   |
#______________|___________|___________|____________|________|
#   Protected  |     ✔    |     ✔    |     ✔**    |   ✔   |
#______________|___________|___________|____________|________|
#    Private   |     ✔    |   ✔**    |   ✔**      |  ✔**  |
#______________|___________|___________|____________|________|


# ✔**:
    # چون در پایتون private یا protected واقعی وجود ندارد
    # و با اینکه طبق قرارداد اینکار ممنوعه ولی همچنان میشه با روشهایی به این levelها دسترسی پیدا کرد













'''
=============================
=============================
======     Abstract    ======
=============================
=============================
'''

# کلاس های Abstract کلاس های انتزاعی هستند و وجود خارجی ندارن
# یعنی نمیشه ازشون instance بسازیم که این ویژگی جهت امنیت پروژه کاربرد داره

# برای اینکه متودهای یک کلاس abstract بشه اول نیازه که خود کلاس abstract بشه
# وقتی کلاس abstract شد میتونیم از یک دکوراتور بنام @abstractmethod استفاده کنیم تا متودها رو abstract کنیم

# بعد از abstract شدن یک کلاس، دیگه نمیشه از متودهای abstract که داخلش هستن استفاده کرد
# البته از متودهای دیگه که داخلش هستن و abstract نیستن مثل __init__ یا __str__ میشه استفاده کرد


# در این مثال کلاس Product کاربردی جز مدیریت کردن بقیه کلاسهای فرزند نداره
# ما محصولی بنام Product نداریم، بنابراین برای کنترل برنامه خودمون این کلاس رو تبدیل به abstract میکنیم
# با اینکار دیگه اجازه نمیدیم آبجکتی از این کلاس ایجاد بشه
# یک کلاس abstract میتونه بدون مشکل به فرزند هاش ارث بری کنه
# یعنی یک متد abstract از کلاس Product میتونه بره توی کلاس فرزند
# سپس اونجا overview میشه و میتونیم حالا از کلاس فرزند یک instance بسازیم و ازین متود استفاده کنیم


from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name, price):
        self.name=name
        self.price=price
    
    def __str__(self):
        return f"Name: {self.name} - Price: {self.price}"
    
    @abstractmethod                    
    def discribe_product(self):
        pass
   
p1=Product('p', 100)
print(p1.discribe_product())      #TypeError: Can't instantiate abstract class Product without an implementation for abstract method 'discribe_product'
#______________________________________________________________________________


# ما محصولی بنام Book داریم، بنابراین لازمه که ازین کلاس بتونیم آبجکت بسازیم
# این کلاس یک متد مشابه کلاس والد خودش یعنی Product داره، که توی کلاس والد این متد Abstract شده
# ولی ازونجایی که این متد در کلاس book دوباره overwrite شده، بنابراین اینجا Abstract نیست و میشه ازش آبجکت ساخت

class Book(Product):
    def __init__(self, name, price, author):
        super().__init__(name, price) 
        self.author=author
    
    def __str__(self):
        return f" {super().__str__()} - author: {self.author}"
                
    def discribe_product(self):
        print(f'this is a book by {self.author}')


b=Book('book', 100, 'author1')
print(b)                         #Name: book - Price: 100 - author: author1
print(b.discribe_product())      #this is a book by author1
#______________________________________________________________________________












'''
=============================================================
=============================================================
======                    Attributes:                  ======
======     1-instance attribute   2-class attribute    ======
=============================================================
=============================================================
'''

# ما کلا داخل __init__ مقادیر مختلفی بنام attribute تعریف میکنیم که 2 گروه میشن:
    # instance attribute
    # class attribute


#__________________________________ [instance attribute]  ______________________________________________

# به att هایی که داخل __init__ یا سایر متدهای کلاس تعریف میشن و اولشون Self دارن میگن instance att
# یعنی att هایی که ما از طریق instance که ساختیم (self) بهشون دسترسی داریم

class Student:
    def __init__(self, name, stu_num, score):
        self.name = name            #instance att
        self.stu_num = stu_num      #instance att
        self.score = score          #instance att
    
    def __str__(self):
        return f"name: {self.name} - stu_number: {self.stu_num} - score: {self.score}"
    
    def calc_avg(self):
        result = sum(self.score)/len(self.score)
        self.avg = result      #instance att


s = Student('reza', '2245', [18,15])
print(s.name)       #reza
print(s.score)      #[18, 15]
print(s)            #name: reza - stu_number: 2245 - score: [18, 15]
print(vars(s))      #{'name': 'reza', 'stu_num': '2245', 'score': [18, 15]}
s.calc_avg()
print(s.avg)        #16.5




#__________________________________ [class attribute]  ______________________________________________

# ولی class att کاملا مربوط به class ما میشه نه instance و هیچ ارتباطی با self نداره
# مثلا چندتا نمونه از کلاس Student ساختیم و میخوایم یک att تعریف کنیم که تعداد نمونه‌هایی که از کلاس ما ایجاد شده رو حساب کنه
# لازمه که همچین att فقط وابسته به کلاس باشه (نه متودها) تا از طریق کلاس بتونیم به تعداد نمونه ها برسیم

# برای تعریف class att میایم میذاریمش قبل از __init__ و یک مقدار اولیه هم بهش میدیم
# یک class att بنام num_of_student ساختیم، و انتهای __ini__ میگیم هروقت یک instance تولید شد یکی بهش اضافه کن
# دسترسی به class att هم از طریق اسم کلاس و هم از طریق اسم instance امکان پذیره


class Student:
    num_of_student=0     #class att
    def __init__(self, name, score):
        self.name = name
        self.score = score
        Student.num_of_student+=1    # increase class att
    
    def __str__(self):
        return f"name: {self.name} - score: {self.score}"


s = Student('reza', [18,15])
s2 = Student('ali',[15,20,13])
s3 = Student('mohammad', [10,18,13])
print(Student.num_of_student)    # 3     دسترسی از طریق کلاس
print(s.num_of_student)          # 3     دسترسی از طریق نمونه












'''
==============================================================================
==============================================================================
======                             Decorators:                          ======
======         1-@instancemethod   2-@classmethod   3-@staticmethod     ======
==============================================================================
==============================================================================
'''


# دکوراتورها یکی از ویژگی های پایتون هستن که برای تغییر رفتار یک متود در داخل یک کلاس استفاده میشن
# این دکوراتورها درواقع خودشون توابع از قبل آماده‌ای هستن که هر کدوم برای کاری ساخته شدن

# وقتی میگیم:
@classmethod
def func():
    pass

# درواقع پایتون در پشت صحنه تابع رو میگیره و تبدیل به یک class method میکنه:
func = classmethod(func)



# دکوراتورها بهمون اجازه میدن بدون اینکه در متود اصلی تغییری ایجاد کنیم:
    # لاگ بگیریم    
    # امنیت اضافه کنیم    
    # زمان اجرا رو اندازه گیری کنیم    
    # اعتبارسنجی انجام بدیم    
    



# creating a decorator
def my_decorator(func):
    def wrapper():
        print('before using function')
        func()
        print('after using function')
    return wrapper


# a simple function without any decorator
def hello():
    print('hello')   # hello


# decorator adds something to the same function
@my_decorator
def hello():
    print('hello')

# before using dunction
# hello
# after using function
#_______________________________________________________________________________




class Student:
    
    num_of_student=0
    
    def __init__(self, name, stu_num, score):
        #instance attribute
        self.name = name
        self.is_valid(stu_num)   # قبل از درست شدن متغیر،این تابع رو گذاشتیم که معتبر بودنش رو اول بررسی کنه
        self.stu_num = stu_num
        self.score = score        
        Student.num_of_student+=1      #class attribute
    
    def __str__(self):
        return f"name: {self.name} - stu_num: {self.stu_num} - score: {self.score}"
    
    def calc_avg(self):
        result = sum(self.score)/len(self.score)
        self.avg = result
        
    
    @classmethod 
    def show_instance_number(cls):
        # this func shows amount of instances
        print(cls.num_of_student)
        
    
    @staticmethod
    def is_valid(stu_num):
        # this function validates student_number
        if stu_num!=4 or not stu_num.startwith('s'):
            raise ValueError("Error! Student Number is not valid, instance can't be made.")
        


# ______________ [ instance متدهای] _________________

# تمام متودهایی که تاحالا باهاش کار کردیم instance method بودن که همشون self میگرفتن و به instance وابسته بودن
# برای دسترسی به instance method ها از نمونه خودمون استفاده میکنیم



# ______________ [ @classmethod دکوراتور] _________________

# حالا class method ها مربوط به کلاس هستند و با class att ها کار میکنن. به عنوان ورودی cls میگیرن
# با cls میتونیم با dot notaion به class att ها دسترسی داشته باشیم
# برای اینکه یک متود تبدیل به کلاس متود بشه قبلش  @classmethod میذاریم
# متودی که تبدیل به classmethod میشه روی کل کلاس عملیات انجام میده نه روی نمونه
# برای اینکه هر متد تبدیل به classmethod بشه باید برای هر کدوم جداجدا از دکوراتور @classmethod استفاده کنیم



# ______________ [ @staticmethod دکوراتور] _________________

# کاربردشون تو گذاشتن validation روی یک سری مقادیر هست
# این validation ها باید قبل از ایجاد instance اعمال بشن
# برای صدازدن staticmethod ها از self استفاده میکنیم




#___________________________________________________

s1=Student('n1', 's123', [14,17,20])
s2=Student('n2', 's345', [14,17,20])

#testing @staticmethod
try:
    s3=Student('n3', 'sh123', [14,17,20])
except Exception as e:
    print(e)    # ValueError: Error! Student Number is not valid, instance can't be made.

s1.calc_avg()                  # instance method
s1.avg                         # instance attribute
Student.show_instance_number()    # class method
s1.show_instance_number()
Student.num_of_student         # class attribute



















'''
==============================================================================
==============================================================================
======                      types of Methods in a class:                ======
======     1-instance attribute   2-class attribute   3-static method   ======
==============================================================================
==============================================================================
'''


# در یک کلاس 3 نوع متود وجود داره:
    # Class method       cls دسترسی به
    # Instance method    self دسترسی به
    # Static methods     None دسترسی به


'''======= instance method ======='''
# این همون متد عادی هست که استفاده میکنیم و Self میگیره
# کلا self همون instance هست که از کلاس ایجاد میکنیم (self=p)
# بنابراین این نوع متود به اطلاعات instance دسترسی داره

# در پایتون هر متود در ابتدا instance method است و نیازی به هیچ دکوراتور نداره که تبدیل بشه
# پس عملا دکوراتوری بنام @instancemethod نداریم

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}")
    
p=Person("ali")
p.introduce()     #instance method



'''======= class method ======='''
# گاهی می‌خواهیم به خود کلاس دسترسی داشته باشیم نه به شیء
# برای اینکه یک متود تبدیل به class method بشه از یک دکوراتور بنام @classmethod استفاده میشه
# همچنین از یک class attribute باید استفاده بشه
# این نوع متودها با کلاس ارتباط دارن و بجای self از cls استفاده میکنن
# این cls همون کلاس ما هست (cls=Person)

class Person:
    country = "Germany"

    @classmethod
    def show_country(cls):
        print(cls.country)

Person.show_country()   #Germany     class method


# یکی دیگه از کاربردهای class method ها برای ساخت شیء هست
# به این نوع متودها Alternative Constructor هم میگن
class Person:

    def __init__(self, name):
        self.name = name

    @classmethod
    def create_unknown(cls):
        return cls("Unknown")

p = Person.create_unknown()    #creating object
print(p.name)    #unknown



'''======= static method ======='''
# گاهی یک تابع به کلاس مربوط هست اما نه self میگیره نه cls میگیره
# در واقع Static Method فقط برای مرتب‌سازی کد داخل کلاس قرار گرفته است
# برای ساختن این نوع متودها از یک دکوراتور بنام @staticmethod استفاده میشه

class Math:
    @staticmethod
    def add(a, b):
        return a + b
    
Math.add(2, 3)   #5




'''======= Summary ========'''
# _________________________________________________________________
# | دسترسی به کلاس | دسترسی به شیء  | self | cls  |  نوع متد     |  
# |---------------|-------|-----|-----------------|----------------|
# |    Instance   | ✔    | ✘  |       ✔        |       ✔       |
# |     Class     | ✘    | ✔  |       ✘        |       ✔       |
# |     Static    | ✘    | ✘  |       ✘        |       ✘       |

# در این مثال نهایی، همه نوع متودها وجود دارن
class Employee:

    company = "Google"

    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(self.name)

    @classmethod
    def show_company(cls):
        print(cls.company)

    @staticmethod
    def is_adult(age):
        return age >= 18
#-----------------------
emp = Employee("Ali")

emp.show_name()              # Instance Method

Employee.show_company()      # Class Method

Employee.is_adult(20)        # Static Method




















'''
==============================================================================
==============================================================================
======                 Property:  getter, setter, deleter               ======
==============================================================================
==============================================================================
'''
# درواقع property هم یک Decorator است که رفتار یک متد را تغییر می‌دهد
# کاربرد property اینجاست که در کلاس زیر، کاربر میتونه هر مقداری که خواست به age بده
# اینجوری دیگه هیچ کنترلی روی age نداریم
class Person:
    def __init__(self, age):
        self.age = age

p = Person(25)
print(p.age)    #25
p.age= 30
p.age= -100
p.age= "abc"


# در زبان هایی مثل java از روشی قدیمی (getter و setter و deleter) استفاده میشه برای این مسئله:

#_________________________[getter | setter]____________________________________

# تعریف: getter روشی برای خواندن مقدار
# تعریف: setter روشی برای تغییر مقدار با کنترل است

class Person:
    
    def __init__(self, age):
        self._age = age
    
    def get_age(self):     #getter
        return self._age
    
    def set_age(self, value):      #setter
        if value < 0:
            print('Age cannot be negative')
        else:
            self._age = value
#------------------------
p = Person(20)
print(p.get_age())   #20
print(p.set_age(30))  #30

# نتیجه:  با p.set_age و p.get_age کدهای ما زشت میشن
# پایتون برای حل این مشکل @property رو معرفی کرده
# این property اجازه میده از ظاهر ساده‌ی Attribute استفاده کنیم ولی پشت صحنه متد اجرا بشه



#______________________ [property decorator] _________________________

# با این دکوراتور یک متد را مثل یک متغیر(attribute) استفاده میکنیم
 # درواقع property میاد getter | setter | deleter رو تبدیل میکنه به Attribute

class Person:
    def __init__(self, age):
        self.age = age
    
    @property 
    def age(self):
        return self.age
    
    @age.setter 
    def age(self, value):
        if value < 0:
            print('Age cannot be negative!')
        else:
            self.age = value
            
    @age.deleter
    def age(self):
        del self.age
#-----------------------------
p = Person(20)
print(p.age)     #20   getter
p.age = 30       # setter
print(p.age)     #30     اول 20 بود و ما مقدار جدیدی براش ست کردیم
p.age = -5
print(p.age)     #Age cannot be negative!
del p._age       # deleter
print(p.age)     # AttributeError: 'Person' object has no attribute '_age'






'''========  create a decorator  ========='''   
  
# گاهی لازمه خود دکوراتور هم تنظیماتی داشته باشه
# مثلا میخوایم زمان اجرای یک تابع رو اندازه بگیره
# میایم یک دکوراتور بنام timer درست میکنیم که اینکار رو برامون انجام بده

import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        
        print('Execution time: ', end - start)
    return wrapper


@timer
def task():
    time.sleep(2)
    print(' Task done')

task()     
# Task done
#Execution time:  2.0005929470062256




# حالا میخوایم یک دکوراتور بسازیم که چندبار اجرا بشه
# پس دکوراتور باید یک لایه بیشتر داشته باشد
#دکوراتور با پارامتر همیشه 3 لایه دارد:
    # decorator
       # ↓
    # wrapper decorator
       # ↓
    # wrapper function

def repeat(times):
    def decorator(func):
        def wrapper():
            for i in range(times):
                func()
        return wrapper
    return decorator    


@repeat(3)
def hello():
    print('hi')

hello()
# hi
# hi
# hi




# حالا میخوایم یک دکوراتور بسازیم که کلاس رو تغییر بده:
# مثلا وقتی میخوایم یک object ساخته میشه پیام چاپ بشه.

def add_message(cls):
    class NewClass(cls):
        def __init__(self, *args, **kwargs):
            print("Object created")
            super().__init__(*args, **kwargs)
    return NewClass


@add_message
class Person:
    def __init__(self, name):
        self.name = name

p = Person('Ali')      # Object created



























        
        
        
        
        
        
        
        
        




















