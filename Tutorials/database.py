
"""
        ====================================================================
        ===========      Created on Sun Jun 28 21:01:36 2026     ===========
        ===========         Author: Khashayar Alipour            ===========
        ===========                IDE: spyder                   ===========
        ===========          python Database (MySQL)             ===========
        ====================================================================
"""



# Database basics
# MySQL 




# در این فایل کلیات راه اندازی دیتابیس با استفاده از MySQL با ذکر یک مثال بررسی میشه

# مسئله: ایجاد db برای مدیریت عکس‌ها
# میخوایم جدول های دیتابیس رو طوری درست کنیم که بفهمیم کدوم user از کدوم category، کدوم image رو میخواد داخل سایت ما قرار بده







'''
==============================
=====    Introduction    =====
==============================
'''
# هر برنامه 3 بخش داره     
#       /       |         \
#    Front    backend    database


# بطور کلی 2 مدل دیتابیس داریم:
    # 1- sqlbase (structured quert language) or relational database
    # 2- nosql -> جدیدتر و کاربرد کمتر

# relational DB:
    # جدول های دیتابیس با رابط هایی بهم وصل هستن    
    # به این نوع دیتابیس‌ها میگن sql base    
#  # به زبان کدنویسی مخصوص دیتابیس های relational میگن SQL    

# انواع relation بین جدولها در relational DB:
    # one to one   مثلا یک استاد دانشگاه فقط اجازه داره یک درس ارائه بده
    # one to many   یک استاد اجازه داره چند درس ارائه بده
    # در رابطه های one to many اون جدولی که سمت one هست، PK خودش رو به عنوان FK میده به جدولی که سمت many هست                    
    # many to many   یک استاد چند درس ارائه میده-یک درس توسط چند استاد ارائه میشه
# در جداول many to many همیشه جدولها به یک جدول سوم که one to many هست شکسته میشه                     


# primary key:
    # ستون id در جداول که مقدار unique برای هر ردیف داره    
# foreign key:
    # اگر دو جدول باهم مرتبط بشن PK در یک جدول، میشه FK در یک جدول دیگه    


# تعریف query نویسی:
    # یعنی کدنویسی داخل sql ها    
    

# DB concepts:
    # امنیت دیتابیس    
    # DB optimization or tuning
    # DB designing
    # مدیریت سرورهای روی DB    
    

# چک کردن مقادیر داخل دیتابیس:
    # مثلا وقتی یک کاربر جدید داخل سایت ثبت نام میکنه باید مثلا در قسمت ایمیل‌ها بررسی بشه که آدرس ایمیل قبلا ثبت شده یا نه    
    

# Table:
    # هر دیتابیس از بخش های کوچکتری بنام جدول درست شده    
    # هر جدول شامل ردیف یا record و ستون یا field (در AI بهش میگن ویژگی یا feature) است    
    
    
# fetching:
    # پروسه‌ی گرفتن دیتا از داخل جدول های دیتابیس    
    
    
# SQLserver:
    # نرم افزاری برای مدیریت دیتابیس‌ها    










'''
=======================
=====    Table    =====
=======================
'''
# هر جدول از ستونهایی تشکیل شده که ویژگی های مربوط به اون جدول هستند
# هر جدول یک id داره که unique هست و primary key اون جدول به حساب میاد
# وقتی PK یک جدول میره داخل یک جدول دیگه قرار میگیره، بهش میگن foreign key

# در این مثال هر عکس مربوط به یک user هست، همچنین هر عکس یک category داره
# پس میایم جدول user و category رو به جدول image متصل میکنیم



#      PK         user table                      PK   category table
#    ____________________________________       ______________
#    | id | username | password | email |       | id | image |
#    |----------------------------------|       |------------|
#    | .. |    ...   |   ...    |  ...  |       | .. |  ...  | 
#    | .. |    ...   |   ...    |       |       | .. |  ...  |
#    ------------------------------------       --------------
#                  |                                   |
#                  |___________________________________|
#                                    |
#                                    |
#                    PK    FK           FK       image table
#                  ___________________________________________________
#                  | id | User_id | Category_id | title | file | ... |
#                  |-------------------------------------------------|
#                  | .. |   ...   |     ...     |  ...  |  ... | ..  | 
#                  |____|_________|_____________|_______|______|_____|











