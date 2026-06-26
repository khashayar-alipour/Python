
"""
        ====================================================================
        ===========      Created on Wed Jun 24 14:45:51 2026     ===========
        ===========         Author: Khashayar Alipour            ===========
        ===========                IDE: spyder                   ===========
        ===========             python Datatypes                 ===========
        ====================================================================
"""

# slicing - indexing - casting
# Datatype methods
# Python variables       _____ numbers
# Datastructure ________|_____ string
                       #|_____ list
                       #|_____ tuple
                       #|_____ set
                       #|_____ dictionary





#=============================
#=============================
'''      Index number      '''
#=============================
#=============================

# داده های قابل شمارش (iterable) به داده هایی میگن که از آنها میشه در یک حلقه استفاده کرد
# با هر بار اجرا شدن حلقه یک عنصر جدید از آن خارج میشود
# مثلا list - tuple - string - dict - set

# دیتاهای قابل شمارش عدد ایندکس دارن
# دیکشنری عدد ایندکس نداره و با استفاده از key به مقدارهاش دسترسی پیدا میکنیم

# عدد ایندکس مثبت از 0 و عدد ایندکس منفی از راست و از 1 شروع میشه






#======================
#======================
'''      Slice      '''
#======================
#======================

# s[start:stop:step]

# عملیات slicing یعنی برداشتن یک تیکه از یک دیتاتایپ Sequence مثل رشته یا لیست یا تاپل
# برای stop هرچی بذاریم یک عدد کمترش رو میگیره
# اگر start نذاریم از 0 میگیره و اگر stop نذاریم میره تا آخر


#-----String
text = "PYTHON"
# "P Y T H O N"
#  0 1 2 3 4 5
print(text[:4])   #'PYTH'
print(text[2:])   #'THON'
print(text[:])    #'PYTHON'   کل داده
print(text[::1])  #'PYTHON'
print(text[::2])  #'PTO'
print(text[::3])  #'PH'

# اگر step منفی بشه یعنی از آخر به اول حرکت کن و بچین
print(text[::-1])    #'NOHTYP'  داده رو برعکس میکنه

# ایندکس منفی
# "P  Y  T  H  O  N"
# -6 -5 -4 -3 -2 -1
print(text[-2:])  #'ON'


#-----List
numbers = [10,20,30,40,50,60]
print(numbers[:3])    #[10, 20, 30]   سه عضو اول
print(numbers[2:])    #[30, 40, 50, 60]   از عضو سوم تا آخر
print(numbers[::2])   #[10, 30, 50]   یکی در میون
print(numbers[::-1])  #[60, 50, 40, 30, 20, 10]   برعکس میکنه


#-----Tuple
colors = ("red", "green", "blue", "black", "white")
print(colors[1:4])    #('green', 'blue', 'black')
print(colors[::-1])   # ('white', 'black', 'blue', 'green', 'red')


#-----set
# اسلایس روی set نمیشه چون عدد ایندکس و ترتیب نداره ❌
s = {1,2,3,4}
s[1:3]   # Error


#----dictionary
# مستقیما نمیشه اسلایس زد ❌
d = {"a":1, "b":2, "c":3}
d[0:2]   # ٍError

# روش درست
keys = list(d.keys())
print(keys[0:2])



#=================================================
# پس مهمترین الگوهای slicing اینا میشن     
# data[:n]   از اول تا قبل از استپ
# data[n:]   از استارت تا آخر
# data[-n:]   از ایندکس منفی تا آخر
# data[:-n]   از اول تا ایندکس منفی
# data[::2]   یکی در میون
# data[::-1]  برعکس
#=================================================









#=============================
#=============================
'''      Type Casting      '''
#=============================
#=============================


'''====== number ======'''

# تبدیل رشته به Int
x = int("10")
print(x)   #10


# تبدیل float به int
x = int(3.9)
print(x)   #3   اعشار حذف نمیشه فقط گرد میشه
int(float("3.14"))    #3


# تبدیل رشته به float
x = float("10.5")
print(x)   #10.5


# تبدیل int به float
x = float(5)
print(x)   #5.0




'''====== str() ======'''
# هرچیزی رو میشه به str تبدیل کرد
x = str(100)
print(x)    #"100"




'''====== bool() ======'''
# با دستور bool() انجام میشه
# اگر ورودی مقدار falthy باشه نتیجه False میشه وگرنه True میشه




'''====== list() ======'''
text = "Python"
print(list(text))    # ['P', 'y', 't', 'h', 'o', 'n']    رشته به لیست

