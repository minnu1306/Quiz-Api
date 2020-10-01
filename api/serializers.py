from .models import Ques,Choice,UserD
from rest_framework import serializers

class QuesSe(serializers.ModelSerializer):
	class Meta:
		model=Ques
		fields=['id','question']
		
class ChoiceSe(serializers.ModelSerializer):
	def create(self, validated_data):
		question=Ques.objects.get(id=validated_data["question"])
		validated_data["question"]=question
		choice=Choice.objects.create(**validated_data)
		
		return choice

	class Meta:
		model=Choice
		fields=['choice']
		
class UserDSe(serializers.ModelSerializer):

	def create(self,validated_data):
		question=Ques.objects.get(id=validated_data["question_id"])
		validated_data["question"]=question
		user=UserD.objects.create(**validated_data)
		
		return user
	class Meta:
		model=UserD
		fields=['answer','question']
		
class UserL(serializers.Serializer):

	#user=UserDSe(many=True)
	class Meta:
		model=UserD
		fields=['score']
		
		
		
	
	