'''
============================
=====    Path to DB    =====
============================
'''

# کلا برای ساخت دیتابیس یکی از این دو مسیر رو باید رفت
# یا از MySQL استفاده میشه یا از SQLite
# کلاس Database که در ادامه نوشته شده برای مسیری هست که از MySQL استفاده میکنه


# SQLite                                                  MySQL
#   │                                                     |
# sqlite3  (کتابخانه استاندارد پایتون)                  mysql.connector
#   │                                                     |
# SQLAlchemy                                              SQLAlchemy 












'''
========================================
=====    Database class (MySQL)    =====
========================================
'''

# اینجا mysql.connector یک مترجم هست که به پایتون کمک میکنه زبان MySQL رو بفهمه
import mysql.connector     

import os   # to connect with the system

from mysql.connector import Error    # shows all the connecting errors


# Steps:
    # 1- create DB
    # 2- create DB tables
    # 3- queries


# تمام کارهای مربوط به ایجاد DB و تمام query های مربوط به آن داخل کلاس Database مینویسیم.
    # این کلاس که برای ایجاد DB به روش OOP نوشیتم در 80 درصد پروژه‌ها دقیقا همینه و مشابه هست.
    
# این کلاس به ما یه سری اطلاعات درمورد DB میده:
    # 1- چطوری بهش connect بشیم.               
# 2- چطوری host - user - password بگیریم.  
# 3- قراره به کدوم DB وصل بشیم و ...      



class Database:
    
   # بصورت پیشفرض database برابر None گذاشتیم و اینجوری خودش به sql متصل میشه.     
   # اگه به عنوان ورودی یک database وارد کنیم دیگه بجای sql به database وصل میشه.     
    
    def __init__(self, host, user, password, database=None):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None    # چون هنوز به سرور وصل نشدیم مقدار اولیه اینو میذاریم نان
        self.cursor = None        # cursor connects mysql to python
        self.connect()            # این متد رو میذاریم اینجا که با ساختن شیء بطور خودکار اتصال اولیه به کمک متد کانکت با دیتابیس انجام بشه
    
    
#_______________________________________[Connection object]____________________________________________
    # متد connect به سرور MySQL وصل می‌شود و یک Connection Object برمی‌گرداند    
    # اینجا connection نماینده اتصال بین برنامه و دیتابیس است و تمام کارها از طریق آن انجام می‌شود    
# روی این شیء (connection) متدهای زیادی وجود دارد:    
        # connection.cursor()
        # connection.commit()   با این متد تغییرات موقتی ایجاد شده داخل حافظه، قطعی میشه
        # connection.rollback()   اگر در آپدیت، یا اضافه و حذف کردن اشتباهی رخ داده و هنوز کامیت نشده میتونیم یه قدم تغییرات رو برگردونیم عقب
        # connection.close()    اتصال را میبندد تا بیهوده باز نباشد
        # connection.is_connected()   بررسی میکنه آیا هنوز به دیتابیس وصل هستیم یا نه
        # connection.reconnect()    اگر اتصال قطع شده باشه دوباره با این متد وصل میشه
    
    # متد cursor قلمی هست که روی دیتابیس می‌نویسد یا از آن می‌خواند و خودش متود های مختلفی داره:    
        # cursor.execute()       کاربرد در بسیاری موارد مثل ایجاد جدول، حذف، اضافه، خواندن
        # cursor.fetchone()   گرفتن یک سطر از جدول 
        # cursor.fetchall()   گرفتن همه سطرها
        # cursor.fetchmany(5)   مثلا 5 سطر اول رو بده
        
    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.database
                )           
            self.cursor = self.connection.cursor()
            # حالا که اتصال برقرار شده میایم cursor رو به اینصورت میسازیم که دیگه None نباشه.           
        
        except Error as e:    # mysql.connector -> Error
            print(e)
#___________________________________________________________________________________________________