t = (1,2,3)
print(list(t))     # [1, 2, 3]    تبدیل تاپل به لیست

s = {1,2,3}
print(list(s))     # [1, 2, 3]    تبدیل تاپل به لیست

# تبدیل دیکشنری به لیست
student = {"name": "Ali", "age": 22}
print(list(student))     # ['name', 'age']   فقط کلیدهارو میده
list(student.values())   # فقط مقدارها
list(student.items())    # [('name', 'Ali'), ('age', 22) ]   هم کلید هم مقدار




'''====== tuple() ======'''
numbers = [1,2,3]
print(tuple(numbers))    # تبدیل لیست به تاپل    (1, 2, 3)




'''====== set() ======'''
# تبدیل لیست به set
numbers = [1,2,2,3,3,3]
print(set(numbers))    # {1, 2, 3}   تکراری ها حذف میشن



#=================
# Upcasting
# Implicit Type Casting or Automatic Type Conversion
# پایتون به صورت خودکار یک نوع داده را به نوعی "بزرگ‌تر" یا "دقیق‌تر" تبدیل می‌کند تا اطلاعات از بین نرود

# int < float < complex   سلسله مراتب عددی در پایتون

# float > int
a = 10      # int
b = 3.5     # float
c = a + b   # 10.0 + 3.5
print(c)
print(type(c))    # 13.5  float 











'''
============================
============================
======     Number     ======
============================
============================
'''


#=====[ Integer ]=====
print(3)    #3


#=====[ Float ]=====
print(3.5)    #3.5


#=====[ Complex ]=====
# اعداد مختلط از دو قسمت Real و Imaginary تشکیل شده‌اند
x = complex(3, 4)   #3+4j

x= 3+4j
print(x)   #3+4j
print(type(x))    # <class 'complex'>  
print(x.real)     #3.0
print(x.imag)     #4.0









'''
============================
============================
======     Boolean    ======
============================
============================
'''

a = True
print(type(a))     # <class 'bool'>


# متد bool()
# بررسی میکند که یک مقدار از نظر پایتون True هست یا False
print(bool(10))   # True


# مقادیر Falthy در پایتون:
bool(0)
bool(0.0) 
bool("")
bool('')
bool([])
bool(())
bool({})
bool(set())
bool(False)
bool(None)











'''
=========================
=========================
======     List    ======
=========================
=========================
'''


l = [1,2,3,4]
print(type(l))    # <class 'list'>

#===== Nested list =====
matrix = [
    [1, 2, 3],
    [4, 5, 6] ]
print(matrix[1][1])    #5   ردیف با ایندکس 1 و ستون با ایندکس 1 رو بده


#===== Index =====
data = [10, "Ali", 3.14, True]
#        0    1      2     3
#       -4   -3     -2    -1

print(data[0])   #10
print(data[-1])  #True



#======================
# ویژگی های لیست   

# 1-Mutable ✅
names = ["Ali", "Sara", "Reza"]
names[1] = "Maryam"    # -> ['Ali', 'Maryam', 'Reza']  

# 2-Ordered (index number) ✅
# 3-Repeatable elements ✅
# 4-Sliceable ✅
# 5-Iterable ✅
#======================




#===== lenght =====
numbers = [10, 20, 30, 40]
print(len(numbers))    #4
# متود len از 1 شروع میشه


#===== add an elemetn =====
numbers = [10, 20, 30]
numbers.append(40)
print(numbers)     #[10, 20, 30, 40]


#===== remove an element =====
numbers = [10, 20, 30]
numbers.remove(20)
print(numbers)     # [10, 30]


#===== بررسی وجود یک عضو =====
numbers = [10, 20, 30]
print(20 in numbers)     # True


#===== عملیات ضرب و concat =====
# دو لیست زمانی باهم برابر هستند که عناصر آناها در هر ایندکس دونه دونه باهم برابر باشن
# concat
l1=['a',1,2]
l2=[3,4.5]
print(l1+l2)    #['a', 1, 2, 3, 4.5]

# ضرب (تکرار)
l3=[1,2,3]
print(l3*3)     #[1, 2, 3, 1, 2, 3, 1, 2, 3]





#=============================
#=============================
'''     list methods      '''
#=============================
#=============================


#=====[Removing]=====
l=[1,2,3.5,'ali']
x=l.pop()        #ali str
x2=l.pop(2)      #3.5 str
print(l)         # [1,2]
# به عنوان ورودی ایندکس موردنظر رو میگیره - اون عنصر رو از لیست اصلی حذف میکنه و همون عنصر رو با تایپ str برمیگردونه
# اگر ایندکسی مشخص نشه آخرین عنصر رو میگیره
# اگه شماره ایندکسی که میدیم در لیست نباشه ارور میده IndexError: pop index out of range

