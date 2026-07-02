
"""
        ====================================================================
        ===========      Created on Mon Jun 29 22:41:08 2026     ===========
        ===========         Author: Khashayar Alipour            ===========
        ===========                IDE: spyder                   ===========
        ===========        python Database (SQLalchemy)          ===========
        ====================================================================
"""

# در این درسنامه، با استفاده از کتابخوانه sqlalchemy یک دیتابیس راه‌اندازی میشه


# SQLite
# ORM
# SQLalchemy








'''
============================
======     SQLite     ======
============================
'''

# کتابخوانه SQLite چیه؟ ساده‌ترین دیتابیس دنیاست
# برخلاف MySQL و PostgreSQL، هیچ سروری نداره و فقط یک فایل روی کامپیوترت می‌سازه
# خود پایتون بصورت پیش‌فرض این کتابخونه رو داره

# تمام دستوراتی که در ادامه وجود داره، پشت صحنه توسط کتابخوانه SQLalchemy اجرا میشه

#=============[ initiate db ]=============
import sqlite3
conn = sqlite3.connect("shop.db")      # یک دیتابیس به این نام (اگر وجود نداشته باشه) ساخته شد و بهش وصل میشه
# اینجا conn مخفف connection هست که تا اتصالی تباشه نمیتونی هیچی بخونی یا بنویسی
# همین فایل، کل دیتابیس توست و اگر پاکش کنی، دیتابیس هم پاک میشه
# داخل این فایل همه چیز داخل جدول و row و column ذخیره شده


#==============[ cursor ]===============
# حالا این connection مستقیم کار خوندن یا نوشتن رو انجام نمیده بلکه یه واسطه بنام cursor داره که دستور رو اجرا میکنه
cursor = conn.cursor()


#==============[ creating table ]================
# یک جدول به اسم students میسازه
cursor.execute("""
CREATE TABLE students(
    id INTEGER,
    name TEXT,
    age INTEGER
)
""")

conn.commit()    # save table


#============[ adding data to table ]====================
cursor.execute("""
INSERT INTO students
VALUES(1, 'Ali', 20)
""")
conn.commit()
#--------------------
cursor.execute("""
INSERT INTO students
VALUES(2, 'Sara', 22)
""")
conn.commit()


# | id | name | age |
# | -- | ---- | --- |
# | 1  | Ali  | 20  |
# | 2  | Sara | 22  |


#==============[ reading data from table ]===============
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
print(rows)
[ (1, 'Ali', 20), (2, 'Sara', 22) ]   # کلا این کتابخوانه داده هارو بصورت تاپل برمیگردونه


#=============[ closing table ]====================
# همیشه در پایان وقتی کارمون تموم شد باید table رو ببندیم
conn.close()     # close table (at the end)










'''
=========================
======     ORM     ======
=========================
'''
# Object Relational Mapper

# کلا ORM یک ابزاری هست که بوسیه اون میتونیم object های پایتونی رو به جدول های DB تبدیل کنیم
# یعنی به زبان پایتونی مینویسیم و در دیتابیس جدول ها تشکیل میشن
# این ORM مخصوص پایتون نیست و سایر زبانهای برنامه نویسی هم ازش استفاده میکنن

# این ORM میاد object های پایتونی رو به record و کلاس های پایتونی رو به table در دیتابیس تبدیل میکنه
# دیگه لازم نیست با دستورات MySQL کار کنی

# Python
#  ↓
# ORM
#  ↓
# SQL
#  ↓
# SQLite


#Python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

ali = Student("Ali",20)


#ORM    
#       Student
# | id | name | age |
# | -- | ---- | --- |
# | 1  | Ali  | 20  |


# Python               SQLite
# ____________________________________
# Class Student  --->  Table students
# Object ali     --->  Row
# name           --->  Column name
# age            --->  Column age














'''
===============================================
======     Introduction of SQLalchemy    ======
===============================================
'''

# کتابخونه SQLalchemy میاد هر کلاس پایتونی رو به جدول در دیتابیس و هر object رو به یک record در این جدول تبدیل میکنه
# چطوری این تبدیل رو انجام میده؟ به کمک ORM

# Python Objects  (OOP)
#       │
#       ▼
# SQLAlchemy ORM
#       │
#       ▼
# SQLite Database


# این کلاس توی پایتون نوشته میشه
class User:  #class=table
    pass
u=User("Ali")   #object=row

# اینا توسط sqlalchemy ساخته میشه

