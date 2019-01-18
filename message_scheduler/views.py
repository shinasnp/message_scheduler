from django.shortcuts import render
from scheduler.celery import schedule_message
from django.http import JsonResponse
from dateutil import parser
from django.views.decorators.csrf import csrf_exempt
import datetime
import json
from tzlocal import get_localzone
import pytz


# Create your views here
@csrf_exempt
def message_schedule(request):
	'''
		This will schedule given message on given date time .
	'''
	data = json.loads(request.body)
	request_datetime = data.get('datetime')
	message = data.get('message')
	if not message or not request_datetime:
		return JsonResponse(
			{
				"status":"ERROR",
				"message":" message or datetime is missing "
			},status=400)
	try:

		parsed_datetime = parser.parse(request_datetime)
		if parsed_datetime > datetime.datetime.now():
			time_zone = pytz.timezone(get_localzone().zone)
			utc_date_time = time_zone.localize(parsed_datetime).astimezone(pytz.utc)
			schedule_message.apply_async(args=(message,),eta=utc_date_time)
			return JsonResponse(
				{
					"status":"SUCCESS",
					"message":" ACCEPTED "
				},status=202)
		else:
			return JsonResponse(
			{
				"status":"ERROR",
				"message":" datetime should be greater than current UTC time "
			},status=400)

	except ValueError:
		return JsonResponse(
			{
				"status":"ERROR",
				"message":"datetime is not valid"
			},status=400)