l=[1,2,3.5,'ali']
l.remove('ali')
print(l)    #[1, 2, 3.5]
print(l.remove(5))    #ValueError: list.remove(x): x not in list
# برعکس pop دیگه ایندکس نمیگیره بلکه مقدار رو مستقیما میگیره
# مقدار جدید برنمیگردونه (خروجی نداره) و لیست اصلی رو inplace تغییر میده
# اولین تکرار مقدار ورودی رو از لیست اصلی حذف میکنه

l=[1,2,3.5,'ali']
l.clear()   # این متد خروجی نداره و لیست اصلی رو تغییر میده
print(l)    #[]   لیست خالی میده

l=[1,2,3.5,'ali']
del(l[0])
print(l)   #[2, 3.5, 'ali']    حذف یک عنصر با استفاده از ایندکس
del(l[0:2])
print(l)   #[2, 3.5, 'ali']  --> ['ali']
del(l)     # این دستور کل لیست رو حذف میکنه حتی [] هم نمیمونه
# تلاش برای پیدا کردن l بعد از دستور del منجر به NameError میشه چون اصلا وجود نداره           


#=====[adding]=====
l=[1,2,3.5,'ali']
l.append('reza')    # این دستور خروجی نداره و هر آبجکتی میشه به عنوان ورودی بهش بدیم که به لیست اصلی اضافه کنه
print(l)            # [1,2,3.5,'ali', 'reza']  عنصر جدید به آخر لیست اضافه میشه
#l.append('reza', 'sara')     # اگر بیشتر از 1 آرگومان به عنوان ورودی به این متد بدیم ارور میده

l=[1,2,3.5,'ali']
l.extend([4,5])   # چسباندن اعضای یک لیست دیگر به انتهای لیست اصلی و تغییر کردن لیست اصلی (خروجی نداره)
print(l)          # [1, 2, 3.5, 'ali', 4, 5]     اضافه شدن به انتهای لیست اصلی
l.extend('reza')
print(l)          # [1, 2, 3.5, 'ali', 4, 5, 'r', 'e', 'z', 'a']
# به عنوان ورودی یک iterable میگیره، سپس آرگومان ورودی رو iter میکنه و عناصرش رو باز میکنه و لیست اصلی رو extend میکنه

l=[1,2,3.5,'ali']
#.insert(i,x)    # x=new element(any object)  | i=index
# برعکس متدهای append و extend با این متود میتونیم هرجای لیست خواستیم یه عنصر جدید اضافه کنیم
l.insert(0,1)
print(l)         # [1, 1, 2, 3.5, 'ali']    این متود خروجی نداره
l.insert(8,"element")    # اگه عدد ایندکس وجود نداشته باشه خودش به آخر لیست اضافه میکنه
print(l)         # [1, 1, 2, 3.5, 'ali', 'element']


#=====[Ordering]=====
l1=[8,1,0,4,9,4,6]
l2=[6,7,3,'ali',1,'sara']    # اگه روی این لیست این متد رو بزنیم تایپ ارور میده چون عناصرش ترکیبی از عدد و رشته هست
l1.sort()
print(l1)    #[0, 1, 4, 4, 6, 8, 9]   این متد خروجی نداره و لیست اصلی رو تغییر میده
l1.sort(reverse=True)
print(l1)    # [9, 8, 6, 4, 4, 1, 0]   بصورت نزولی مرتب میکنه

x=sorted(l1)
print(x)     # [0, 1, 4, 4, 6, 8, 9]   این متد تابع پایتون هست و مخصوص لیست نیست و خروجی جدید میده

l=[2,482,5,9]
l.reverse()
print(l)    # [9, 5, 482, 2]   لیست رو فقط برعکس میکنه


#=====[جست‌وجو و اطلاعات]=====
l=[6,7,3,'ali',1,'sara']
x=l.index('ali')   # شماره ایندکس اولین عنصری که به عنوان ورودی بهش دادیم رو برمیگردونه
print(x)     #3
# اگر ورودی موردنظر در لیست وجود نداشته باشه ValueError میده
x2=l.index('ali',1,4)    # در بازه ایندکس 1 تا ایندکس 4 اولین "علی" که پیدا کردی عدد ایندکسش رو برگردون
print(x2)    #3   .index(x,start,stop)   این متد 3 آرگومان میگیره

l=[1,1,1,4,5,8]
x=l.count(1)  # تعداد دفعات تکرار این ورودی در لیست رو برگردون
print(x)      #3   تایپ خروجی عدد هست