#      User table
#   _____________
#   | id | name |
#   |-----------|
#   | 1  | Ali  |
#   |____|______|



# مهمترین اجزای SQLalchemy اینا میشن:
    # Engine تعریف
      # ↓
    # Base تعریف
      # ↓
    # Model(Class) تعریف
      # ↓
    # create_all()
    # Column ساخت
      # ↓
    # Session ساخت
      # ↓
    # Object ساخت
      #↓
    # session.add()
    # session.commit()
    # Database


# در مقایسه OOP با SQLalchemy به این جدول میرسیم:
# _________________________________
# | OOP             | SQLAlchemy  |
# | --------------- | ----------- |
# | Class           | Table       |
# | Object          | Row         |
# | Attribute       | Column      |
# | Constructor     | ساخت رکورد  |
# | List of Objects | نتیجه Query |




#===============
''' engine  '''
#===============

# این engine پل ارتباطی برنامه با دیتابیس هست

# engine = create_engine("sqlite:///shop.db")
# این خط فایل shop.db را باز می‌کند و اگر وجود نداشته باشد، می‌سازد و آمادهٔ ارتباط می‌شود

# Program
#    │
# Engine
#    │
# SQLite



#============
''' Base  '''
#============

# Base = declarative_base()
# این خط یعنی از این به بعد هر کلاسی که از Base ارث ببرد، تبدیل به جدول می‌شود

# مثلا در پایتون این کلاس رو داریم:
class User(Base):
    pass

# ولی SQLalcheny میفهمه که این یک جدوله



#=============
''' Model  '''
#=============
# این model یعنی همون کلاس پایتونی

class User(Base):   # Table User
    pass



#=============
''' Column  '''
#=============
# هر ویژگی کلاس، یک ستون از جدول هست
# مثلا در یک کلاس این id و name رو داریم:
id = Column(Integer, primary_key=True)
name = Column(String)

# در جدول user:
#    ___________________
#    | id | name | ...
#    |----|------|------
#     ...   ...



#================
''' session  '''
#================
# اینجا Session مهم‌ترین قسمت SQLAlchemy است و مثل یک دفتر یادداشت تغییرات است

# Object
#   ↓
# Session
#   ↓
# Commit
#   ↓
# Database

user = User(name="Ali")
session.add(user)
# چیزی داخل دیتابیس ذخیره نشده هنوز، ولی session میدونه که قراره تغییری رخ بده و یک object ذخیره بشه

session.commit()
# با این خط دیگه دیتا ذخیره میشه



#================
''' add()  '''
#================
session.add(user)
# این خط یعنی object رو آماده ذخیره کن



#================
''' commit()  '''
#================
session.commit()
# یعنی همه تغییرات رو دائمی کن



#==================
''' rollback()  '''
#==================
# اگر قبل از commit کردن مشکلی پیش بیاد با این دستور تمام تغییرات لغو میشه
session.rollback()



#===============
'''  Query  '''
#===============
session.query(User)
# الان اینجا ساخته میشه ولی بعدا برای خواندن اطلاعات استفاده میشه



#==================
'''  Relation  '''
#==================
# فرض کنیم یک user چند سفارش (order) داده
# هم جدول user میخوایم هم جدول order
class User(Base):
    pass
class Order(Base):
    pass

# این دوتا جدول باید بهم وصل بشن
# اینکار با استفاده از 2 چیز انجام میشه
ForeignKey()
relationship()



#===================
'''  Foreignkey  '''
#===================
# این ستون به جدول user متصل هست
user_id = Column(ForeignKey("users.id"))



#=======================
'''  Relationship()  '''
#=======================
# بدون relationship باید خط زیر رو بنویسی و دوباره بری دنبال کاربر و پیداش کنی
order.user_id

# ولی با relationship() فقط خط زیر رو مینویسی و مستقیم شیء user رو میگیری
order.user

# تفاوت FK با relationship اینه که FK داخل دیتابیس وجود داره ولی relationship فقط توی پایتون وجود داره



#=================
'''  database  '''
#=================
# تقریبا آخر برنامه همیشه این خط نوشته میشه:
Base.metadata.create_all(engine)
# این خط یعنی تمام کلاس‌هایی که از Base ساخته شده‌اند را به جدول تبدیل کن اگر وجود نداشته باشند، بساز




#====================================
''' creating a db with SQLalchemy '''
#====================================

