
# crud.py

# ساخت این فایل میشه مرحله سوم
# این فایل اجازه میده ما روی دیتابیس عملیاتی که میخوایم انجام بدیم
# داخل این فایل کلی تابع هست که اجازه میده بتونیم عدد وارد دیتابیس کنیم یا ازش خارج کنیم
# بنابراین تمام جدول هایی که ساخته بودیم وارد این فایل میکنیم


from sqlalchemy.orm import Session
from models import User, Questions, Choice, Answers




# در CRUD ما در بعضی تابع‌ها میایم write میکنیم و در بعضی توابع فقط Read میکنیم

#   ___________________________
#   |                         |
#   |    Write Functions      |
#   |_________________________|


def create_user(db:Session, name:str):
    # کل کار این تابع اینه که داخل جدول User بیاد نام کاربر جدید بسازه و وارد کنه    

# این db همان connection/session دیتابیس است    
# از طریقش query میزنیم- دیتا میخونیم-حذف میکنیم-ذخیره میکنیم    

    # یک متغیر ساختیم و ستون name از جدول User رو ریختیم داخلش    
    user = User(name=name)
    
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# مثال    
    #create_user(db, name='ali')
    #create_user(db,name='reza')





def create_question(db:Session,text:str):
    # کار این تابع ایجاد question هست    
    # ستون text از جدول Questions رو پر میکنه    
   
    question = Questions(text=text)
    db.add(question)
    db.commit()
    db.refresh(question)
    return question





def add_choice(db:Session,question : Questions , text:str, is_correct= False):
    # کار این تابع درست کردن گزینه‌هاست    
    # برای ایجاد یک گزینه اول باید بگی به کدوم question؟ چه text میخوای وصل کنی؟ و آیا اون گزینه True هست یا False؟    
    
    choice = Choice(text=text, is_correct=is_correct, question=question)
    db.add(choice)
    db.commit()
    db.refresh(choice)
    return choice












#   ___________________________
#   |                         |
#   |     Read Functions      |
#   |_________________________|


def list_questions(db:Session):
    # این تابع میاد کل سوالات رو به ما میده    
    
    # برو از توی db و query بزن روی جدول questions و همه (all) رو بهم بده (return)    
    return db.query(Questions).all()






'''
===============================================================================
===============================================================================
'''


def submit_answer(db: Session, user_id :int , question_id : int, choice_id:int | None):
    # این تابع پاسخ هایی که کاربر برای سوالات وارد میکنه رو ثبت میکنه    
    # هدف اینه که کاربر یک گزینه برای یک سوال انتخاب می‌کند و داخل جدول answers ذخیره می‌شود    
    
    
    # این answer یعنی یک ردیف جدید برای جدول Answers توی فایل model.py بساز    
    # ستون های جدول هم که مشخصه باید چیا باشه، همونارو اینجا میاریم تا پر بشه    
    
    
    
    try:
        answer = Answers(user_id=user_id, question_id=question_id, choice_id=choice_id)
        db.add(answer)
        db.commit()
        db.refresh(answer)
        return answer

    except Exception as e:
        db.rollback()
        print("DB ERROR:", e)






def calculate_score(db:Session ,user_id:int):
    # این تابع نمره کاربر از جوابهای درست رو بهش نشون میده    
# هدف ازین تایع اینه بفهمیم چند پاسخ درست داده شده    
    # 1- اول باید همه answer های کاربر رو بگیری         
# 2- دوم باید بری داخل choice های مربوطه            
# 3- سوم باید چک کنی is_correct=true هست یا نه      
# 4- چهارم آخر باید تعداد درست هارو بشمری          
    
    answers = db.query(Answers).filter(
        Answers.user_id == user_id
    ).all()

    score = 0

    for ans in answers:

        # خط پایین بخاطر Relationship کار میکنه        
        # میگیم از answer برو به choice مربوطه و بعد مقدار is_correct رو بخون        
        # سپس اگر درست بود بهم برگردون        
        if ans.choice and ans.choice.is_correct:
            score += 1

    return score








def get_top_users(db:Session, n=3):
    # کار این تابع اینه که 3 کاربر برتر که بیشترین جواب درست دادن رو نشون بده    
    
    
    users = db.query(User).all()

    result = []   # اسم و نمره کاربر قراره این تو ذخیره بشه

    for user in users:

        score = calculate_score(db, user.id)

        result.append((user.name, score))

    result.sort(key=lambda x: x[1], reverse=True)
# اینجا sort مرتب میکنه و reverse این مرتب شده هارو بترتیب نزولی میچینه    

# اینجا به روش اسلایس، میگیم از اول لیست تا آیتم nام بردار    
    return result[:n]   