#=====[copy]=====
old=[1,2,3,4,5]
new = old.copy()   #لیست اصلی تغییر نمیکنه
print(new)   #[1, 2, 3, 4, 5]   shallow copy

new = old[:] #روشی سریع برای کپی کردن کل لیست
print(new)   #[1, 2, 3, 4, 5]













'''
===========================
===========================
======     String    ======
===========================
===========================
'''


"Hello"
"Python"
"123"
"سلام"
"Ali Reza"
# <class 'str'>


#===== Index =====
name = " P  y  t  h  o  n"
       # 0  1  2  3  4  5
       #-6 -5 -4 -3 -2 -1

print(name[0])   #P
print(name[-1])  #n


#===== Lenght =====
name = "Python"
print(len(name))  #6


#===== Concatenate =====
first = "Ali"
last = "Reza"
print(first + last)    #AliReza


#===== Repeat =====
print("Hi" * 3)    #HiHiHi



#===========================
# ویژگی های رشته      

# 1-Immutable
name = "Python"
name[0] = "J"    # ❌ error

name = "Python"
name = "Jython"  #این مشکلی نداره

# 2-Indexable ✅
# 3-Ordered ✅
# 4-Repeatable ✅
# 5-Sliceable ✅
# 6-Unicode based  ✅ میشه به همه زبانها یک رشته بنویسیم
# 7-Iterable ✅ میشه روش لوپ بزنیم
#===========================







#=============================
#=============================
'''      str methods      '''
#=============================
#=============================


s="kHAshayaR alp"

#===== تغییر وضعیت حروف (case) =====
s.upper()    #KHASHAYAR ALP
s.lower()    #khashayar alp
s.title()    #Khashayar Alp   حروف اول کلمات بزرگ میشه
s.capitalize()    #Khashayar alp   فقط حرف اول کل متن


#===== جست و جو و جایگزینی =====
s.find("a")    # ایندکس اولین موردی که پیدا میکنه رو میده (نباشه -1 میده)
s.find("sh")   # ایندکس اولین حرف عبارت رو میده 
s.find("s",2,4)    # تو بازه ایندکس 2 تا 4 این عبارت رو داریم؟ اگه آره عدد ایندکسش وگرنه -1 میده

s.index()   # دقیقا مثل بالایی هست
# با این تفاوت که اگه چیزی وجود نداشته باشه میگه ValueError:substring not found            

s.count("a")    #3  تعداد تکرار یک مقدار رو میده
s.count("a",0,4)

s.startswith("s")    #False
s.endswith("p")      #True

s.replace("alp", "ALP")   #kHAshayaR ALP   replace(old,new,count)
# این متد رشته اصلی رو تغییر نمیده پس نتیجه رو باید در یک متغیر ذخیره کرد                          

s.replace("a","")    #kHAshyR lp     حذف یک کاراکتر از کل متن

text = "apple apple apple"
text.replace("apple", "orange")     #orange orange orange   جایگزینی چندباره

text = "apple apple apple"
text.replace("apple", "orange", 1)    #orange apple apple |  count parameter -> مشخص میکنه فقط تعداد خاصی جایگزین بشه

phone = "0912-123-4567"
phone.replace("-", "")   #09121234567   حذف بخشی از متن

text = "banana"
text.replace("a", "*")   #b*n*n*   جایگزینی کاراکترها

text = "Python Java"
text.replace("Python", "Go").replace("Java", "Rust")    # Go Rust   پشت سر هم


#===== تکه کردن و اتصال =====
s.split(" ")    # ['kHAshayaR', 'alp']    تبدیل رشته به لیستی از کلمات
s.split("a")    # ['kHAsh', 'y', 'R ', 'lp']
# وقتی به Separator موردنظرش رسید حذفش میکنه و ازونجا از هم جدا میکنه                

s.split("a",1)   #['kHAsh', 'yaR alp']   تعداد مشخص میکنیم که چندبار از جداکننده استفاده کنه
s.split()        #['kHAshayaR', 'alp']   اگه جای جداکننده خالی باشه خودش فاصله رو درنظر میگیره

l=["khashayar", "alipour", "programmer"]
"-".join(l)      #'khashayar-alipour-programmer'   اتصال اعضای لیست با جداکننده موردنظر و در نهایت تایپش رشته میشه

text = """Ali
Sara
Reza"""
text.splitlines()    # ['Ali', 'Sara', 'Reza']     هرجا انتهای یک خط برسه اونجارو میشکونه و میذاره توی یک لیست
text.split("\n")     # اینم نتیجه بالایی رو میده



