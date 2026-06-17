
# models.py

# جدول‌ها (table) توی این فایل هستن - ساخت این فایل مرحله دوم هست
# ساخت جدول ها به کمک کتابخوانه sqlalchemy و به کمک ORM انجام میشه

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base


# هر جدول یک اسم داره
# ستون های هر جدول هم اسم داره
# همچنین هر ستون باید تایپ هم داشته باشه: ستون عدده؟ str؟ یا float؟ یا ...






# شکل کلی جدول user:
#  ________________________
#  |         USER         |
#  |______________________|
#  | id  | name | answers |
#  | ... | ...  |   ...   |


class User(Base):
    __tablename__ = 'users'   # اسم دلخواه برای جدول
    
    # ستون اول    
    id = Column(Integer, primary_key=True, index=True)
    # این اولین ستون این جدوله که تایش integer هست    
    # primary_key=True -> یعنی خودش خود به خود بسازه و ایندکس بشه
# این ستون همیشه تو همه جدول‌ها به همین صورت وجود داره    

# ستون دوم    
    name = Column(String, nullable=False)
    # تایپ این ستون String هست    
    # nullable=False -> یعنی این ستون اجازه نداره خالی باشه و باید حتما پر بشه
    
    # ستون سوم    
    # answers = Column(String, nullable=False) #null khali bashe
    answers = relationship('Answers', back_populates='user')
    # با استفاده از relationship میایم ستون یک جدول رو به جدول دیگه متصل میکنیم    
    # الان ستون answers از جدول User به جدول Answers متصل شده    
    # الان دیگه با اینکار ستون Asnwers یک ستون معمولی نیست    
    # back_populates='user' -> یعنی این رو کاربر خودش پر میکنه
    
    









# شکل کلی جدول Questions:
#  _________________________________
#  |          Questions            |
#  |_______________________________|
#  | id  | text | choice |  answer |
#  | ... | ...  |   ...  |   ...   |


class Questions(Base):
    __tablename__ = 'questions'
    
    # ستون اول    
    id = Column(Integer, primary_key=True, index=True)
    
    # ستون دوم    
    text = Column(String, nullable=False)
    
    # ستون سوم    
    # choice = Column(String, nullable=False)
    choices = relationship('Choice', back_populates='question')
    
    # ستون چهارم    
    # answer = Column(Integer, nullable=False)
    answers = relationship('Answers', back_populates='question')
    
    








# شکل کلی جدول Choices:
#  _________________________________________
#  |         Choices                       |
#  |_______________________________________|
#  | id  | text | is_correct | question_id |
#  | ... | ...  |    ...     |    ...      |

class Choice(Base):
    __tablename__  ='choice'
    
    # ستون اول    
    id = Column(Integer, primary_key=True, index=True)

# ستون دوم    
    text = Column(String, nullable=False)
    
    # ستون سوم    
    is_correct = Column(Boolean, nullable=False)
    
    # ستون چهارم    
    question_id = Column(Integer, ForeignKey('questions.id'))
    
    
    question = relationship('Questions', back_populates='choices')
    answers = relationship('Answers', back_populates='choice')







# شکل کلی جدول Answers:
#  _____________________________________________
#  |                 Answers                   |
#  |___________________________________________|
#  | id  | user_id | question_id | choice_id   |
#  | ... |   ...   |    ...      |    ...      |


class Answers(Base):
    __tablename__ = 'answers'
    
    # ستون اول    
    #id = Column(Integer, prioice_id = Column(Integer, ForeignKey('choice.id'), nullable=True), mary_key=True, index=True)
    id = Column(Integer, primary_key=True, index=True)
    
    # ستون دوم    
    user_id = Column(Integer, ForeignKey('users.id'))
    
    # ستون سوم    
    question_id = Column(Integer, ForeignKey('questions.id'))
    
    # ستون چهارم    
    choice_id = Column(Integer, ForeignKey('choice.id'), nullable=True)
# اینجا nullable=True میذاریم یعنی کاربر مجازه که به بعضی سوالات اگه خواست پاسخ نده    

    user = relationship('User', back_populates='answers')
    question = relationship('Questions', back_populates='answers')
    choice = relationship('Choice', back_populates='answers')





# ============================================================================================
# ============================================================================================

# در هر جدول ستون id خودش به ترتیب پر میشه
# ستون هایی که relational هستن هم خودشون بصورت داخلی پر میشن
# پس فقط یه سری ستون میمونه که باید توی فایل crud یه تابع واسشون بسازیم
# که این توابع بیان به ما امکان این رو بدن که به کمک یک ورودی ستون‌ها رو با دیتا پر کنیم











