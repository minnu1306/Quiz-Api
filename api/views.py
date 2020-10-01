from django.shortcuts import render
from .models import Ques,Choice,UserD
from .serializers import QuesSe, ChoiceSe, UserDSe, UserL
from django.http import Http404, HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class QuesL(APIView):
	def get(self,request):
		ques=Ques.objects.all()
		serializer=QuesSe(ques, many=True)
		return Response(serializer.data)
		
class ChoiceL(APIView):
	def get(self,request,id):
		
		choice=Choice.objects.filter(question=id)	
		serializer= ChoiceSe(choice, many=True)
		return Response(serializer.data)
		
	def post(self, request, id):
		try:
			Ques.objects.get(id=id)
		except Ques.DoesNotExist:
			raise Http404
		serializer=UserDSe(data=request.data)
		if serializer.is_valid():
			print("lost")
			answer=Choice.objects.get(question=id, is_correct=True)
			if request.data["answer"]== answer.choice:
				correct=1
				print ("l")
			else:
				correct=0
				print("false")
			serializer.save(question_id=id,correct=correct)
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            	
class Result(APIView):
	def get(self,request):
		score=UserD.score(self)
		#serializer=UserL(score)
		return Response(score)
		
		