#===== اعتبارسنجی =====
s.isdigit()    #عدد؟
s.isalpha()    #حروف الفبا؟
s.isalnum()    #عدد یا حروف؟
s.isspace()    #فقط فضای خالی؟
s.isupper()    #حروف بزرگ؟
s.islower()    #حروف کوچک؟


#===== cleaning =====
# white space: space, enter, tab
s.strip()    #حذف فاصله های اضافی از دوطرف
s.strip("#")    #حذف کاراکتر موردنظر از دوطرف
s.lstrip()      # حذف از چپ
s.rstrip()      # حذف از راست
s.zfill()       #00042  پرکردن با صفر



#===== format =====
# format(*args: object, **kwargs: object) -> str
# هرجا اولین {} رو دید میره متغیر اول خودش رو میریزه داخلش و همینطوری الی آخر ...
y=2020
e="corona"
n="reza"
print("in this year {}, {} happend to {}".format(y,e,n))
# in this year 2020, corona happend to reza

# میتونیم به هر {} عدد ایندکس بدیم:
print("in this year {1}, {0} happend to {2}".format(y,e,n))
# in this year corona, 2020 happend to reza

print("{} {} {}".format("python", "is", "fun"))    #python is fun

print("{:.2f}".format(3.14678965))    #3.15
# میخوایم بخش خاصی رو جدا کنیم (:)   کجارو؟اعشار(.)   چند رقم؟ (2) رقم    f=float



#===== چند متد دیگه از str =====
'capitalize','casefold','center','encode','expandtabs','format_map','isascii','isdecimal','isidentifier',
'isnumeric','isprintable','ljust','maketrans','partition','removeprefix','removesuffix','rfind','rindex',
'rjust','rpartition','rsplit','rstrip','swapcase','translate'















'''
==========================
==========================
======     Tuple    ======
==========================
==========================
'''

# تاپل برعکس لیست بعد از ساخته شدن قابل تغییر نیست
# پس درجاهایی کاربرد داره که میخوایم دیتا ثابت باشه ولی نمیشه از لیست استفاده کرد
# لیست با [] ساخته میشه ولی تاپل با () ساخته میشه


tup = ("Ali", "Sara", "Reza")
print(type(tup))    # <class 'tuple'>

# بدون () هم میشه تاپل ساخت
t = 1,2,3
print(type(t))   #<class 'tuple'>


#===== تاپل تک عضوی =====
x = (10)    #Int
x = (10,)   #Tuple
x = 10,     #Tuple


#===== index =====
names = ("Ali", "Sara", "Reza")
        #  0      1       2
        # -3     -2      -1

print(names[0])    #Ali
print(names[-1])   #Reza


#===== Lenght =====
numbers = (10, 20, 30, 40)
print(len(numbers))    #4



#===========================
# ویژگی های تاپل      

# 1-Immutable 
names = ["Ali", "Sara", "Reza"]
names[0] = "Maryam"    #در لیست مشکلی نداره

names = ("Ali", "Sara", "Reza")
names[0] = "Maryam"    # ❌ TypeError  

# 2-Indexable ✅
# 3-Ordered ✅
# 4-Repeatable ✅
# 5-Sliceable ✅
# 6-Iterable ✅
#===========================


#===== Unpacking =====
# می‌توان اعضای تاپل را مستقیم در متغیرها ریخت

person = ("Ali", 25, "Tehran")
name, age, city = person
print(name)    #Ali
print(age)     #25
print(city)    #Tehran







#=============================
#=============================
'''      tuple methods     '''
#=============================
#=============================

# تاپل کلا 2 تا متد داره: index و count

#=====[index]=====
#index(value,start,stop)    value=any type
t=(1,2,3,'ali')
x=t.index('ali')
print(x)    #3
x=t.index('reza')
print(x)    # ValueError: tuple.index(x): x not in tuple


#=====[count]=====
#count(value:any) -> int
t=(1,'a',2,'a')
x=t.count('a')
print(x)    #2
x2=t.count('b')
print(x2)   #0   اگه ورودی در تاپل موردنظر وجود نداشته باشه 0 برمیگردونه


#====changing an element=====
# میشه با روش Casting یک المنت تاپل رو تغییر داد
# تغییر دادن المنت در خود تاپل ممکن نیست، ولی میشه تاپل رو به لیست cast کنیم
# المنت موردنظر رو تغییر بدیم و دوباره به تایپ تاپل برگردونیم