# در متد sort همیشه باید یک چیزی به اسم key function بدیم تا بگه بر اساس چی مرتب کنه    
# لیست Result ما اینجوری هستش:  result = [('ali', 4), ('reza', 2)]     
# هر آیتم اینجوری میشه: ('ali',4)=x    
# ما برای هر آیتم عدد دومش رو میخوایم یعنی x[1]    
# حالا این lambda x: x[1] یعنی چی؟؟   
# یعنی برای هر آیتم، عدد دومش رو بده یا به عبارتی بر اساس نمره (عدد دوم هر tuple) مرتب کن    










def get_unanswered_qeuestions(db:Session, user_id:int):
    # کار این تابع اینه که سوالات بدون پاسخ رو نشون بده    
    # منطق پشت این تابع اینه که همه answer های کاربر رو بگیری    
    # سپس question_id هاشون رو استخراج کنی    
    # سپس سوالهایی که داخل آن لیست نیستن رو بگیر    
    # اینجوری میشه فهمید به کدوم سوالات جوابی داده نشده    
  
    # علامت ~ یعنی NOT    
    # اون خط که این علامت رو داره یعنی سوال‌هایی که داخل answered_ids نیستند    
    
    # این db.query(Answers.question_id) یعنی فقط ستون question_id از جدول answers رو بگیر نه کل جدول    
    # این Answers.user_id == user_id یعنی فقط جواب های همین کاربر    
    # خروجیش میشه شبیه این: [(1,), (3,), (5,)] یعنی این کاربر به سوالهای 1 و 3 و 5 جواب داده    
    answered_questions = db.query(
        Answers.question_id
    ).filter(
        Answers.user_id == user_id
    ).all()

        # حالا میخوایم لیست نهایی که در کد بالا بدست آوردیم رو تبدیل به لیست ساده کنیم    
        # یه حلقه زدیم و هر آیتم (q) اینجوریه (1,) و q[0] یعنی عدد داخل تاپل رو بردار و خارج کن که میشه این [1,3,5]    
    answered_ids = [q[0] for q in answered_questions]

# در کد زیر شرط ما میشه سوال‌هایی که ID آنها داخل answered_ids نیست    
# سوالها [1,2,3,4,5] | جواب کاربر [1,3,5] | نتیجه [2,4]    
# اینجا in یعنی سوالایی که داخل لیست هستن و notin برعکسش میشه    
    # اینجا notin_ یک تابع مخصوص SQLAlchemy است، و _ جزئی از اسم تابع است    
    # in_() | notin_()
    unanswered = db.query(Questions).filter(
        Questions.id.notin_(answered_ids)
    ).all()

    return unanswered










def reset_user_answers(db:Session, user_id:int):
    # به این تابع یوزر ID میدی و پاسخ‌هات به سوالات رو ریست میکنه    
    
    # هرجایی میخوایم از دیتابیس اطلاعات رو بخونیم query میزنیم روی اون جدول    
    
    db.query(Answers).filter(
        Answers.user_id == user_id
    ).delete()

    db.commit()









def get_choice_distribution(db: Session , user_id:int):
    # کار این تابع اینه که مثلا بگه هر سوال چند نفر جواب درست دادن    
    
    # چند سوال پاسخ داده شده؟    
    # چند سوال بدون پاسخ؟    
    # چند درست؟    
    # چند غلط؟    

    # اینجا user_id میشه شماره کاربری که میخواهیم آمارش رو ببینیم    
    # متود query یعنی برو روی این جدول سرچ کن و عملیات انجام بده    
    # متود count میاد برامون تعداد ردیف های جدول رو میشمره    
# متود all یعنی همه نتایج رو بصورت یک لیست برگردون    
# پس اینجا متغیر answer یک لیست از آبجکت هاست    

    total_questions = db.query(Questions).count()

    answers = db.query(Answers).filter(
        Answers.user_id == user_id     # مثلا اگر شماره کاربر 2 بود، فقط پاسخ هایی رو بده که برای کاربر 2 هستن
    ).all()

    answered_count = len(answers)

    unanswered_count = total_questions - answered_count

    correct = 0
    wrong = 0

# بخاطر relationship هر Answer به یک Choice وصل هست    
# پس از روی ans که یک آبجکت (ردیف) از جدول Answers هست میتونیم به پاسخ کاربر دسترسی پیدا کنیم    
    for ans in answers:

        if ans.choice.is_correct:
            correct += 1
        else:
            wrong += 1
    
    return {
        'total_questions': total_questions,
        'answered': answered_count,
        'unanswered': unanswered_count,
        'correct': correct,
        'wrong': wrong
    }
            







