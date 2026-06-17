
# seed.py

 # فایل طراحی سوالات و گزینه هاش - مرحله چهارم
# کدهای موجود در این فایل یک بار run میشه و دیتابیس و جدول های مارو میسازه
# در فایل database.py فقط engine و ساختارش تعریف (configure) میشه ولی از این فایل در نهایت ساخته میشه


# اهداف این فایل:
    # 1- ساخت دیتابیس و جدول ها
# 2- ساخت سوالات و ساخت گزینه ها
# 3- ساخت کاربر
# 4- ساخت 


# قبل از اجرا کردن فایل اصلی main.py باید این فایل رو یکبار run کنیم
#python seed.py   اینجوری این فایل رو اجرا میکنیم


from database import Base, engine, get_db
from crud import create_user, create_question, add_choice #list_questions




# ________________________ ساخت جدول در db ____________________
print('Creating tables in database...')
Base.metadata.create_all(engine)

print('✅ Tables created successfully')
db = get_db()
#_____________________________________________________________





db = get_db()
# ___________________________________ ساخت کاربر اولیه ___________________________
print('👤 Creating test user ...')
usr1 = create_user(db, name = "Khashayar")
print(f"✅ User created successfuly! ID: {usr1.id}")

# اگه ساخت کاربر در فایل Seed.py باشه، کاربر یکبار ساخته و ذخیره میشه
# ولی اگه در فایل main.py ساخته بشه هربار که برنامه اجرا میشه یک کاربر جدید ساخته میشه
# و دیتابیس از داده های تکراری پر میشه و خراب میشه
# ساخت کاربر برای تست اولیه و شروع کار در این فایل انجام میشه

# اگر کاربر اولیه نسازی دیتابیس جدول user خالی میمونه
# و در این فایل فقط جدول ها و سوالات و گزینه ها ساخته میشن
# عدم وجود کاربر اولیه و خالی بودن جدول user شاید باعث ارور فنی مستقیم نشه
# ولی جاهایی از برنامه که غیر مستقیم برای اجرای اولیه نیاز دارن که user خالی نباشه، ممکنه ارور بخورن
# اینجوری شاید این اشتباه پیش بیاد که برنامه خرابه
#__________________________________________________________________________





# ___________________________ ساخت سوالات _______________________
print('Creating questions in database...')

q1 = create_question(db, text='کدام وسیله برای وارد کردن متن به کامپیوتر استفاده می‌شود؟')
add_choice(db,q1, text='Monitor',is_correct=False)
add_choice(db,q1,text='Keyboard', is_correct=True)
add_choice(db,q1,text='Speaker', is_correct=False)


q2 = create_question(db, text='کدام زبان بیشتر برای طراحی صفحات وب استفاده می‌شود؟')
add_choice(db,q2, text='Windows',is_correct=False)
add_choice(db,q2, text='JAVA',is_correct=False)
add_choice(db,q2, text='HTML',is_correct=True)



q3 = create_question(db, text='وظیفه سی‌پی‌یو در کامپیوتر چیست؟')
add_choice(db,q3, text='ذخیره فایل‌ها',is_correct=False)
add_choice(db,q3, text='نمایش تصویر',is_correct=False)
add_choice(db,q3, text='پردازش اطلاعات',is_correct=True)


q4 = create_question(db, text='کدامیک مرورگر اینترنت است؟')
add_choice(db,q4, text='Chrome',is_correct=True)
add_choice(db,q4, text='Excel',is_correct=False)
add_choice(db,q4, text='Linux',is_correct=False)



q5 = create_question(db, text='فایلهای حذف شده در ویندوز معمولا اول به کجا میرن؟')
add_choice(db,q5, text='Recycle bin',is_correct=True)
add_choice(db,q5, text='Task manager',is_correct=False)
add_choice(db,q5, text='BIOS',is_correct=False)




print('✅ Questions created successfully')
print('💾 finalizing...')
# _______________________________________________________________




