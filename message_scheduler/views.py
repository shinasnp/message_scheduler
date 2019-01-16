from django.shortcuts import render
from scheduler.celery import schedule_message
from django.http import JsonResponse
from dateutil import parser
from django.views.decorators.csrf import csrf_exempt
import datetime


# Create your views here
@csrf_exempt
def message_schedule(request):
	'''
		This will schedule given message on given date time .
	'''
	datetime = request.POST.get('datetime')
	message = request.POST.get('message')
	if not message or not datetime:
		return JsonResponse(
			{
				"status":"ERROR",
				"message":" message or datetime is missing "
			},status=400)
	try:
		parsed_datetime = parser.parse(datetime)
		schedule_message.apply_async(args=(message,),eta=parsed_datetime)
		return JsonResponse(
			{
				"status":"SUCCESS",
				"message":" ACCEPTED "
			},status=202)

	except ValueError:
		return JsonResponse(
			{
				"status":"ERROR",
				"message":"datetime is not valid"
			},status=400)

