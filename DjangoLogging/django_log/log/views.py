from django.http import HttpResponse
from django.shortcuts import render
import logging
from datetime import datetime
# Create your views here.
logger = logging.getLogger(__name__)

def my_view(request):
    logger.info('Записываем request')
    logger.warning('Warning')
    logger.error('Ужасная ошибка')
    return HttpResponse("ok")

def home_view(request):
    user_visiting_time = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    logger.warning(f"Пользватель заходил в: {user_visiting_time}",)
    return HttpResponse("<h1>Welcome to web application development course 2023  (URFU/RTF)</h1>")