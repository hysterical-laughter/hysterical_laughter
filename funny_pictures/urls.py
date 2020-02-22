from django.urls import path
from django.views.generic import TemplateView
from . import views
urlpatterns = [
	path('',	views.pictures,	name='pictures'),
	path('<image>/', views.image, name='image'),
	]
