from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from logentries_logging.models import LogentriesConnection
import requests

# Create your views here.
class LogsView(View):
    def get(self, request):
        connection = LogentriesConnection.objects.get()
        url = 'https://pull.logentries.com/%s/%s/' % (connection.account_key, connection.log_addr)
        print url
        logs = requests.get(url)


        return HttpResponse(logs)