t=(1,2,3)    #t[1]=0 -> not possible
l=list(t)    #[1,2,3]
l[1]=0       #[1,0,3]
t=tuple(l)   #(1, 0, 3)


#=====adding new element=====
# اضافه کردن مقدار جدید به انتهای تاپل
# در روش اول مقدار جدید به عنوان تاپل ذخیره میکنیم و به انتهای تاپل اصلی concat میکنیم
t=8,9,'a'
t2='hello',
print(t+t2)   #(8, 9, 'a', 'hello')

# در روش دوم تاپل اصلی رو به لیست cast میکنیم و بعد با append یا Extend مقدار جدید میدیم
t=8,9,'a'
l=list(t)        #[8,9,'a']
l.append(10)     #[8,9,'a',10]
t=tuple(l)       #(8,9,'a',10)


#=====[delete an element]=====
t=(1,2,3,4)
l=list(t)    #[1,2,3,4]
l.remove(3)  #[1,2,4]
l.pop(2)     #[1,2]   index number
t=tuple(list)














'''
========================
========================
======     Set    ======
========================
========================
'''

names = {"Ali", "Sara", "Ali", "Reza", "Sara"}
print(names)    #{'Ali', 'Sara', 'Reza'}
print(type(names))    #<class 'set'>

# این دیتاتایپ عضو تکراری را قبول نمی‌کند و ترتیب اعضا برایش مهم نیست
# در set مقادیر unique و غیرتکراری وجود داره

# وقتی فقط وجود یا عدم وجود مهم است یا نمیخوایم مقادیر تکراری وجود داشته باشه از Set استفاده میکنیم
# از کاربرد های دیگر Set بررسی سریع وجود یک عنصر در مجموعه میباشد
# همچنین عملیاتهای ریاضی مثل اشتراک و اجتماع با set انجام میشه

# برعکس تاپل، برای ساختن یک set تک عضوی نیازی نیست کنارش , بذاریم
s={"a"}


#===========================
# ویژگی های set      

# 1-Immutable  ❌

# 2-No index
names = {"Ali", "Sara", "Reza"}
print(names[0])    #❌ خطا

# 3-Unordered  ❌
numbers = {10, 20, 30, 40}
print(numbers)    # {40, 10, 30, 20} or {10, 20, 30, 40} or ...

# 4-Unrepeatable  ❌  اعضای تکراری حذف میشن

# 5-Equality
s1={1,1,2,3}
s2={1,2,2,3}
print(s1==s2)   #True

# 6-Iterable ✅   میشه روش حلقه زد ولی معلوم نیست نتیجه چاپ در هر دور چی باشه

# 7-unSliceable  ❌  نمیشه برش بزنیم   s[0:2] -> error
#===========================


#=====| Length |=====
numbers = {10, 20, 30}
print(len(numbers))    #3


#=====| Empty set |=====
s = {}    # dict ❌
s = set()   # empty set ✅


#=====| عملیات ریاضی برای Set |=====
A = {1, 2, 3}
B = {3, 4, 5}

#Union (همه اعضای دو مجموعه)
print(A | B)    #{1, 2, 3, 4, 5}

#Intersection (اعضای مشترک)
print(A & B)    #3

#تفاضل (اعضای A که در B نیستند)
print(A - B)    #{1,2}
#==================================


#=====| متد set() |=====
# با استفاده ازین متد میشه لیست رو به set تبدیل کرد
numbers = [1, 2, 2, 3, 3, 4]   #list
newNumbers = set(numbers)      #set








#=============================
#=============================
'''      set methods     '''
#=============================
#=============================

#=====[add()]=====
# ورودی با هر تایپی | خروجی نداره
# اگر مقدار جدید تکراری باشه حذف میشه
# عضو جدید مشخص نیست که قراره به کدوم قسمت از Set اصلی اضافه بشه چون ترتیب ندارن
s={1,2,3}
s.add(4)
print(s)    #{1, 2, 3, 4}


#=====[remove()]=====
# ورودی با هر تایپی | خروجی نداره
s={1,2,3,"ali"}
s.remove("ali")
print(s)     #{1,2,3}
s.remove("reza")
print(s)     #KeyError: 'reza'


#=====[discard()]=====
# دقیقا همون کار remove رو میکنه ولی دیگه keyError نمیده
s={1,2,3,"ali"}
s.discard("ali")
print(s)     #{1,2,3}
s.discard("reza")
print(s)     #{1, 2, 3}   ورودی رو پیدا نکرد و خود ست رو برگردوند ولی ارور نداد


#=====[clear()]=====
# یک set خالی تحویل میده
s={1,2,3}
s.clear()
print(s)    #set()


