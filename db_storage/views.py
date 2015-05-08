from django.shortcuts import render
from db_storage.models import Image
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.
class ImageView(View):
    def get(self, request, file_name):
        image = Image.objects.get(file_name=file_name)
        return HttpResponse(image.data, content_type=image.mimetype)