# دستور query برای ساخت DB اینه:  CREATE DATABASE    
# اسم DB میشه name    
# بعدش cursor میاد query که نوشتیم رو execute میکنه.   

    def create_database(self, name):
        try:
            sql = f'CREATE DATABASE IF NOT EXISTS {name}'
            self.cursor.execute(sql)
            
            # حالا که DB ما ساخته شد میایم connect رو از sql میبریم روی DB خودمون.       
            self.connection.database = name    
        
            # حالا اون database که توی init تعریف کرده بودیم مقدارش رو برابر name دیتابیس میذاریم که دیگه None نباشه.       
            self.database = name
            
            print('database created!')
        except Error as e:
            print(e)
#___________________________________________________________________________________________________     
        
    
    # ساختن جدول برای دیتابیس.    
# برای ساخت جدول‌ها باید از query های خیلی طولانی استفاده کنیم و چون اینجا جا نمیشه جای دیگه مینویسیم اینجا اضافه میکنیم.    
    def create_table(self, table_sql):
        try:
            # اینجا جدول هارو توسط cursor میایم execute میکنیم که ایجاد بشن.           
            self.cursor.execute(table_sql)
            print(f"{table_sql} created!")
        except Error as e:
            print(e)
#___________________________________________________________________________________________________


    # کلا queryها دو نوع هستند:    
        # 1- یا خروجی دارن که میریزیم توی یک متغیر              
        # 2- یا فقط یک عملیاتی رو انجام میدن و خروجی ندارن     
    
    def execute_query(self, query, params=None):
        # بعضی از queryها parametr ندارن برای همین مقدار پیشفرض میذاریم None.       
        # پارامترها تاپل هستند و هرکی پارامتر نداشت جاش تاپل خالی میذاریم.       
        try:
            self.cursor.execute(query, params or ())
            
            # هر query که خروجی داشته باشه باید عملیات fetch all با استفاده از واسط cursor روش انجام بشه.           
# اگه with_rows برای یک query مقدارش True بشه ینی اون query خروجی داره.           
            if self.cursor.with_rows:
                self.cursor.fetchall()
        except Error as e:
            print(e)
#___________________________________________________________________________________________________  
    
    # بعضی دستورها برای اینکه نتیجشون دیده بشه نیاز به commit شدن دارن.    
    # این متد میگه connection اصلی رو برای من بیار و روش commit انجام بده.    
    def commit(self):
        self.connection.commit()
#___________________________________________________________________________________________________
    
    # مثل کار کردن با فایلها باید اینجا هم آخرش connection رو ببندیم.    
    def close(self):
        self.connection.close()
#___________________________________________________________________________________________________       








'''
=========================================
=====    Define tables (queries)    =====
=========================================
'''

# keys = اسم جدول
# values = محتویات ستونها
# auto_increment = ینی یکی یکی خودش میره بالا
# جدول users و Category جفتشون FK ندارن و مستقل هستن



tables = {
    'users': """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT,     # primary key
            username VARCHAR(50) NOT NULL,
            password VARCHAR(50) NOT NULL,
            email VARCHAR(100),
            PRIMARY KEY (id)
        )
    """,
    'categories': """
        CREATE TABLE IF NOT EXISTX categories (
            id INT AUTO_INCREMENT,     # primary key
            name VARCHAR(100) NOT NULL,
            PRIMARY KEY (id)
        )
    """,
    'images': """
        CREATE TABLE IF NOT EXISTS images (
            id INT AUTO_INCREMENT,     # primary key
            user_id INT NOT NULL,      # foreign key
            category_id INT,           # foreign key
            title VARCHAR(255) NOT NULL,
            description TEXT,
            file_path VARCHAR(255) NOT NULL,    # images are saved in this path
            PRIMARY KEY (id),
            FOREIGN KEY (user_id) REFERENCES users (id),
            FOREIGN KEY (category_id) REFERENCES categories (id)
        )
    """
}









'''
=========================================
=====    class for every table      =====
=========================================
'''

# User Management
class User:
    def __init__(self, db):
        # با db ما به متدهای کلاس database دسترسی داریم.       
        self.db = db
    
    def register(self, username, password, email):
        # مقادیر داخل ستونهای جدول اینجا با دستور query میتونن insert بشن.        