#=====[intersection()]=====
# عملیات اشتراک در ریاضی
# با علامت ampersand (&) هم میشه همین کار رو انجام داد
s1={1,1,2,3}
s2={1,2,2}
f=s1.intersection(s2)    #{1, 2}
x=s1&s2    #{1, 2}


#=====[union()]=====
# عملیات اجتماع
# با علامت OR (|) هم میشه همین کارو انجام داد
s1={1,1,2,3}
s2={1,2,2,4,5}
f=s1.union(s2)    #{1, 2, 3, 4, 5}
x=s1|s2      #{1, 2, 3, 4, 5}


#=====[difference()]=====
# عملیات تفاضل (-) در ریاضی
# این کارو با علامت تفاضل (-) هم میشه انجام داد
s1={1,1,2,3}
s2={1,2,2}
f=s1.difference(s2)   #{3}    چیزهایی که در 1 هست ولی در 2 نیست
x=s1-s2    #{3}
y=s2-s1    #{}    چیزهایی که در 2 هست ولی در 1 نیست
















'''
===============================
===============================
======     Dictionary    ======
===============================
===============================
'''

# در لیست برای دسترسی به المان‌ها عدد ایندکس داشتیم
# در دیکشنری برای دسترسی به valueها key داریم
# کلیدهای تکراری مجاز نیست ولی میتونیم value های تکراری داشته باشیم
# اگر یک کلید تکراری باشه value جدید جایگزین میشه
#d={"a":1, "a":2} -> {"a":2}

student = {
    "name": "Ali",
    "age": 22,
    "city": "Tehran" }
print(type(student))    # <class 'dict'>

# کلیدها باید immutable باشن پس رشته و int مجازه و استفاده از لیست و set و دیکشنری برای کلید مجاز نیست
# ولی valueها میتونن هر دیتاتایپی باشن و محدودیت نداره



#====| Nested dictionary |=====
student = {
    "name": "Ali",
    "scores": {
        "math": 20,
        "physics": 18}
    }
print(student["scores"]["math"])    #20


#=====| Access |=====
print(student["name"])    #Ali
# با روش بالا اگر کلید "name" وجود نداشته باشه خطا میده
print(student.get("name"))    #None  روش جایگزین برای اینکه به ارور نخوریم
print(student.get("name", 0))    # مقدار پیشفرض میدیم که اگه وجود نداشت بره جاش


#=====| adding new element |=====
student = {"name": "Ali"}
student["age"] = 22
print(student)    #{'name': 'Ali', 'age': 22}


#=====| Changing a value |=====
student = {"name": "Ali","age": 22}
student["age"] = 25
print(student)    #{'name': 'Ali', 'age': 25}


#=====| Delete a value |=====
student = {"name": "Ali","age": 22}
del student["age"]
print(student)    #{'name': 'Ali'}


#=====| Length |=====
student = {
    "name": "Ali",
    "age": 22,
    "city": "Tehran"}
print(len(student))    #3



#===========================
# ویژگی های Dict      

# 1-mutable ✅   بعد از ساخت دیکشنری میشه مقادیر رو تغییر داد، کلید جدید اضافه یا کلید قدیمی حذف کرد
# خود keyها به علت hash number خاصی که دارن امکان mutation ندارن                  
d={"name":"ali","age":26}
d["name"]="reza"   #changing value
del d["name"]      #delete a key

# 2-No index  
data = {"name": "Ali","age": 22}
print(data[0])    # ❌ ارور

# 3-ordered  ✅ در پایتون 3.7 به بعد ترتیب وارد کردن کلیدها حفظ می‌شود

# 4-Unrepeatable   ❌ کلید تکراری مجاز نیست
# 5-Iterable ✅ loop on value/ loop on keys/ loop on key-value
# 6-Slicable ❌
# مثلا دیگه نمیشه با d[0:2] برش بزنیم. بجاش:                 
                  # list(d.items())[0:2]
#===========================



#=====[پیمایش در dict]=====

d={"name":"ali", "age":20, 1:2}

for i in d.keys():          #name age 1  (keys)
    print(i)


for i in d.values():        #ali 20 2  (values)
    print(i)
    
                           # [k]   [v]
for k,v in d.items():      # name  ali
    print(k,v)             # age   20
                           # 1     2


#=====[مثال مهم با متد get()]=====
# آیتمهای این لیست رو بصورت key-value در یک dict قرار بده:
L=["A","A","B","B","A","C"]

d={}
for i in L:
        d[i]=d.get(i,0)+1
print(d)

