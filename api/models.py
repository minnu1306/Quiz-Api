from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Ques(models.Model):
	question=models.CharField(max_length=100)
	
	
	
	def __str__(self):
		return self.question
class Choice(models.Model):
	question=models.ForeignKey(Ques, on_delete=models.CASCADE)
	choice=models.CharField(max_length=50)
	is_correct=models.BooleanField(default=False)
	
	def __str__(self):
		return self.choice
		
class UserD(models.Model):
	question=models.ForeignKey(Ques, on_delete=models.CASCADE)
	answer=models.CharField(max_length=50)
	correct=models.IntegerField(default=0)
	
	def score(self):
		s=UserD.objects.all().aggregate(score=models.Sum('correct'))
		return s['score']
	def __str__(self):
		return str(self.question.id)	
	
