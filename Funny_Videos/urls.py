from django.contrib.auth import views as V
from django.urls import path
from django.views.generic import TemplateView
from . import views
urlpatterns = [
	path('',	views.videos,	name='videos')
	]