#{'A': 3, 'B': 2, 'C': 1}

# در این روش میگیم i رو get کن و اگه به عنوان key وجود داشت مقدار اون رو +1 کن
# در غیر اینصورت، پیام کنارش (0) رو برگردون و سپس +1 کن
# حالا نتیجه هرچی شد به عنوان یک مقدار برای اون key در d وارد کن






#==================================
#==================================
'''      dictionary methods     '''
#==================================
#==================================


#=====[get()]=====
# ورودی= کلید با هر تایپی  -  خروجی هم میده
# اگر key وجود داشت Value موردنظر رو برمیگردونه وگرنه None برمیگردونه
# وقتی هیچی بهمون برنگردونه و نتونیم چیزی در متغیر ذخیره و چاپ کنیم میشه None

d={"name":"a", "age":20, 1:2}
f=d.get("name")   #"a"
f2=d.get("b")    #None   همچین کلیدی نداریم

# این متد یک option هم داره که یک پیام بعد از key مینویسیم و اگر اون کلید وجود نداشت بجای None پیام چاپ میشه
f=d.get("b", "not found")   #not found


#=====[دسترسی به Value]=====
f=d["name"]
print(f)    #"a"
d["name"]="reza"
print(d)    # {"name":"reza", "age":20, 1:2}


#=====[value()]=====
# ورودی نداره ولی خروجی داره و تمام value هارو نشون میده
# خروجی این متد یک نمای داینامیک از دیکشنری اصلی هست و اگه مقادیر dict اصلی تغییر کنه اینم تغییر میکنه
d={"name":"a", "age":20, 1:2}   # دیکشنری اصلی
x=d.values()
print(x)      #dict_values(['a', 20, 2])
print(type(x))   #<class 'dict_values'>


#=====[keys()]=====
# خروجی این متد یک نمای داینامیک از دیکشنری اصلی هست و اگه کلیدهای dict اصلی تغییر کنه اینم تغییر میکنه
# این متد کلیدهای دیکشنری رو کنار هم برمیگردونه
d={"name":"a", "age":20, 1:2}
x=d.keys()
print(x)       #dict_keys(['name', 'age', 1])
print(type(x))   #<class 'dict_keys'>


#=====[items()]=====
# یک نمای قابل پیمایش از key-value هارو بصورت تاپل برمیگردونه
# بهمون اجازه میده همزمان به key و value دسترسی داشته باشیم
d={"name":"a", "age":20, 1:2}
x=d.items()
print(x)       #dict_items([('name', 'a'), ('age', 20), (1, 2)])
print(type(x))  #<class 'dict_items'>


#=====[pop()]=====
# هر عنصر در دیکشنری = key-value
# وقتی key حذف بشه کل عنصر key-value هم حذف میشه
# این متد میاد key رو حذف میکنه (به همراهش کل عنصر از Dict اصلی حذف میشه) و value آن رو برمیگردونه
# اینجا dict اصلی بصورت in place تغییر میکنه و این متود خروجی هم داره
d={"name":"a", "age":20, 1:2}
x1=d.pop("name")
print(x1)     #"a"  removed value
print(d)      #{'age': 20, 1: 2}    "name":"a" -> removed
x2=d.pop("ali")
print(x2)     #KeyError: 'ali'    همچین کلیدی وجود نداره


#=====[popitem()]=====
# ورودی نمیگیره
# خروجی: آخرین عنصر (کلید-مقدار) اضافه شده به dict رو حذف میکنه و اون رو بصورت تاپل برمیگردونه
d={"name":"a", "age":20, 1:2}
x=d.popitem()
print(x)      #(1, 2)   last element
print(d)      #{'name': 'a', 'age': 20}     1:2 -> removed

d={}     #empty dict
print(d.popitem())    #KeyError: 'popitem(): dictionary is empty'


#=====[update()]=====
# آپدیت کردن یک دیکشنری بوسیله اضافه کردن عناصر یک دیکشنری به دیکشنری دیگر
# اگر یک کلید بین دو دیکشنری مشترک باشه، مقدارش با مقدار جدید آپدیت میشه
# دیکشنری جدید به انتهای دیکشنری قدیمی اضافه میشه
a={"a":"b", 1:2}
b={"name":"ali"}
#x=a.update(b) ->  print(x)=None   این متد خروجی نداره
a.update(b)
print(a)    #{'a': 'b', 1: 2, 'name': 'ali'}
print(b)    #{"name":"ali"}

a={"name":"reza"}
b={"name":"ali"}
a.update(b) #update dict(a) with dict(b)
print(a)    #{'name': 'ali'}


















