
# main.py

# مرحله پنجم
# این فایل اگر run بشه برنامه شروع به کار میکنه
# با اجرای این فایل کاربر میاد و سوالات براش نمایش داده میشه و دونه دونه جواب میده


# برعکس فایل seed.py که کلا یکبار اجرا میشه، این فایل همیشه باید اجرا بشه
# با هربار اجرا شدن اتفاقات زیر میوفته:
    # گرفتن اسم کاربر جدید    
    # ساخت user واقعی در دیتابیس    
    # نمایش سوال به کاربر    
    # پاسخ دادن توسط کاربر    
    # ذخیره پاسخ‌های کاربر    
    # نمره دهی    



from database import get_db  #Base , engine,
from crud import create_user, list_questions, submit_answer, calculate_score  # create_question, add_choice,
# from models import User, Questions, Choice, Answers


# ساخت session دیتابیس
# یعنی یک ارتباط فعال با دیتابیس باز کن
# به دیتابیس وصل شو
db = get_db()   



print('================= ✨ Mini Quiz demo ✨ ===================')
print("🙋🏻‍ Welcome!")
print('===========================================================')
print("\n")

#____________________________ ساخت کاربر واقعی برای ورود به سیستم _________________________
print('🧾 First you must insert your name')
name = input('enter your name: ')
user = create_user(db, name = name)
print(f"✅ User created successfuly! 👤 ID: {user.id}")
print('===========================================================')

# ساخت کاربر در فایل main مجاز است ولی ساخت داده اولیه نباید اینجا باشه
# داده اولیه باید در seed.py ایجاد بشه
#____________________________________________________________________________________________





# ______________________________________ نمایش سوالات ، گرفتن پاسخ و ذخیره آن _______________

questions = list_questions(db)   # گرفتن سوال‌ها

print("\n")
print('__________________ Questions___________________')
print("\n")
    
print("Total Questions:", len(questions))      # 111111111111111111111111111111111111111111111


for q in questions:
    
    print(f'Question{q.id}: {q.text}')     # نمایش متن سوال

    choice_map={}
    
    for i, c in enumerate(q.choices, start=1):
        print(f'{i}- {c.text}')     #  نمایش گزینه‌های هر سوال از 1 تا 3
        choice_map[i] = c.id
        # با استفاده از enumerate و index میایم از عدد 1 دونه دونه برای هر c میریم بالا. اینجوری عدد گزینه 1 و 2 و 3 تشکیل میشه                                    


    answer = input("\nEnter choice id (or press s to skip): ")
    
    # اینجا گفتیم اگه کاربر s زد سوال رو رد کن، در غیراینصورت جواب رو submit کن    
# همچنین اومدیم از یک mismatch بین ورودی کاربر و اطلاعات دیتابیس جلوگیری کردیم    
# عدد گزینه‎ها در دیتابیس بصورت 1.2.3  - 1.2.3  و ... ذخیره نمیشه    
# بلکه به ترتیبی که گزینه ها وارد میشه یعنی 1-2-3-4-5-6-7-9-... عدد گذاری میشه    
# حالا کاربر مثلا برای یک گزینه که choice.id واقعی آن برابر مثلا 15 هست داره یه input برابر مثلا 3 وارد میکنه    
# این دوگانگی باعث ارور میشه    
# زمانیکه از کاربر index(1,2,3) میگیریم پس باید یجوری برای دیتابیس معادل سازیش کنیم    
# پس میایم در Answer_index و selected_choice این مشکل رو حل میکنیم و input به index واقعی تبدیل میشه    
# همچنین کل عملیات رو در try-except گذاشتیم که اگه اروری داشتیم دیگه ترمزش رو بکشه و دوباره لوپ تکرار نشه    

    try:

        if answer.lower() == "s":
            print("Skipped ❌")
            submit_answer(
                db,
                user_id=user.id,
                question_id=q.id,
                choice_id=None
            )
            continue

        answer_index = int(answer)

        selected_choice_id = choice_map[answer_index]

        submit_answer(
            db,
            user_id=user.id,
            question_id=q.id,
            choice_id=selected_choice_id
        )

    except (ValueError, KeyError):

        print("Invalid input → skipped")

        submit_answer(
            db,
            user_id=user.id,
            question_id=q.id,
            choice_id=None
        )
#___________________________________________________________________________________________





#________________________________محاسبه نمره کاربر و نمایش نتیجه__________________________________

# با استفاده ازین تابع که قبلا در CRUD تعریف کرده بودیم، میگیم برو همه جوابهای کاربر رو بررسی کن و بگو چندتا درست است
score = calculate_score(db, user.id)

print("\n=============== 📊 RESULT ===============")
print(f"User: {user.name}")
print(f"Score: {score} / {len(questions)}")
#___________________________________________________________________________________________________