# کل پروسه در 6 مرحله کلی انجام میشه:
# کتابخانه‌ها را وارد می‌کند
#         ↓
# به SQLite وصل می‌شود
#         ↓
# یک کلاس (Model) تعریف می‌کند
#         ↓
# از روی آن کلاس، جدول می‌سازد
#         ↓
# یک Session می‌سازد
#         ↓
# عملیات CRUD را انجام می‌دهد


from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String


# موتور اتصال ما به دیتابیس میشه این engine که ساختیم
# اسم دیتابیس خودمون اینجا مشخص کردیم test.db باشه
# دیتابیس بصورت پیشفرض گذاشتیم sqlite باشه
# وقتی echo روی True میذاریم میاد اتفاقاتی که در پشت صحنه میوفته رو بهمون میگه
# درواقع echo فقط اموزشی هست و هر SQLای که SQLAlchemy پشت صحنه اجرا کند را در ترمینال چاپ می‌کند (INSERT INTO users ...)
engine = create_engine('sqlite:///test.db', echo=True)


# تمام مدلهایی که تعریف میکنیم باید از متغیر base ارث بری کنن.
# وقتی Base اجرا میشه، یک کلاس به اسم Base میسازه
# این کلاس در SQLalchemy طوری ساخته شده که که بتونه کلاسهای فرزندش رو به جدول تبدیل کنه
Base = declarative_base()


# اینجا bind مشخص میکنه که ما قراره به کدوم engine و کدوم دیتابیس وصل بشیم.
# با استفاده از تابع sessionmaker یک session میسازیم (ممکنه در طول برنامه هزاران session ساخته بشه)
Session = sessionmaker(bind=engine)


# اینجا میایم از کلاس Session یک نمونه میسازیم.
# اینکار میاد تمام ارتباطات برنامه با دیتابیس مدیریت میکنه.
# مثلا: اضافه کردن یا حذف یک ردیف - تغییر داده ها و نگه داشتن تغییرات در حافظه
# تمام مثالهای بالا تا زمانیکه ما دستور commit رو بزنیم در حافظه میمونن.
# دستور commit میاد تغییرات رو ذخیره میکنه در جدول های ما.
# تا زمانیکه تغییرات در جدول های ما ذخیره نشدن، مدیریت و نگهداری ازشون با متغیر session هست.
session = Session()


# این کلاس قراره جدول ما بشه چون از Base ارث بری کرده.
# جداول همون کلاس های ما در کدنویسی هستند.
# با دستوراتی که داخل کلاسها مینویسیم تبدیلشون میکنیم به جدول.
# هر کلاسی که قراره به جدول تبدیل بشه باید از Base ارث بری کنه.
class User(Base):
    __tablename__='users'   # این داندرمتود اسم جدول رو مشخص میکنه
    
    # در این جدول 3 تا ستون داریم که جنسشون یا int هست یا str هست     
    # با استفاده از متود Column که از SQLalchemy.orm آوردیمش میتونیم attribute های کلاس رو تبدیل به ستون کنیم    
   # همچنین با استفاده از متود Integer یا String میتونیم تایپ هر ستون رو مشخص کنیم    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    
    # داندر متود representation مثل __str__ هست با این تفاوت که پیامی برای developerها نمایش میده    
    def __repr__(self):
        return f"<User(name: {self.name}, email: {self.email})>"


# این خط میاد مدلهایی که برای دیتابیس تعریف کردیم به جدول تبدیل میکنه تا عملیات CRUD روش انجام بدیم
# CRUD = Create - Read - Update - Delete
# درواقع Base مسئول ثبت تمام مدل(کلاس) هایی هست که ازش ارث بری میکنن
# اینجا metadata یک object هست که مسئول ذخیره اطلاعات جدولهایی است که داخل Base ساخته میشه
# متد create_all کارش بررسی همه جدولهای ثبت شده داخل metadata و ایجاد کردن اونها داخل DB هست
Base.metadata.create_all(engine)





''''''''''''''''''''''''''''''''''''
# تا اینجای کار اینو ساختیم:

#create file:  test.db
    
#       users
# | id | name | email |
# | -- | ---- | ----  |

''''''''''''''''''''''''''''''''''''
    



# __________ CRUD ___________

# 1-Create
# اینجا دیگه id به عنوان ورودی نمیدیم. چون pk هستش و خودش بصورت automatic increment اعداد رو بصورت 1 2 3 ... وارد میکنه
new_user = User(name="Ali", email="ali@gmail.com")
new_user2 = User(name="Sara", email="sara@gmail.com")
new_user3 = User(name="Ahmad", email="ahmad@gmail.com")