# اینجا values میاد مقادیری که میخوایم از کاربر insert کنیم رو میگیره و s ینی string باشه.        
        query = "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)"
        
        # این query ما ازونایی هست که ورودی داره () پس میایم پارامترهاشم این پایین بصورت تاپل وارد میکنیم که execute بشه.        
        self.db.execute_query(query, (username, password, email))
        
        # اینجا query رو commit میکنیم.       
        self.db.commit()



# Image Categories
class Category:
    def __init__(self, db):
        self.db = db
    
    def add_category(self, name):
        query = "INSERT INTO categories (name) VALUES (%s)"
        self.db.execute_query(query, (name,))
        self.db.commit()

    
    def get_all_categories(self):
        query = "SELECT * FROM categories"
        
        #ازونجایی که این query خروجی داره، باید علاوه بر execute شدن، fetch all هم بشه.        
        return self.db.execute_query(query)
        


# Image Handling
class Image:
    def __init__(self, db):
        self.db = db
    
    def upload_img(self, user_id, cat_id, title, desc, file_path):
        query = """INSERT INTO images (user_id, category_id, title, description, file_path) VALUES (%s, %s, %s, %s, %s)"""
        self.db.execute_query(query, (user_id, cat_id, title, desc, file_path))
        self.db.commit()
    
# این متد میگه که کدام user_id کدام عکسها رو آپلود کرده.    
    def search_by_user(self, user_id):
        query = "SELECT * FROM images WHERE user_id = %s"
        return self.db.execute_query(query, (user_id,))

# این متد بر اساس user_id عکس رو حذف میکنه    
    def del_img(self, img_id):
        query = "SELECT * FROM images WHERE id=%s"
        img = self.db.execute_query((query, (img_id,)))
        if img:
            query = "DELETE FROM images WHERE id=%s"
            self.db.execute_query(query, (img_id,))
            self.db.commit()
            os.remove(img[0]['file_path'])








'''
==============================
=====    running DB      =====
==============================
'''


db_info={
    'host':'localhost',
    'user':'root',
    'password':'12345678A'
    }

db=Database(**db_info)
print(vars(db))    # {'host':'localhost', 'user':'root', 'password':'12345678A', 'database': None, 'connection': ,mysql.connector.connection_cexts.CMySQLConnection object at 0x00000213B433D550>, 'cursor': <mysql.connector.cursor_cext.CMySQLConnection object at 0x00000213B5130920>}

# ساختن دیتابیس
db.create_database('image_gallery')
print(vars(db))    # {'host':'localhost', 'user':'root', 'password':'12345678A', 'database': image_gallery, 'connection': ,mysql.connector.connection_cexts.CMySQLConnection object at 0x00000213B433D550>, 'cursor': <mysql.connector.cursor_cext.CMySQLConnection object at 0x00000213B5130920>}
                   # database created!



# ساختن جدول دیتابیس
# روی دیکشنری tables حرکت میکنیم و value هاشو میگیریم

for table in tables.values():
    db.create_table(table)     # 3 tables (users, categories, images) created!




# ---------  ایجاد کردن یک کاربر جدید برای جدول user با استفاده از کلاس User --------

user1 = User(db)
user1.register('n1', 123, 'a@gmail.com')


# ---------  ایجاد کردن یک category جدید برای جدول categories با استفاده از کلاس Category --------

cat1 = Category(db)
cat1.add_category('art')
cat1.add_category('nature')
d = cat1.get_all_categories()
print(d)      # [(1, 'art'), (2, 'nature')]


# ---------  ایجاد کردن یک نمونه جدید برای جدول image با استفاده از کلاس Image --------

img1 = Image(db)
img1.upload_img(1, 1, 'title1', 'desktop')
img1.upload_img(2, 2, 'title2', 'desktop')
img1.upload_img(3, 3, 'title3', 'desktop')

img1.search_by_user(1)
'''
images uploaded by user_id:1:
    
[(1, 1, 'title1', 'desktop'),
 (2, 1, 'title2', 'desktop'),
 (3, 1, 'title3', 'desktop') ]
'''

img1.delete_img(2)
''' 
[(1, 1, 'title1', 'desktop'),
 (3, 1, 'title3', 'desktop') ]
'''











