from django.test import TestCase
from message_scheduler.views import message_schedule
import json

# Create your tests here.
class ScheduleTests(TestCase):

	def test_empty_data(self):
		"""
            Should return 400 on empty data
        """

		mimetype = 'application/json'
		headers = {
			"Content-Type": mimetype,
			"Accept": mimetype
		}
		data = {
			"message":"hellooo",
			"datetime":""
		}
		url = "/message/"
		response = self.client.post(url, data=data, headers=headers)
		assert response.status_code == 400

	def test_wrong_data(self):
		"""
            Should return 400 on invalid data
        """
		
		mimetype = 'application/json'
		headers = {
			"Content-Type": mimetype,
			"Accept": mimetype
		}
		data = {
			"message":"hellooo",
			"datetime":"434426633"
		}
		url = "/message/"
		response = self.client.post(url, data=data, headers=headers)
		assert response.status_code == 400

	def test_valid_data(self):
		"""
            Should return 202 on valid data
        """
		
		mimetype = 'application/json'
		headers = {
			"Content-Type": mimetype,
			"Accept": mimetype
		}
		data = {
			"message":"hellooo",
			"datetime":"16/01/2019 16:32"
		}
		url = "/message/"
		response = self.client.post(url, data=data, headers=headers)
		assert response.status_code == 202


