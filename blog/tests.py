from django.test import TestCase
from .tasks import send_email_task
from .views import check_params
import requests

# Create your tests here.
