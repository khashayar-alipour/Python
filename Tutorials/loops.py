
"""
        ====================================================================
        ===========      Created on Wed Jun 24 17:35:27 2026     ===========
        ===========         Author: Khashayar Alipour            ===========
        ===========                IDE: spyder                   ===========
        ===========               python Loops                   ===========
        ====================================================================
"""


# OVER VIEW
    # conditional statements
    # ternary operators
    # for loop
    # while loop
    # break/continue
    # loop termination methods






'''
===========================================
======     conditional statements    ======
===========================================
'''

# if   elif   else

# اجرای یک بخش از کد فقط در صورتی که یک شرط برقرار باشد
# هرجا condition جلوی عبارت شرطی True باشه، همون عملیات اجرا میشه و دیگه دنبال بقیه شرطها نمیره

# میشه در condition از انواع عملگرهای مقایسه ای استفاده کرد
# مهم اینه که در نهایت جواب این عبارت True میشه یا False میشه

# if condition1:
#     ...
# elif condition2:
#     ...
# elif condition3:
#     ...
# else:
#     ...


# مثال اول
score = 75

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
    

# مثال دوم
is_active = True

if is_active:
    print("Account active")







'''
=====================================
======     Ternary Operator    ======
=====================================
'''

# برای کوتاه نوشتن عبارت شرطی کاربرد داره

age = 20
status = "Adult" if age >= 18 else "Child"
print(status)   #Adult










#==========================
#======     loops    ======
#==========================

# انجام کارهای تکراری با تعداد بالا

#    __________________           _________________          __________________
#   |                  |         |                 |        |                  |
#   |  input(متغیر)    |  ===>   |  process(ثابت) |  ===>  |  output (متغیر)  |
#   |__________________|         |_________________|        |__________________|


# حلقه یک بلاک از کد رو با تعداد محدودی که ما مشخص میکنیم اجرا میکنه
# دو نوع حلقه داریم:
    # 1- تعداد تکرار محدود و مشخص (مثل اضافه کردن یک نمره مشخص به تعداد مشخص دانشجو)    
# 2- تعداد تکرار محدود و نامشخص (مثل تعداد خرید از فروشگاه اینترنتی که مشخص نیست توی یک روز چنتا بشه)    

# برای نوع 1 هم for کاربرد داره هم while
# برای نوه 2 فقط while کاربرد داره




'''
=============================
======     for loop    ======
=============================
'''

#======================
# ساختار اول    
#======================

iterable = "abcd"
for i in iterable:
    print("something")
# این ساختار برای دیتاتایپ های sequence مثل رشته و لیست و تاپل کاربرد داره
# در این حالت range میشه از ایندکس 0 تا آخر در دیتای ما
# روی دونه دونه عناصر دیتای موردنظر حرکت میکنه و اونارو میگیره
# i = loop variable


#_________________________
string="reza"
counter=0
for i in string:
    counter+=1
    print(f"{counter}-{i}")
# 1-r
# 2-e
# 3-z
# 4-a


#_________________________
s=input("enter a string: ")
counter=0
for i in s:
    counter+=1
print(f"Your string has {counter} words")
# enter a string: khashayar
# Your string has 9 words


#_________________________
s=input("enter a string: ")
counter=0
for i in s:
    if i=="a":
        counter+=1
print(f"Your string has {counter} 'a' words")
# enter a string: khashayar
# Your string has 3 'a' words


#_________________________
# Fibunacci series: 0,1,1,2,3,5,8,...
# اعداد پایه: a=0 و b=1
# c=a+b
count=int(input("how many digits of fibunacci should be printed?: "))
first=0
second=1
for i in range(count):
    print(first)
    third=first+second
    first=second
    second=third
# how many digits of fibunacci should be printed?: 15
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377


#_________________________
# یک رشته از ورودی بگیر و برعکسش کن
s=input("enter a string: ")
d=""
lastIndex= len(s)-1     # عدد لن همیشه یک عدد از ایندکس کمتره
for i in range(lastIndex, -1, -1):    # استاپ رو -1 گذاشتیم که حرف اول با ایندکس 0 رو هم بگیره
    d=d+s[i]
print(d)
# enter a string: khashayar
# rayahsahk


#_________________________
# استفاده از متد end
# این متد یک option برای تابع print هست
# در حلقه کاربردش اینه که هرجا حلقه خواست enter بزنه و بره خط بعدی، End جلوشو میگیره
# این End یک separator هم داره که باهاش هرچی که توی هر مرحله پرینت میشه رو به پرینت قبلی concat میکنه
s=input("enter a string: ")
lastIndex= len(s) - 1
for i in range(lastIndex,-1,-1):
    print(s[i], end="")
# enter a string: khashayar
# rayahsahk


#_________________________
# حلقه روی دیکشنری
student = {"name": "Ali", "age": 22}
for key, value in student.items():
    print(key, value)
