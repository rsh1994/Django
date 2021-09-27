from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
# 데이터의 각 필드는 Field 클래스의 인스턴스로서 표현됩니다.
# 각 필드가 어떤 자료형을 가질 수 있는지를 Django에게 말해줍니다.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text



# Django는 이 정보를 가지고 다음과 같은 일을 할 수 있습니다.
# - 이 앱을 위한 데이터베이스 스키마 생성(CREATE TABLE 문)
# - Question과 Choice 객체에 접근하기 위한 Python 데이터베이스 접근 API를 생성