session.add(new_user)
session.add(new_user2)
session.add(new_user3)
session.commit()    # Insert = ذخیره تغییرات

# تا اینجای برنامه رو اگه اجرا کنیم یه فایل دیتابیس با اسم test.db میسازه
# داخل این فایل یک جدول با نام users هست که 3 تا ستون داره و 3 تا ردیف هم داره



''''''''''''''''''''''''''''''''''''
# تا اینجای کار اینو ساختیم:

#create file:  test.db
    
#       users
# | id | name  | email           |
# |----|-------|-----------------|
# | 1  | Ali   | ali@gmail.com   |
# | 2  | Sara  | sara@gmail.com  |
# | 3  | Ahmad | ahmad@gmail.com |

''''''''''''''''''''''''''''''''''''



# 2-Read

# این خط یعنی یک query بزن روی جدولی که از کلاس User ساخته شده(users) و همه (all()) ردیف هاشو بگیر و بریز توی متغیر users
# متغیر users لیستی از تمام object هایی خواهد بود که با کمک کلاس User ساختیم
# یعنی شیء هایی که از کلاس User ساخته شده
users = session.query(User).all()
print(type(users))    # <class '__main__.User'>

for user in users:
    print(user)     # print(user) = print(user.__repr__())

# [
# <User(name: Ali, email: ali@gmail.com)>
# <User(name: Sara, email: sara@gmail.com)>
# <User(name: Ahmad, email: ahmad@gmail.com)>
# ]




# 3-Update

# میخوایم فقط یک ردیف رو آپدیت کنیم
# برای اینکه فقط یک ردیف رو از بقیه ردیفها جدا کنیم از تابع filter_by استفاده میکنیم
# پارامتری که میخوایم بر اساسش اون ردیف رو فیلتر کنیم به این تابع میدیم
# اینجا first() یعنی اولین مقداری رو که دیدی اسمش برابر 'Ali' بود برام برگردون و بریز توی متغیر user
# حالا تو خط بعدی میگیم وقتی به اولین ردیفی که اسمش برابر علی هست دسترسی پیدا کردی ایمیلش رو به فلان چیز تغییر بده

user = session.query(User).filter_by(name="Ali").first()
user.email = "new_ali@gmail.com"
session.commit()



''''''''''''''''''''''''''''''''''''
# تا اینجای کار اینو ساختیم:

#create file:  test.db
    
#       users
# | id | name  |       email       |
# |----|-------|-------------------|
# | 1  | Ali   | new_ali@gmail.com |
# | 2  | Sara  | sara@gmail.com    |
# | 3  | Ahmad | ahmad@gmail.com   |

''''''''''''''''''''''''''''''''''''



# 4-Delete

user = session.query(User).filter_by(name="Ahmad").first()
session.delete(user)
session.commit()


''''''''''''''''''''''''''''''''''''
# تا اینجای کار اینو ساختیم:

#create file:  test.db
    
#       users
# | id | name  |       email       |
# |----|-------|-------------------|
# | 1  | Ali   | new_ali@gmail.com |
# | 2  | Sara  | sara@gmail.com    |

''''''''''''''''''''''''''''''''''''











''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# کار sqlalchemy.text چیه که اول برنامه import کردیم؟

# اینجا text کارش ساختن query های متنی هست
# در واقع تابع text زمانی استفاده می‌شود که بخواهی خودت یک دستور SQL خام (Raw SQL) بنویسی و آن را از طریق SQLAlchemy اجرا کنی

# مثلاً اگر بخواهی تمام کاربران را بخوانی، به جای:
    users = session.query(User).all()
# می‌توانی SQL خام بنویسی:
    session.execute(text("SELECT * FROM users"))
    for row in result:
        print(row)
    # (1, 'Ali', 'ali@gmail.com')
    # (2, 'Sara', 'sara@gmail.com')
    # (3, 'Ahmad', 'ahmad@gmail.com')

# متود text کاربردهای مختلفی داره و در کل وقتی ORM داریم معمولا از text استفاده نمیشه
# معمولاً در موارد زیر text استفاده میشه:
# یک Query خیلی پیچیده داری    
# یا SQL خاصی می‌خواهی که ORM به‌راحتی نمی‌تواند بنویسد    
# یا داری یک دیتابیس قدیمی را مدیریت می‌کنی    
''''''''''''''''''''''''''''''''''''''''''''''''''''''''