# name Ali
# age 22







#====================
# ساختار دوم    
#====================

for i in range(1,11):      #range(start,stop,step)
    print("something")

# range()  یک تابع که یه سری عدد تولید میکنه
# Range(5)  0,1,2,3,4

# در ساختار دوم حلقه‌ی For یکبار بیشتر از range مشخص شده اجرا میشه
 # یعنی مثلا توی بازه 1 تا 10 (خود 11 حساب نمیکنه) بعد از اینکه دفعه 10 اجرا شد
 # یکبار دیگه دفعه 11 اجرا میشه و چک میکنه و متوجه میشه که توی range مشخص شده نیست و حلقه رو متوقف میکنه
 
 
for i in range(11):
    print("hello")    
# وقتی فقط 1 ورودی داریم این همون stop هست پس بازه‌ی ما میشه از 1 تا 10


for i in range(100,0,-1):
    print(i)
# شروع=100 و با step منفی برعکس از 100 میاد تا یکی کمتر از stop که میشه تا 1




'''===== important example ====='''

# نمایش اعداد درون رشته به همراه عدد ایندکس اون عدد
s="ab5dc66a8"
#  012345678  index number

c=0                                #c-i
for i in s:                        #1-5
    if i.isdigit():                #2-6
        c+=1                       #3-6
        print(f"{c}-{i}")          #4-8

# با روش بالا نمیتونیم روی عدد ایندکس حرکت کنیم
                             
                                   #i-s[i]
for i in range(0,len(s)):          #2-5
    if s[i].isdigit():             #5-6
        print(f"{i}-{s[i]}")       #6-6
                                   #8-8
# در این روش از len استفاده کردیم تا range حلقه رو اعداد ایندکس دیتا درنظر بگیره
# عدد ایندکس این رشته از 0 تا len-1 هست
# شروع رو برابر 0 میذاریم و پایان دیگه نیاز نیست len-1 بذاریم چون خودش یکی قبل از stop رو در نظر میگیره
# پس اینجوری range ما میشه همون ایندکس
# پس i میشه اعداد 0 تا 8
# برای اینکه بدونیم داخل i  چیه از s[i] استفاده میکنیم











'''
===============================
======     while loop    ======
===============================
'''
# تعداد تکرار محدود و نامشخص
# تازمانیکه شرطی که جلوی while گذاشتیم True باشه حلقه اجرا میشه
# برخلاف حلقه for دیگه شمارنده (range) نداره و باید خودمون یک counter براش ست کنیم

i=1
while i<=10:  #condition
    print(i)
    i+=1     #counter




#==================================
#    حالتهای مختلف حلقه while    
#==================================

#==== 1-counter condition (i<n):
# زمانی هست که counter داریم و در شرط میگیم اگه فلان متغیر مثلا > یا < از عدد n باشه        
i=0
n=5
while i<n:
    i+=1


#==== 2-infinite loop
# زمانیکه در شرط True میذاریم و حلقه دائما اجرا میشه        
# مگه اینکه جایی با nreak یا Continue اون رو متوقف کنیم        
while True:
    print("hello")
    
    
#==== 3-logical condition
# زمانیکه از عملگرهای logical یا computational به عنوان شرط برای حلقه while استفاده میشه        
x=5
x>0 and x%7!=0


#==== 4-boolean/flag condition
# حالت flag گذاری که ازین روش برای خاتمه دادن به حلقه بجای استفاده از break یا continue استفاده میشه        
# در این روش یک متغیر که True هست به عنوان شرط حلقه قرار میگیره        
# هرجا به حالت مطلوب ما رسید مقدارش برابر False میذاریم و حلقه متوقف میشه        
running=True
# process ...
running=False
# Break loop





#========================================
#    حالتهای مختلف اتمام حلقه while    
#========================================

# automatic termination -> condition becomes False
# flag change -? active=False
# break -> break statement
# return -> inside function
# external control -> event
# raise -> exception













'''
=====================================
======     break - continue    ======
=====================================
'''
# break => در یک حالت مشخص حلقه رو میشکونه و متوقف میکنه
# continue => در یک حالت مشخص یک دور رو رد میکنه و حلقه رو ادامه میده
        # هرجا فعال بشه میاد برمیگرده اول حلقه و دیگه ادامه حلقه رو نمیره              
i=0
while True:    #True -> infinite loop
    i+=1
    if i==3:
        continue
    print(i)
    if i==6:
        break
# 1
# 2
#[3] continue(چاپ نکرد و از روش پرید)
# 4
# 5
# 6 break(شرط فعال شد و حلقه شکست)



# بعضی وقتا ممکنه continue حلقه رو به بینهایت ببره و حالتی مثل break ایجاد کنه:
i=0
while i<=10:
    if i==5:
        continue
    i+=1
    print(i)
# 1
# 2
# 3
# 4
# 5
# ... stuck here























